from cmu_graphics import *
import string
import calendar

######
# ON APP START
######
def onAppStart(app):
    app.page = 'landing page'
    app.users = []

    #login page app variables
    app.username = ''
    app.password = ''
    app.currentUser = None

    #calendar page variables
    app.currMonth = 11
    app.currYear = 2024
    app.displayMonth = app.currMonth
    app.displayYear = app.currYear
    app.leftX, app.leftY = 40, 50
    app.rightX, app.rightY = 360, 50
    app.bumperRadius = 50

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
    app.entryList = ["aldkfjadslkfjasklfjlaskjf"]

    app.happy2 = 'smile.png'
    app.happy1 = 'smile (1).png'
    app.middle = 'sceptic.png'
    app.sad1 = 'sceptic (1).png'
    app.sad2 = 'crying.png'

    app.happy2 = 'smile.png'
    app.happy1 = 'smile (1).png'
    app.middle = 'sceptic.png'
    app.sad1 = 'sceptic (1).png'
    app.sad2 = 'crying.png'

    app.wallpaper = 'converted_image.png'



######
# ON KEY PRESS
######
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

#####
# ON MOUSE PRESS
#####
def onMousePress(app, mouseX, mouseY):
    if app.page == 'journal entry':
        if 50<=mouseX<=app.width-50 and 50<=mouseY<=app.height/3:
            app.inBox = True
    elif app.page == 'mood':
        onMousePressMood(app, mouseX, mouseY)
    elif app.page == 'calendar view':
        onMousePressCalendar(app, mouseX, mouseY)

def onMousePressMood(app, mouseX, mouseY):
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

def onMousePressCalendar(app, mouseX, mouseY):
    app.displayMonth -= 1
    if distance(mouseX, mouseY, app.leftX, app.leftY) < 50:
        app.displayMonth -= 1
        if app.displayMonth != app.displayMonth % 12:
            app.displayMonth = app.displayMonth % 12
            app.displayYear -= 1
    if distance(mouseX, mouseY, app.rightX, app.rightY) < 50:
        app.displayMonth += 1
        if app.displayMonth != app.displayMonth % 12:
            app.displayMonth = app.displayMonth % 12
            app.displayYear += 1
    app.displayMonth += 1

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
<<<<<<< Updated upstream
        drawCalender(app)
=======
        drawCalender(app, app.calender)

>>>>>>> Stashed changes
        
def drawLandingPage(app):
    drawImage('converted_image.png', 0, 0)
    

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
    months = ['fill', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    boxWidth = app.width // 7
    daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    _, lastDay = calendar.monthrange(app.displayYear, app.displayMonth)
    lastDayOfMonth = calendar.weekday(app.displayYear, app.displayMonth, lastDay)
    currWeek = 0
    currDay = lastDay
    currDayOfWeek = lastDayOfMonth
    
    if app.displayMonth == 2 and app.displayYear % 4 != 0 and lastDayOfMonth == 6:
        rows = 4
        boxHeight = (5 / 4) * boxWidth
    elif lastDayOfMonth + 29 < lastDay:
        rows = 6
        boxHeight = (5 / 6) * boxWidth
    else:
        rows = 5
        boxHeight = boxWidth
        
    for row in range(rows):
        for col in range(7):
            left, top = 0 + boxWidth * col, 400 - boxHeight * (row + 1)
            drawRect(left, top, boxWidth, boxHeight, fill = None, border = 'black')
                

    for day in range(lastDay):
        left, top = 0 + currDayOfWeek * boxWidth, 400 - (currWeek + 1) * boxHeight
        drawRect(left, top, boxWidth, boxHeight, fill=None, border='black')
        drawLabel(str(currDay), left + 5, top + 5, align = 'left-top', size = 10)
        currDay -= 1
        currDayOfWeek = (currDayOfWeek - 1) % 7
        if currDayOfWeek == 6:
            currWeek += 1
            
    for i in range(len(daysOfWeek)):
        day = daysOfWeek[i]
        drawLabel(day, boxWidth * i + 0.5 * boxWidth, 400 - boxHeight * (row + 1.25), size = 10)
        
    drawLabel(months[app.displayMonth] + " " + str(app.displayYear), app.width // 2, 50, size = 35)        
    drawRect(0, 400 - boxHeight * (row + 1), app.width, boxHeight * (row + 1), fill = None, border = 'black', borderWidth = 2)
    
    drawCircle(40, 50, 20, opacity = 50)
    drawCircle(360, 50, 20, opacity = 50)
    
def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

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