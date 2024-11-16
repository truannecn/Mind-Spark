

class Account():
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Calender():
    def __init__(self):
        self.calender = {}

    def addEntry(self, date, entry):
        self.calender[date] = entry

class DailyEntry():
    def __init__(self, user):
        self.journalEntry = ''
        self.mood = None