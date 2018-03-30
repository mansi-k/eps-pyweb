from werkzeug.utils import secure_filename
import datetime
import time
import cx_Oracle

class RegistrationModel:
    
    __instance = None

    @staticmethod
    def getInstance(con, cur):
        """ Static access method. """
        if RegistrationModel.__instance == None:
            RegistrationModel(con, cur)
        return RegistrationModel.__instance

    def __init__(self, con, cur):
        """ Virtually private constructor. """
        if RegistrationModel.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            RegistrationModel.__instance = self
            self.con = con
            self.cur = cur

    def exParticipate(self, eid, uid):
        qr1 = self.cur.execute('select max(r_id) from mitali.registration')
        maxid = qr1.fetchall()
        i = maxid[0][0] + 1
        rows = [(i, uid, eid)]
        self.cur.bindarraysize = 1
        self.cur.setinputsizes(int, int, int)
        self.cur.executemany("insert into mitali.registration (r_id, r_uid, r_eid) VALUES (:1, :2, :3)", rows)
        self.con.commit()

    def exPCancel(self, rid):
        statement = 'delete from mitali.registration where r_id = :id'
        self.cur.execute(statement, {'id': int(rid)})
        self.con.commit()