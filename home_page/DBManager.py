# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 17:18:43 2019

@author: tyler
"""

import boto3
  
# Get the service resource.
# table is the name of the table the instance will be working on
    
class DBManager:
   __instance = None
   __dynamodb = boto3.resource('dynamodb', 
                               region_name='us-east-1',
                               aws_access_key_id='AKIAJTNALKALUKKL3XUQ',
                               aws_secret_access_key='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')
   __table = __dynamodb.Table('users')
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
       self.__table =  self.__dynamodb.Table(table)
       response = self.__table.get_item(Key = key)
       return response['Item']
   
    
    
   def saveItem(self, item, table):
       self.__table =  self.__dynamodb.Table(table)
       self.__table.put_item(Item=item)


  
   def __init__(self):
      """ Virtually private constructor. """
      if DBManager.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         DBManager.__instance = self
    


    
'''
dynamodb = boto3.resource('dynamodb', 
                               region_name='us-east-1',
                               aws_access_key_id='AKIAJTNALKALUKKL3XUQ',
                               aws_secret_access_key='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')
table = dynamodb.Table('users')
    


table.put_item(
   Item={
        'username': 'janedoe',
        'first_name': 'Jane',
        'last_name': 'Doe',
        'age': 25,
        'account_type': 'standard_user',
    }
)



response = table.get_item(
    Key={
        'username': 'janedoe',
        'last_name': 'Doe'
    }
)
item = response['Item']
print(item)



table.update_item(
    Key={
        'username': 'janedoe',
        'last_name': 'Doe'
    },
    UpdateExpression='SET age = :val1',
    ExpressionAttributeValues={
        ':val1': 26
    }
)




table.delete_item(
    Key={
        'username': 'janedoe',
        'last_name': 'Doe'
    }
)




response = table.query(
    KeyConditionExpression=Key('username').eq('johndoe')
)
items = response['Items']
print(items)
'''