from django.db import models
import .DBManager
# Create your models here.



def create_journal(item):
	DB = DBManager.getInstance()
	Item={
					'JournalID': item,
		}
	DB.saveItem(Item,'Journal')