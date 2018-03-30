from flask import Flask, render_template, request, redirect, url_for
from models.UserModel import UserModel
from SessionManager import SessionManager
import Helper as hp
import cx_Oracle


class UserController:
    __instance = None

    @staticmethod
    def getInstance(con, cur):
        """ Static access method. """
        if UserController.__instance == None:
            UserController(con, cur)
        return UserController.__instance

    def __init__(self, con, cur):
        """ Virtually private constructor. """
        if UserController.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            UserController.__instance = self
            self.con = con
            self.cur = cur
            self.um = UserModel.getInstance(self.con, self.cur)
            self.sm = SessionManager.getInstance()

    def cLogin(self, uid):
        sess = self.sm.getSession()
        if sess is None:
            cursor, rows = self.um.getUserData(uid)
            udata = hp.zip_data(cursor, rows)
            self.sm.setSession(udata[0])
            return render_template("login.html", sess=self.sm.getSession())
        else:
            return redirect(url_for('search'))

    def cLogout(self):
        self.sm.destroySession()
        return redirect(url_for('index'))