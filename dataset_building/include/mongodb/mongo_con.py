'''
Created on 8 de set de 2020

@author: michel
'''

from pymongo.mongo_client import MongoClient

from helpers import conf_reader

class mongo_con:
    def connect_db(self):
        c_reader = conf_reader.conf_reader('../configuration.cfg')
        host = c_reader.getConf('general', 'host')
        method = c_reader.getConf('general', 'con_method')
        user = c_reader.getConf('security', 'user')
        password = c_reader.getConf('security', 'password') 
        extra = c_reader.getConf('security', 'extra_param')
        conString = method+"://"+user+":"+password+"@"+host+"/"+extra
        print(conString)
        self.mongoClient = MongoClient(conString)
        if self.mongoClient:
            return self.mongoClient
        else:
            return None
        
con = mongo_con()
con.connect_db()
print(con.mongoClient.database_names())   
