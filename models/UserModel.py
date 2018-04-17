from werkzeug.utils import secure_filename
import datetime
import time
import cx_Oracle
import tkinter
import tkinter.messagebox
from tkinter import messagebox as tkMessageBox


class UserModel:
    
    __instance = None

    @staticmethod
    def getInstance(con, cur):
        """ Static access method. """
        if UserModel.__instance == None:
            UserModel(con, cur)
        return UserModel.__instance

    def __init__(self, con, cur):
        """ Virtually private constructor. """
        if UserModel.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            UserModel.__instance = self
            self.con = con
            self.cur = cur

    def getUserData(self, res):
        log = "select * from reshma.useracc, reshma.usertype where u_type = ut_id and u_email= :email AND u_password= :pass"
        ex = self.cur.execute(log, {"email": res['email'], "pass": res['password']})
        data = ex.fetchall()
        if data != 0:
            return self.cur, data

    def getNewUser(self, res):
        test = "select count(*) from reshma.useracc where u_email= :email"
        qr1 = self.cur.execute(test, {'email': res['email']})
        cnt = qr1.fetchall()
        fcnt = cnt[0][0]
        if fcnt > 0:
           print("user alredy exist")
        else:
            typ = res['utype']
            test = "select max(u_id) from reshma.useracc"
            qr = self.cur.execute(test)
            maxid = qr.fetchall()
            i = maxid[0][0] + 1
            qc = "INSERT INTO reshma.useracc (u_id, u_type, u_name, u_mobno, u_address, u_city, u_email, u_password) VALUES(:1, :2, :3, :4, :5, :6, :7, :10)"
            self.cur.execute(qc, (
                i, typ, res['uname'], res['umobno'], res['uaddress'], res['ucity'], res['email'], res['password']))
            self.con.commit()
            if self.cur.rowcount > 0:
                return True
            else:
                return None



