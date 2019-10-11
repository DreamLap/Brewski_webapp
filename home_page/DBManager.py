# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 17:18:43 2019

@author: tyler
"""

import pymongo
from pymongo import MongoClient
  
# Get the service resource.
# table is the name of the table the instance will be working on
    
class DBManager:
   __instance = None
   __client = MongoClient()


   __db = __client['Brewjournal']
   __table = __db['Brewjournal']
   
   @staticmethod 
   def getInstance():
      """ Static access method. """
      if DBManager.__instance == None:
         DBManager()
      return DBManager.__instance
  
    
   '''
   x = DBManager.getInstance()
   key={
        'username': 'janedoe',
        'last_name': 'Doe'
            }

   print( x.getItem(key,'users'))
    '''
   def getItem(self, key,table):
       self.__table =  self.__db[table]
       response = self.__table.find_one(key)
       return response
   
    
    
   def saveItem(self, item, table):
       self.__table =  self.__db[table]
       self.__table.insert_one(item)
    
   def deleteItem(self,item,table):
       self.__table =  self.__db[table]
       self.__table.delete_one(item)

  
   def __init__(self):
      """ Virtually private constructor. """
      if DBManager.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         DBManager.__instance = self
    


    
