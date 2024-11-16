from cmu_graphics import *
import string

def onAppStart(app):
    app.faceR = 10
    app.moodFaces = []
    app.inBox = False
    app.entry = ''
    app.page = 1
    app.textBoxLeft = 50
    app.textBoxTop = 50
    app.entryList = ["aldkfjadslkfjasklfjlaskjf"]

def makeTextBox(app):
    drawRect(app.textBoxLeft, app.textBoxTop, app.width-100, app.height/3, border='black', fill=None)
    if len(app.entry) == 0:
        drawLabel("How are you feeling today?", app.textBoxLeft+7, app.textBoxTop + 10, align='left', fill = 'gray', italic = True)

def updateTextBox(app):
    currentLine = app.textBoxTop
    for i in range(len(app.entryList)):
        currentLine = (app.textBoxTop+10) + (15*i)
        drawLabel(app.entryList[i], 57, currentLine, align='left', fill='black', size = 15)

    drawLabel(app.entry, 57, currentLine + 15, align='left', fill='black',size=15)

def onKeyPress(app, key):
    if app.inBox:
        if key == 'space':
            app.entry += " "
        elif key == 'backspace':
            app.entry = app.entry[:-1]
        elif key.isalpha() or key.isdigit() or key in string.punctuation:
            app.entry += key
        else:
            app.entry = app.entry

        

def onMousePress(app, mouseX, mouseY):
    if 50<=mouseX<=app.width-50 and 50<=mouseY<=app.height/3:
        app.inBox = True


def redrawAll(app):
    if app.page == 1:
        makeTextBox(app)
        updateTextBox(app)


class Account():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        app.name = None

class Calender():
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