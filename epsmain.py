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
    return xc.cSearch()


@app.route('/details/<exid>')
def details(exid):
    return xc.cDetails(exid)


@app.route('/participate', methods=['POST'])
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


@app.route('/onpublish', methods=['POST'])
def onpublish():
    if request.method == 'POST':
        return ec.cOnPublish(request)


@app.route('/publishedbyme/')
def pubyme():
    return ec.cPubyme()


@app.route('/edit/<exid>')
def edit(exid):
    return ec.cExEdit(exid)


@app.route('/regs/<exid>')
def regs(exid):
    return ec.cExRegs(exid)


@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        return ec.cUpdatex(request)


@app.route('/log')
def log():
        return uc.clog()

@app.route('/user')
def user():
        return uc.cuser()


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        res = request.form
        return uc.cLogin(res)
    return render_template("login.html")

@app.route('/suser')
def suser():
        return uc.suser()


@app.route("/signup", methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        res = request.form
        return uc.cSignup(res)
    return render_template('signup.html')

@app.route('/logout')
def logout():
    return uc.cLogout()

@app.route('/myparts')
def myparts():
    return rc.cMyParts()

if __name__ == '__main__':
    app.run(debug=True)