from cmu_graphics import *
import string
import calendar

######
# ON APP START
######
def onAppStart(app):
    app.page = 'mood'
    app.users = []

    #login page app variables
    app.username = ''
    app.password = ''
    app.currentUser = None

    #user variables
    app.calender = UserCalender()

    #mood app variables
    app.mood = None
    app.mood0w = app.mood1w = app.mood2w = app.mood3w = app.mood4w = 50

    #textBox app variables
    app.inBox = False
    app.entry = ''
    app.textBoxLeft = 50
    app.textBoxTop = 50
    app.entryList = []
    
    app.hold = False

    app.happy2 = 'smile.png'
    app.happy1 = 'smile (1).png'
    app.middle = 'sceptic.png'
    app.sad1 = 'sceptic (1).png'
    app.sad2 = 'crying.png'



######
# ON KEY PRESS
######
def onKeyPress(app, key):
    if app.inBox:
        if len(app.entry) >= 115:
            app.entryList.append(app.entry)
            app.entry = ''
        if key == 'space':
            app.entry += " "
        elif key == 'backspace':
            if len(app.entryList) != 0 or len(app.entry) != 0:
                if len(app.entry) > 0:
                    app.entry = app.entry[:-1]
                elif len(app.entry) == 0:
                    app.entry = app.entryList[0]
                    app.entryList.pop()
                    app.entry = app.entry[:-1]
            
        elif key in string.ascii_letters or key in string.digits or key in string.punctuation:
            app.entry += key
            

#####
# ON MOUSE PRESS
#####
def onMousePress(app, mouseX, mouseY):
    if app.page == 'journal entry':
        if 50<=mouseX<=app.width-50 and 50<=mouseY<=app.height/3:
            app.inBox = True
    elif app.page == 'mood':
        if app.height/2 + 25 <= mouseY <= app.height/2 + 75:
            if app.width/2-225<= mouseX <= app.width/2-175:
                app.mood = 0
            elif app.width/2-125 <= mouseX <= app.width/2-75 :
                app.mood = 1
            elif app.width/2-25 <= mouseX <= app.width/2 + 25:
                app.mood = 2
            elif app.width/2+75 <= mouseX <= app.width/2 + 125:
                app.mood = 3
            elif app.width/2 + 175 <= mouseX <= app.width/2 + 225: 
                app.mood = 4

#####
# REDRAW ALL
#####
def redrawAll(app):
    if app.page == "landing page":
        drawLandingPage(app)
    if app.page == 'journal entry':
        makeTextBox(app)
        updateTextBox(app)
    elif app.page == 'mood':
        drawMoods(app)
    elif app.page == 'calender view':
        drawCalender(app, app.calender)
        
def drawLandingPage(app):
    pass
    

def makeTextBox(app):
    drawRect(app.textBoxLeft, app.textBoxTop, app.width-100, app.height/3, border='black', fill=None)
    if len(app.entry) == 0 and len(app.entryList) == 0:
        drawLabel("How are you feeling today?", app.textBoxLeft+7, app.textBoxTop + 15, align='left', fill = 'gray', italic = True, size = 20)

def updateTextBox(app):
    currentLine = app.textBoxTop
    for i in range(len(app.entryList)):
        currentLine = (app.textBoxTop+10) + (15*i)
        drawLabel(app.entryList[i], 57, currentLine, align='left', fill='black', size = 20, font = 'monospace')

    drawLabel(app.entry, 57, currentLine + 15, align='left', fill='black', size = 20, font = 'monospace')

def drawMoods(app):
    drawLabel("How are you feeling today?", app.width/2, app.height/2, align='center', size=20, bold=True)
    drawCircle(app.width/2-200, app.height/2 + 50, app.mood0w/2, fill='blue', opacity=60)
    drawCircle(app.width/2-100, app.height/2 + 50, app.mood1w/2, fill='lightBlue', opacity=60)
    drawCircle(app.width/2, app.height/2 + 50, app.mood2w/2, fill='yellow', opacity=60)
    drawCircle(app.width/2+100, app.height/2 + 50, app.mood3w/2, fill='lightGreen', opacity=60)
    drawCircle(app.width/2+200, app.height/2 + 50, app.mood4w/2, fill='green', opacity=60)
    drawImage(app.sad2, app.width/2 - 200, app.height/2 + 50, width=app.mood0w, height=app.mood0w, align='center')
    drawImage(app.sad1, app.width/2 - 100, app.height/2 + 50, width=app.mood1w, height=app.mood1w, align='center')
    drawImage(app.middle, app.width/2, app.height/2 + 50, width=app.mood2w, height=app.mood2w, align='center')
    drawImage(app.happy1, app.width/2 + 100, app.height/2 + 50, width=app.mood3w, height=app.mood3w, align='center')
    drawImage(app.happy2, app.width/2 + 200, app.height/2 + 50, width=app.mood4w, height=app.mood4w, align='center')

    if app.mood != None and 0 <= app.mood <= 2:
        drawLabel("I'm sorry your day hasn't been going well. Here are some suggestions to make it better!", app.width/2, app.height/2 + 100, align = 'center')

def onMouseMove(app, mouseX, mouseY):
    if app.page == 'mood':
        if app.height/2 + 25 <= mouseY <= app.height/2 + 75:
            if app.width/2-225<= mouseX <= app.width/2-175:
                app.mood0w = 60
            elif app.width/2-125 <= mouseX <= app.width/2-75 :
                app.mood1w = 60
            elif app.width/2-25 <= mouseX <= app.width/2 + 25:
                app.mood2w = 60
            elif app.width/2+75 <= mouseX <= app.width/2 + 125:
                app.mood3w = 60
            elif app.width/2 + 175 <= mouseX <= app.width/2 + 225: 
                app.mood4w = 60
        else:
            app.mood0w = app.mood1w = app.mood2w = app.mood3w = app.mood4w = 50

def drawCalender(app):
    months = {'January': 31, 'February': (28, 29), 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}
    boxWidth = app.width // 7
    daysOfWeek = ['Sunday', 'Monday', '']


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