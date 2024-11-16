class DailyEntry():
    def __init__(self, journalEntry, mood):
        self.journalEntry = journalEntry
        self.mood = mood

    def setJournalEntry(self, journalEntry):
        self.jounalEntry = journalEntry

    def getJournalEntry(self):
        return self.journalEntry

    def getMood(self):
        return self.mood