from flask import Flask, render_template, request, redirect, url_for
from models.ExhibitionModel import ExhibitionModel
from SessionManager import SessionManager
import Helper as hp
import cx_Oracle


class ExhibitionController:
    __instance = None

    @staticmethod
    def getInstance(con, cur):
        """ Static access method. """
        if ExhibitionController.__instance == None:
            ExhibitionController(con, cur)
        return ExhibitionController.__instance

    def __init__(self, con, cur):
        """ Virtually private constructor. """
        if ExhibitionController.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            ExhibitionController.__instance = self
            self.con = con
            self.cur = cur
            self.xm = ExhibitionModel.getInstance(self.con, self.cur)
            self.sm = SessionManager.getInstance()

    def cSearch(self, xfilter):
        sess = self.sm.getSession()
        cursor, rows = self.xm.getFilterExs(xfilter)
        exs = hp.zip_data(cursor,rows)
        cursor, rows = self.xm.getCats()
        cats = hp.zip_data(cursor,rows)
        cursor, rows = self.xm.getCities()
        cts = hp.zip_data(cursor,rows)
        return render_template('exlist.html', exs=exs, sess=sess, cats=cats, cts=cts)

    def cXfSearch(self, xfilter):
        cursor, rows = self.xm.getFilterExs(xfilter)
        exs = hp.zip_data(cursor, rows)
        #print(exs)
        return exs

    def cDetails(self, exid, excity):
        sess = self.sm.getSession()
        #print("SESSION : "+sess)
        cursor, rows = self.xm.exDetails(exid, excity, sess)
        det = hp.zip_data(cursor, rows)
        cursor, rows = self.xm.exEnterprises(exid)
        entries = hp.zip_data(cursor, rows)
        return render_template('details.html', sess=sess, detail=det[0], ents=entries)