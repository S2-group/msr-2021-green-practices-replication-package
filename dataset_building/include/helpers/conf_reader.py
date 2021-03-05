'''
Created on 12 de set. de 2020

@author: michel
'''

from configparser import ConfigParser

class conf_reader:
    
    conf = ConfigParser()

    def __init__(self, cfile):
        self.conf.read(cfile)
        
    def getConf(self, s, c):
        cfg = self.conf.get(s,c)
        return cfg
