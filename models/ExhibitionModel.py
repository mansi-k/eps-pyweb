from werkzeug.utils import secure_filename
import datetime
import time
import cx_Oracle

class ExhibitionModel:
    
    __instance = None

    @staticmethod
    def getInstance(con, cur):
        """ Static access method. """
        if ExhibitionModel.__instance == None:
            ExhibitionModel(con, cur)
        return ExhibitionModel.__instance

    def __init__(self, con, cur):
        """ Virtually private constructor. """
        if ExhibitionModel.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            ExhibitionModel.__instance = self
            self.con = con
            self.cur = cur

    def getCats(self):
        cats = self.cur.execute('select * from mansi.cat')
        return self.cur, cats.fetchall()

    def getAllExs(self, sess):
        qr1 = None
        if sess:
            uid = sess['u_id']
            statement = 'select * from reshma.pvfexhibition e left join mansi.cat c on ex_cat_id = cat_id left join mitali.registration on r_eid = ex_id and r_uid = :id order by ex_start_date'
            qr1 = self.cur.execute(statement, {'id': int(uid)})
        else:
            qr1 = self.cur.execute('select * from reshma.pvfexhibition left join mansi.cat on ex_cat_id = cat_id order by ex_start_date')
        entries = qr1.fetchall()
        exs = list()
        for entry in entries:
            ex = list(entry)
            ex[4] = datetime.datetime.strptime(str(ex[4]), '%Y-%m-%d %H:%M:%S').strftime("%B %d, %Y, %H:%M")
            exs += [ex]
        return self.cur, exs

    def exDetails(self,exid):
        statement = 'select * from mansi.exhibition, mansi.cat where ex_id = :id and cat_id = ex_cat_id'
        qr1 = self.cur.execute(statement, {'id': int(exid)})
        dets = list()
        for dt in qr1.fetchall():
            dets += [dt]
        return self.cur, dets

