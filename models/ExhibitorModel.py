from werkzeug.utils import secure_filename
import datetime
import time
import cx_Oracle

class ExhibitorModel:

    __instance = None

    @staticmethod
    def getInstance(con, cur):
        """ Static access method. """
        if ExhibitorModel.__instance == None:
            ExhibitorModel(con, cur)
        return ExhibitorModel.__instance

    def __init__(self, con, cur):
        """ Virtually private constructor. """
        if ExhibitorModel.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            ExhibitorModel.__instance = self
            self.con = con
            self.cur = cur

    def exPublish(self, request, uid):
        rfd = request.form
        rff = request.files['exdoc']
        rff.save("exdocs/" + secure_filename(rff.filename))
        qr1 = self.cur.execute('select max(ex_id) from mansi.exhibition')
        maxid = qr1.fetchall()
        i = maxid[0][0] + 1
        exstart = datetime.datetime.strptime(rfd['exstart'], '%d-%m-%Y %H:%M:%S')
        exend = datetime.datetime.strptime(rfd['exend'], '%d-%m-%Y %H:%M:%S')
        rows = [(i, rfd['exname'], rfd['excat'], rfd['exaddress'], rfd['excity'], exstart, exend, uid, rff.filename, '',rfd['exvrr'], rfd['exnote'])]
        self.cur.bindarraysize = 1
        self.cur.setinputsizes(int, 20, int, 100, 20, cx_Oracle.TIMESTAMP, cx_Oracle.TIMESTAMP, int, 50, 5, 5, 100)
        self.cur.executemany("INSERT INTO mansi.exhibition (ex_id, ex_name, ex_cat_id, ex_address, ex_city, ex_start_date, ex_end_date, ex_creator_id, ex_doc, ex_is_verified, ex_is_vrr, ex_note) VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12)", rows)
        self.con.commit()

    def exPubyme(self, uid):
        statement = "select ex_id, ex_name from reshma.pvfexhibition  where ex_creator_id = :id"
        qr1 = self.cur.execute(statement, {'id': int(uid)})
        return self.cur, qr1.fetchall()

    def exEdit(self, eid):
        statement = 'select * from mansi.exhibition, mansi.cat where ex_id = :id and cat_id = ex_cat_id'
        qr1 = self.cur.execute(statement, {'id': int(eid)})
        return self.cur, qr1.fetchall()

    def exUpdate(self,request):
        rfd = request.form
        rff = request.files['exdoc']
        rff.save("exdocs/" + secure_filename(rff.filename))
        exstart = datetime.datetime.strptime(rfd['exstart'], '%d-%m-%Y %H:%M:%S')
        exend = datetime.datetime.strptime(rfd['exend'], '%d-%m-%Y %H:%M:%S')
        statement = 'update mansi.exhibition set ex_name = :1, ex_cat_id = :2, ex_address = :3, ex_city = :4, ex_start_date = :5, ex_end_date = :6, ex_creator_id = :7, ex_doc = :8, ex_is_vrr = :9, ex_note = :10 where ex_id = :11'
        self.cur.execute(statement, (rfd['exname'], rfd['excat'], rfd['exaddress'], rfd['excity'], exstart, exend, 1, rff.filename, rfd['exvrr'],rfd['exnote'], rfd['exupdate']))
        self.con.commit()

    def getExRegs(self, eid):
        statement = 'select * from mitali.registration, reshma.vfuseracc, reshma.usertype where r_eid = :id and r_uid = u_id and u_type = ut_id'
        qr1 = self.cur.execute(statement, {'id': int(eid)})
        return self.cur, qr1.fetchall()