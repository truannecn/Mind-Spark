

class Account():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.name = None
        self.calender = UserCalender()

class UserCalender():
    def __init__(self):
        self.calender = {}

    def addEntry(self, date, entry):
        self.calender[date] = entry

    def getEntry(self, date):
        return self.calender.get(date, None)

class DailyEntry():
    def __init__(self, user):
        self.journalEntry = ''
        self.mood = None

    def setJournalEntry(self, journalEntry):
        self.jounalEntry = journalEntry

    def getJournalEntry(self):
        return self.journalEntry

def main():
    runApp()

main()