from django.db import models
from .DBManager import DBManager
# Create your models here.



def create_journal(item, username):
	DB = DBManager.getInstance()
	Item={
					'JournalID': item,
					'UserID': username
		}
	DB.saveItem(Item,'Journal')

	
def register_user(username, password):
	DB = DBManager.getInstance()
	Item={
					'Username': username,
					'Password': password
		}
	DB.saveItem(Item,'Users')