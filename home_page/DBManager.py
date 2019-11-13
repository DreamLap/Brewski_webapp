# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 17:18:43 2019

@author: tyler
"""

import pymongo
from pymongo import MongoClient
from bson import ObjectId
  
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
   def getItemByID(self, key, table):
       if ObjectId.is_valid(key) == False:
          return None
       self.__table =  self.__db[table]
       response = self.__table.find_one(ObjectId(key))
       return response

    
   def saveItem(self, item, table):
       self.__table =  self.__db[table]
       self.__table.insert_one(item)


   def deleteItemByID(self, key, table):
       self.__table =  self.__db[table]
       self.__table.delete_one({'_id': ObjectId(key)})

   
   def favoriteJournalByID(self, journal_id, username):
       print('add journal to favs')
       self.__table =  self.__db['Favorites']
       query = {'_id': str(username)}
       add_value = {"$push": {'Favorites_list': journal_id}}
       self.__table.update(query, add_value)
       #print('user db response: ')

   def getFavoriteJournalList(self, username):
       self.__table =  self.__db['Favorites']
       mydoc = self.__table.find({'_id': str(username)})

       #gets 'Favorites' table with user info
       my_list = []
       #my_list.append(mydoc[0])
       for x in mydoc:
         x['id'] = x.pop('_id')
         my_list.append(x)

       #converts pointer to object
       favortie_list = []
       for journal_id in my_list[0]['Favorites_list']:
          entry = self.getItemByID(journal_id, 'Journal')
          entry['id'] = entry.pop('_id')
          favortie_list.append(entry)
       

       return favortie_list

       


   def createFavoritesForUser(self, username):
       self.__table = self.__db['Favorites']
       self.__table.insert_one({'_id': str(username), 'Favorites_list': []})


   def getAllJournals(self):
      mycol = self.__db["Journal"]
      mydoc = mycol.find()
      my_list = []
      for x in mydoc:
         x['id'] = x.pop('_id')
         my_list.append(x)
      #print(my_list)
      return my_list
   
   def editItem(self, item, table, journal_id):
      print('----')
      print('item: ', item)
      print('table: ', table )
      print('journal_id: ', journal_id )
      print('-------')

      self.__table =  self.__db[table]
      self.__table.find_one_and_replace( {"_id" : ObjectId(journal_id)}, item, upsert = True )


   def __init__(self):
      """ Virtually private constructor. """
      if DBManager.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         DBManager.__instance = self

