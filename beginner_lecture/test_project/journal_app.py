from useful_tools import new_journal_page
from datetime import date 

example = new_journal_page(str(date.today()))

example.write("Journal entry for today")

example.close()