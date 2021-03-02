'''
Created on 8 de set de 2020

@author: michel
'''

from pymongo.mongo_client import MongoClient

from helpers import ConfReader

class MongoCon:
    def connectDB(self):
        cReader = ConfReader.ConfReader('../mongodb.cfg')
        host = cReader.getConf('general', 'host')
        method = cReader.getConf('general', 'con_method')
        user = cReader.getConf('security', 'user')
        password = cReader.getConf('security', 'password') 
        extra = cReader.getConf('security', 'extra_param')
        conString = method+"://"+user+":"+password+"@"+host+"/"+extra
        print(conString)
        self.mongoClient = MongoClient(conString)
        if self.mongoClient:
            return self.mongoClient
        else:
            return None
        
con = MongoCon()
con.connectDB()
print(con.mongoClient.database_names())   
