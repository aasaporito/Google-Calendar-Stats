from datetime import datetime
import rfc3339
import iso8601

class Event:
	summary = ""
	id = ""
	startDateTime = ""
	endDateTime = ""
	duration = ""
	

	def __init__(self, event):
		self.summary = event['summary']
		self.id = event['id']
		self.startDateTime = get_date_object(event['start']['dateTime'])
		self.endDateTime = get_date_object(event['end']['dateTime'])
		
		self.duration = self.endDateTime-self.startDateTime

	def __str__(self):
		return "Summary: {} \nId: {} \nstartDateTime: {} \nendDateTime: {} \nDuration: {} \n\n".format(self.summary, self.id, self.startDateTime, self.endDateTime, self.duration)

def get_date_object(date_string):
	return iso8601.parse_date(date_string)

def get_date_string(date_object):
	return rfc3339.rfc3339(date_object)