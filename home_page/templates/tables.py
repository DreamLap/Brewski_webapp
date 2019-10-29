from .models import Journal
from table import Table
from table.columns import Columns 

class JournalTable(Table):
	brew_name = Column(field='Brew Name')
	hop_name = Column(field='Hop Name');
	class Meta:
		model = Journal 
