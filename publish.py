from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import datetime
import time
import cx_Oracle

app = Flask(__name__)

con = cx_Oracle.connect('system/mansik123@127.0.0.1/XE')

@app.route('/eps')
def hello_world():
	return 'Hello, World!'

def rows_to_dict_list(cursor, rows):
    columns = [i[0].lower() for i in cursor.description]
    return [dict(zip(columns, row)) for row in rows]

@app.route('/publish/')
def publish():
	cur = con.cursor()
	cur = cur.execute('select * from mansi.cat')
	entries = cur.fetchall()
	return render_template("publish.html",cats = entries)

@app.route('/result',methods = ['POST'])
def result():
	if request.method == 'POST':
		res = request.form
		#return render_template("result.html",result = res)
		f = request.files['exdoc']
		f.save("docs/"+secure_filename(f.filename))
		cur = con.cursor()
		qr1 = cur.execute('select max(ex_id) from mansi.exhibition')
		maxid = qr1.fetchall()
		i = maxid[0][0]+1
		exstart = datetime.datetime.strptime(res['exstart'], '%d-%m-%Y %H:%M:%S')
		#res['exstart'] = time.mktime(d.timetuple())
		exend = datetime.datetime.strptime(res['exend'], '%d-%m-%Y %H:%M:%S')
		rows = [ (i, res['exname'], res['excat'], res['exaddress'], res['excity'], exstart, exend, 1, f.filename, '', res['exvrr'], res['exnote']) ]
		cur.bindarraysize = 1
		cur.setinputsizes(int, 20, int, 100, 20, cx_Oracle.TIMESTAMP, cx_Oracle.TIMESTAMP, int, 50, 5, 5, 100)
		cur.executemany("INSERT INTO mansi.exhibition (ex_id, ex_name, ex_cat_id, ex_address, ex_city, ex_start_date, ex_end_date, ex_creator_id, ex_doc, ex_is_verified, ex_is_vrr, ex_note) VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12)", rows)
		con.commit()
		return redirect(url_for('search'))

@app.route('/participate',methods = ['GET'])
def participate():
	if request.method == 'GET':
		if request.args.get('pexbtn') :
			rid = request.args.get('pexbtn')
			cur = con.cursor()
			qr1 = cur.execute('select max(r_id) from mitali.registration')
			maxid = qr1.fetchall()
			i = maxid[0][0]+1
			rows = [ (i, 10, res['pexbtn']) ]
			cur.bindarraysize = 1
			cur.setinputsizes(int, int, int)
			qr1 = cur.executemany("insert into mitali.registration (r_id, r_uid, r_eid) VALUES (:1, :2, :3)", rows)
			con.commit()
		elif request.args.get('cexbtn') :
			cur = con.cursor()
			rid = request.args.get('cexbtn')
			statement = 'delete from mitali.registration where r_id = :id'
			cur.execute(statement, {'id':int(rid)})
			con.commit()
	return redirect(url_for('search'))

@app.route('/search/')
def search():
	cur = con.cursor()
	qr1 = cur.execute('select * from mansi.exhibition e left join mansi.cat c on ex_cat_id = cat_id left join mitali.registration on r_eid = ex_id and r_uid = 10 order by ex_id')
	entries = qr1.fetchall()
	exs = list()
	for entry in entries:
		ex = list(entry)
		ex[5] = datetime.datetime.strptime(str(ex[5]), '%Y-%m-%d %H:%M:%S').strftime("%B %d, %Y, %H:%M")
		exs += [ex]
	exd = rows_to_dict_list(cur, exs)
	cur = con.cursor()
	qr2 = cur.execute('select * from mitali.registration where r_uid=10')
	regs = qr2.fetchall()
	return render_template("result.html",result = exd)

@app.route('/details/<exid>')
def details(exid):
	cur = con.cursor()
	statement = 'select * from mansi.exhibition, mansi.cat where ex_id = :id and cat_id = ex_cat_id'
	qr1 = cur.execute(statement, {'id':int(exid)})
	dets = list()
	for dt in qr1.fetchall():
		dets += [dt]
	det = rows_to_dict_list(cur, dets)
	return render_template("details.html",detail = det)

@app.route('/publishedbyme')
def pubyme():
	cur = con.cursor()
	qr1 = cur.execute("select ex_id, ex_name from mansi.exhibition where ex_creator_id = 1")
	det = qr1.fetchall()
	return render_template("createdex.html",exs = det)

@app.route('/editex')
def editex():
	if request.method == 'GET':
		if request.args.get('xedit') :
			eid = request.args.get('xedit')
			cur = con.cursor()
			statement = 'select * from mansi.exhibition, mansi.cat where ex_id = :id and cat_id = ex_cat_id'
			qr1 = cur.execute(statement, {'id':int(eid)})
			dets = list();
			for dt in qr1.fetchall():
				dets += [dt]
			det = rows_to_dict_list(cur, dets)
			cur = cur.execute('select * from mansi.cat')
			entries = cur.fetchall()
			return render_template("editex.html",ex = det[0], cats = entries)
		elif request.args.get('xparts') :
			eid = request.args.get('xparts')
			cur = con.cursor()
			statement = 'select * from mitali.registration, reshma.useracc, reshma.usertype where r_eid = :id and r_uid = u_id and u_type = ut_id'
			qr1 = cur.execute(statement, {'id':int(eid)})
			dets = list();
			for dt in qr1.fetchall():
				dets += [dt]
			det = rows_to_dict_list(cur, dets)
			return render_template("regs.html",regs = det)
		
@app.route('/update',methods = ['POST'])
def update():
	if request.method == 'POST':
		res = request.form
		#return render_template("result.html",result = res)
		f = request.files['exdoc']
		f.save("docs/"+secure_filename(f.filename))
		cur = con.cursor()
		exstart = datetime.datetime.strptime(res['exstart'], '%d-%m-%Y %H:%M:%S')
		#res['exstart'] = time.mktime(d.timetuple())
		exend = datetime.datetime.strptime(res['exend'], '%d-%m-%Y %H:%M:%S')
		#rows = [ (i, res['exname'], res['excat'], res['exaddress'], res['excity'], exstart, exend, 1, f.filename, '', res['exvrr'], res['exnote']) ]
		statement = 'update mansi.exhibition set ex_name = :1, ex_cat_id = :2, ex_address = :3, ex_city = :4, ex_start_date = :5, ex_end_date = :6, ex_creator_id = :7, ex_doc = :8, ex_is_vrr = :9, ex_note = :10 where ex_id = :11'
		cur.execute(statement, (res['exname'], res['excat'], res['exaddress'], res['excity'], exstart, exend, 1, f.filename, res['exvrr'], res['exnote'], res['exupdate']))
		con.commit()
		return redirect(url_for('pubyme'))


if __name__ == '__main__':
   	app.run(debug = True)

'''
db = connect_db()
cur = db.execute('select * from mansi.cat')
entries = cur.fetchall()
for result in entries:
	print(result)
'''

