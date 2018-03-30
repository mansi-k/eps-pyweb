from flask import Flask, render_template, request, redirect, url_for
from models.RegistrationModel import RegistrationModel
from SessionManager import SessionManager
import Helper as hp
import cx_Oracle

class RegistrationController:
    __instance = None

    @staticmethod
    def getInstance(con, cur):
        """ Static access method. """
        if RegistrationController.__instance == None:
            RegistrationController(con, cur)
        return RegistrationController.__instance

    def __init__(self, con, cur):
        """ Virtually private constructor. """
        if RegistrationController.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            RegistrationController.__instance = self
            self.con = con
            self.cur = cur
            self.rm = RegistrationModel.getInstance(self.con, self.cur)
            self.sm = SessionManager.getInstance()

    def cParticipate(self, eid):
        sess = self.sm.getSession()
        if sess:
            self.rm.exParticipate(eid, sess['u_id'])
        return redirect(url_for('search'))

    def cPCancel(self, rid):
        sess = self.sm.getSession()
        if sess:
            self.rm.exPCancel(rid)
        return redirect(url_for('search'))