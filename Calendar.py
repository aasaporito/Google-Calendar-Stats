class Calendar:
	summary = ""
	id = ""
	timeZone = ""

	isActive = True
	events = []

	def __init__(self, summary, id, timeZone, isActive):
		self.summary = summary
		self.id = id
		self.timeZone = timeZone
		self.isActive = isActive
		self.events = []