from flask import Flask, render_template, request, redirect, url_for
from SessionManager import SessionManager
import cx_Oracle

class EPSController :
    
    __instance = None

    @staticmethod
    def getInstance(con, cur):
        """ Static access method. """
        if EPSController.__instance == None:
            EPSController(con, cur)
        return EPSController.__instance

    def __init__(self, con, cur):
        """ Virtually private constructor. """
        if EPSController.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            EPSController.__instance = self
            self.con = con
            self.cur = cur
            self.sm = SessionManager.getInstance()

    def cIndex(self):
        return render_template('index.html', sess=self.sm.getSession())



















