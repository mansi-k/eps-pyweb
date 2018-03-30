from werkzeug.utils import secure_filename
import datetime
import time
import cx_Oracle

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

    def getUserData(self, uid):
        statement = "select u.*, t.ut_type from reshma.useracc u, reshma.usertype t where u_id = :id and u_type = ut_id"
        qr1 = self.cur.execute(statement, {'id': int(uid)})
        return self.cur, qr1.fetchall()
