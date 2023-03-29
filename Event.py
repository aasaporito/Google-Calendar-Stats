class Event:
	summary = ""
	id = ""
	startDateTime = ""
	endDateTime = ""
	endTimeUnspecified = ""

	__init__(self, summary, id, startDateTime, endDateTime, endTimeUnspecified):
		self.summary = summary
		self.id = id
		self.startDateTime = startDateTime
		self.endDateTime = endDateTime
		self.endTimeUnspecified = endTimeUnspecified