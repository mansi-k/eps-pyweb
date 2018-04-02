from werkzeug.utils import secure_filename
import datetime
import time
import cx_Oracle

class ExhibitionModel:
    
    __instance = None

    @staticmethod
    def getInstance(con, cur):
        """ Static access method. """
        if ExhibitionModel.__instance == None:
            ExhibitionModel(con, cur)
        return ExhibitionModel.__instance

    def __init__(self, con, cur):
        """ Virtually private constructor. """
        if ExhibitionModel.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            ExhibitionModel.__instance = self
            self.con = con
            self.cur = cur

    def getCats(self):
        cats = self.cur.execute('select * from mansi.cat')
        return self.cur, cats.fetchall()

    '''
    def getAllExs(self):
        qr1 = self.cur.execute('select * from reshma.pvfexhibition left join mansi.cat on ex_cat_id = cat_id order by ex_start_date')
        entries = qr1.fetchall()
        cdt = datetime.datetime.strptime(str(datetime.datetime.now()).split('.', 1)[0], '%Y-%m-%d %H:%M:%S')
        #print(str(cdt))
        exd = {}
        exs = list()
        for entry in entries:
            ex = list(entry)
            sdt = datetime.datetime.strptime(str(ex[4]), '%Y-%m-%d %H:%M:%S')
            edt = datetime.datetime.strptime(str(ex[5]), '%Y-%m-%d %H:%M:%S')
            ex[4] = sdt.strftime("%B %d, %Y, %H:%M")
            exs += [ex]
            if sdt <= cdt and cdt <= edt:
                exd[ex[0]] = 'ongoing'
            elif sdt > cdt:
                exd[ex[0]] = 'upcoming'
            elif cdt > edt:
                exd[ex[0]] = 'past'
            #print(str(exd))
        return self.cur, exs, exd
    '''

    def getFilterExs(self,xfilter):
        qr1 = None
        if xfilter == 'ongoing':
            qr1 = self.cur.execute('select * from reshma.pvfexhibition left join mansi.cat on ex_cat_id = cat_id where ex_start_date >= current_timestamp and ex_end_date <= current_timestamp order by ex_start_date')
        elif xfilter == 'upcoming':
            qr1 = self.cur.execute('select * from reshma.pvfexhibition left join mansi.cat on ex_cat_id = cat_id where ex_start_date > current_timestamp order by ex_start_date')
        elif xfilter == 'past':
            qr1 = self.cur.execute('select * from reshma.pvfexhibition left join mansi.cat on ex_cat_id = cat_id where ex_start_date < current_timestamp order by ex_start_date')
        entries = qr1.fetchall()
        exs = list()
        for entry in entries:
            ex = list(entry)
            ex[1] = ex[1].title()
            ex[3] = ex[3].title()
            ex[9] = ex[9].title()
            sdt = datetime.datetime.strptime(str(ex[4]), '%Y-%m-%d %H:%M:%S')
            edt = datetime.datetime.strptime(str(ex[5]), '%Y-%m-%d %H:%M:%S')
            ex[4] = sdt.strftime("%B %d, %Y, %H:%M")
            ex[5] = sdt.strftime("%B %d, %Y, %H:%M")
            exs += [ex]
        return self.cur, exs


    def exDetails(self,exid,excity,sess):
        qr1 = None
        if sess:
            uaid = sess['u_id']
            if excity.lower() == 'mumbai':
                statement = 'select * from reshma.phfexcitym left join mansi.cat on ex_cat_id = cat_id left join reshma.vfuseracc on ex_creator_id = u_id left join mitali.registration on r_eid = ex_id and r_uid = :uaid where ex_id = :eid'
                qr1 = self.cur.execute(statement, {'uaid': int(uaid), 'eid': int(exid)})
            elif excity.lower() == 'delhi':
                statement = 'select * from sarthak.phfexcityd left join mansi.cat on ex_cat_id = cat_id left join reshma.vfuseracc on ex_creator_id = u_id left join mitali.registration on r_eid = ex_id and r_uid = :uaid where ex_id = :eid'
                qr1 = self.cur.execute(statement, {'uaid': int(uaid), 'eid': int(exid)})
            elif excity.lower() == 'banglore':
                statement = 'select * from mitali.phfexcityb left join mansi.cat on ex_cat_id = cat_id left join reshma.vfuseracc on ex_creator_id = u_id left join mitali.registration on r_eid = ex_id and r_uid = :uaid where ex_id = :eid'
                qr1 = self.cur.execute(statement, {'uaid': int(uaid), 'eid': int(exid)})
            else:
                statement = 'select * from mansi.phfexcityo left join mansi.cat on ex_cat_id = cat_id left join reshma.vfuseracc on ex_creator_id = u_id left join mitali.registration on r_eid = ex_id and r_uid = :uaid where ex_id = :eid'
                qr1 = self.cur.execute(statement, {'uaid': int(uaid), 'eid': int(exid)})
        else:
            if excity.lower() == 'mumbai':
                statement = 'select * from mansi.exhibition, mansi.cat, reshma.useracc where ex_id = :eid and ex_cat_id = cat_id and ex_creator_id = u_id'
                qr1 = self.cur.execute(statement, {'eid': int(exid)})
            elif excity.lower() == 'delhi':
                statement = 'select * from mansi.exhibition, mansi.cat, reshma.useracc where ex_id = :eid and ex_cat_id = cat_id and ex_creator_id = u_id'
                qr1 = self.cur.execute(statement, {'eid': int(exid)})
            elif excity.lower() == 'banglore':
                statement = 'select * from mansi.exhibition, mansi.cat, reshma.useracc where ex_id = :eid and ex_cat_id = cat_id and ex_creator_id = u_id'
                qr1 = self.cur.execute(statement, {'eid': int(exid)})
            else:
                statement = 'select * from mansi.exhibition, mansi.cat, reshma.useracc where ex_id = :eid and ex_cat_id = cat_id and ex_creator_id = u_id'
                qr1 = self.cur.execute(statement, {'eid': int(exid)})
        dets = list()
        for dt in qr1.fetchall():
            dets += [dt]
        return self.cur, dets

    def exEnterprises(self, exid):
        statement = 'select u_name from reshma.useracc, mitali.registration where u_id = r_uid and r_eid = :id'
        qr1 = self.cur.execute(statement, {'id': int(exid)})
        entries = list()
        for dt in qr1.fetchall():
            entries += [dt]
        return self.cur, entries

    def getCities(self):
        qr1 = self.cur.execute('select unique ex_city from reshma.pvfexhibition')
        cities = list()
        for ct in qr1.fetchall():
            cities += [ct]
        return self.cur, cities

