from django.db import models
import .DBManager
# Create your models here.



def create_journal(item):
	DB = DBManager.getInstance()
	Item={
					'JournalID': item,
		}
	DB.saveItem(Item,'Brewjournal')
	
def register_user(username, password):
	DB = DBManager.getInstance()
	Item={
					'Username': username,
					'Password': password
		}
	DB.saveItem(Item,'Users')