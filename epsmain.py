from flask import Flask, render_template, request, redirect, url_for, json
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
    return xc.cSearch('ongoing')

@app.route('/fxsearch',methods = ['POST'])
def xfsearch():
    if request.method == 'POST':
        if 'xf' in request.json:
            res = xc.cXfSearch(request.json['xf'])
            return json.dumps(res,ensure_ascii=False)

@app.route('/details/<exid>')
def details(exid):
    eid, ecity = exid.split('|', 2)
    return xc.cDetails(eid, ecity)

@app.route('/participate',methods = ['POST'])
def participate():
    if request.method == 'POST':
        if 'usid' in request.json:
            if rc.cParticipate(request.json['usid']):
                return json.dumps({'status': 'ok'})
            else:
                return json.dumps({'status': 'fail'})
        elif 'rgid' in request.json:
            if rc.cPCancel(request.json['rgid']):
                return json.dumps({'status': 'ok'})
            else:
                return json.dumps({'status': 'fail'})

@app.route('/publish/')
def publish():
    return ec.cPublish()

@app.route('/onpublish',methods = ['POST'])
def onpublish():
    if request.method == 'POST':
        return ec.cOnPublish(request)

@app.route('/myparts')
def myparts():
    return rc.cMyParts()

@app.route('/publishedbyme/')
def pubyme():
    return ec.cPubyme()

@app.route('/edit/<exid>')
def edit(exid):
    eid, ecity = exid.split('|', 2)
    return ec.cExEdit(eid, ecity)

@app.route('/regs/<exid>')
def regs(exid):
    eid, ecity, ename = exid.split('|', 3)
    return ec.cExRegs(eid, ecity, ename)

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