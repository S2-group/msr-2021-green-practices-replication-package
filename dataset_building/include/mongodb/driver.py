'''
Created on 8 de set de 2020

@author: michel
'''
from mongodb import  mongo_con


global client
client = mongo_con.con.mongoClient
            
def insertIntoCollection(database, col, doc):
    if client != None:
        db = client[database]
        c = db[col]
        c.insert_one(doc)
    else:
        print('MongoDB is unreachable!')

#d = { "name": "John", "address": "Highway 37" }
#insertIntoCollection('data_phase1','test1',d)
