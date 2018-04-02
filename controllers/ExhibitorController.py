from flask import Flask, render_template, request, redirect, url_for
from models.ExhibitorModel import ExhibitorModel
from models.ExhibitionModel import ExhibitionModel
from SessionManager import SessionManager
import Helper as hp
import cx_Oracle

class ExhibitorController:
    __instance = None

    @staticmethod
    def getInstance(con, cur):
        """ Static access method. """
        if ExhibitorController.__instance == None:
            ExhibitorController(con, cur)
        return ExhibitorController.__instance

    def __init__(self, con, cur):
        """ Virtually private constructor. """
        if ExhibitorController.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            ExhibitorController.__instance = self
            self.con = con
            self.cur = cur
            self.em = ExhibitorModel.getInstance(self.con, self.cur)
            self.xm = ExhibitionModel.getInstance(self.con, self.cur)
            self.sm = SessionManager.getInstance()
            
    def cPublish(self):
        sess = self.sm.getSession()
        if sess and sess['ut_type'] == 'exhibitor':
            cursor, rows = self.xm.getCats()
            cats = hp.zip_data(cursor,rows)
            return render_template('publish.html', cats=cats, sess=sess)
        else:
            return render_template('error.html', msg='Please login to exhibitor\'s account')

    def cOnPublish(self, request):
        sess = self.sm.getSession()
        if sess and sess['ut_type'] == 'exhibitor':
            self.em.exPublish(request, sess['u_id'])
        return redirect(url_for('search'))

    def cPubyme(self):
        sess = self.sm.getSession()
        if sess and sess['ut_type'] == 'exhibitor':
            cursor, rows = self.em.exPubyme(sess['u_id'])
            exs = hp.zip_data(cursor, rows)
            return render_template('createdex.html', exs=exs, sess=sess)
        else:
            return render_template('error.html', msg='Please login to exhibitor\'s account')


    def cExEdit(self, eid, ecity):
        sess = self.sm.getSession()
        if sess and sess['ut_type'] == 'exhibitor':
            cursor, rows = self.em.exEdit(eid, ecity)
            det = hp.zip_data(cursor, rows)
            cursor, rows = self.xm.getCats()
            cats = hp.zip_data(cursor, rows)
            return render_template("editex.html", ex=det[0], cats=cats)
        else :
            return render_template('error.html', msg='Please login to exhibitor\'s account')

    def cUpdatex(self, request):
        sess = self.sm.getSession()
        if sess and sess['ut_type'] == 'exhibitor':
            self.em.exUpdate(request)
        return redirect(url_for('pubyme'))

    def cExRegs(self, eid, ecity, ename):
        sess = self.sm.getSession()
        if sess and sess['ut_type'] == 'exhibitor':
            cursor, rows = self.em.getExRegs(eid, ecity)
            regs = hp.zip_data(cursor, rows)
            return render_template("regs.html",regs = regs, ename=ename, sess=sess)
        else:
            return render_template('error.html', msg='Please login to exhibitor\'s account')