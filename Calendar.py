class Calendar:
	summary = ""
	id = ""
	timeZone = ""

	isActive = True

	def __init__(self, summary, id, timeZone, isActive):
		self.summary = summary
		self.id = id
		self.timeZone = timeZone
		self.isActive = isActive

	def __init__(self, summary, id, timeZone):
		self.summary = summary
		self.id = id
		self.timeZone = timeZone
		self.isActive = True
