from flask import Flask, render_template, request, redirect, url_for
from controllers.EPSController import EPSController
from controllers.UserController import UserController
from controllers.ExhibitionController import ExhibitionController
from controllers.ExhibitorController import ExhibitorController
from controllers.RegistrationController import RegistrationController
import Helper as hp
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

global con, cur, ic, uc, xc, ec, rc
con, cur = hp.connectDB()
ic = EPSController.getInstance(con, cur)
uc = UserController.getInstance(con, cur)
xc = ExhibitionController.getInstance(con, cur)
ec = ExhibitorController.getInstance(con, cur)
rc = RegistrationController.getInstance(con, cur)

@app.route('/')
def index():
    return ic.cIndex()

@app.route('/search/')
def search():
    return xc.cSearch()

@app.route('/details/<exid>')
def details(exid):
    return xc.cDetails(exid)

@app.route('/participate',methods = ['GET'])
def participate():
    if request.method == 'GET':
        if request.args.get('pexbtn'):
            return rc.cParticipate(request.args.get('pexbtn'))
        elif request.args.get('cexbtn'):
            return rc.cPCancel(request.args.get('cexbtn'))

@app.route('/publish/')
def publish():
    return ec.cPublish()

@app.route('/onpublish',methods = ['POST'])
def onpublish():
    if request.method == 'POST':
        return ec.cOnPublish(request)

@app.route('/publishedbyme/')
def pubyme():
    return ec.cPubyme()

@app.route('/exaction',methods = ['GET'])
def exaction():
    if request.method == 'GET':
        if request.args.get('xedit'):
            return ec.cExEdit(request.args.get('xedit'))
        elif request.args.get('xparts'):
            return ec.cExRegs(request.args.get('xparts'))

@app.route('/update',methods = ['POST'])
def update():
    if request.method == 'POST':
        return ec.cUpdatex(request)

@app.route('/login/<uid>')
def login(uid):
    return uc.cLogin(uid)

@app.route('/logout')
def logout():
    return uc.cLogout()


if __name__ == '__main__':
    app.run(debug = True)