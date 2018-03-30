from flask import session

class SessionManager:
    
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if SessionManager.__instance == None:
            SessionManager()
        return SessionManager.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if SessionManager.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            SessionManager.__instance = self

    def issetSession(self):
        if session.get('user'):
            return True
        else:
            return False

    def setSession(self, data):
        if not self.issetSession():
            session['user'] = data

    def getSession(self):
        if self.issetSession():
            return session['user']
        else:
            return None

    def destroySession(self):
        session.pop('user', None)
        SessionManager.__instance = None



