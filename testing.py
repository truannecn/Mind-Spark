from cmu_graphics import *
import string
import calendar
from datetime import date

######
# ON APP START
######
def onAppStart(app):
    # app.users = []

    # #login page app variables
    # app.username = ''
    # app.password = ''
    # app.currentUser = None

    #calendar page variables
    app.currMonth = 11
    app.currentDay = 16
    app.currYear = 2024
    app.displayMonth = app.currMonth
    app.displayYear = app.currYear
    app.leftX, app.leftY = 433, 200
    app.rightX, app.rightY = 1079, 200
    app.bumperRadius = 50
    app.selectedDay = None

    #user variables
    app.calender = UserCalender()

    #mood app variables
    app.mood = None
    app.mood0w = app.mood1w = app.mood2w = app.mood3w = app.mood4w = 50

    #textBox app variables    
    app.name = 'Truanne'
    app.inBox = False
    app.entry = ''
    app.textBoxLeft = 50
    app.textBoxTop = 150
    app.entryList = []
    app.showMoods = False
    app.showSubmit = False
    app.illumSubmit = False
    app.cover = False
    app.popup = False
    app.popupButton1 = False
    app.popupButton2 = False
    app.popupButton3 = False

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
    
    #landing variables
    app.buttonRect = False

    #quest variables
    app.quests = ['Take a 10 minute walk outside', 'Meditate for 5 minutes', 'Listen to your favorite song!', 'Give someone a hug', 'Drink water!', 'Practice daily affirmations', 'Complete a 10 minute yoga session', 'Treat yourself to your favorite food', 'Tell someone you love them', 'Take a relaxing bath']

######
# LANDING PAGE
######
def landingPage_redrawAll(app):
    drawImage('converted_image.png', 0, 0)
    imageWidth, imageHeight = getImageSize('mindSpark.png')
    drawImage('mindSpark.png', app.width/2 - 375 , app.height/2+100, width = imageWidth/2, height = imageHeight/2, align='center')
    drawLabel("Welcome! We are glad you are here. How do you feel today?", app.width/2 + 350, app.height/2 + 100, font='monospace', size=21, italic=True)
    drawRect((app.width/2+350), (app.height/2+175), 225, 50, align='center', fill = None, border='black')
    if app.buttonRect:
        drawRect((app.width/2+350), (app.height/2+175), 225, 50, align='center', fill = 'lightGreen', opacity=70)
    drawLabel("Begin Journaling", (app.width/2+350), (app.height/2+175), align='center', font='monospace', size=18)
    
def landingPage_onMousePress(app, mouseX, mouseY):
    if (app.width/2+237.5 <= mouseX <= app.width/2+462.5) and (app.height/2+150<= mouseY <= app.height/2+200):
        setActiveScreen('journalEntry')
def landingPage_onMouseMove(app, mouseX, mouseY):
    if (app.width/2+237.5 <= mouseX <= app.width/2+462.5) and (app.height/2+150<= mouseY <= app.height/2+200):
        app.buttonRect = True
    else:
        app.buttonRect = False

######
# JOURNAL ENTRY
######
def journalEntry_redrawAll(app):
    drawImage('jounralBackground.jpeg', 0, 0)
    makeTextBox(app)
    updateTextBox(app)
    if app.showMoods:
        drawMoods(app)
    if app.showSubmit:
        submitButton(app)
    makePopUp(app)
    
def journalEntry_onMousePress(app, mouseX, mouseY):
    if 50<=mouseX<=app.width-50 and 50<=mouseY<=app.height/3:
            app.inBox = True

    if app.showMoods:
        if app.height/2 + 75 <= mouseY <= app.height/2 + 125:
            if app.width/2-225<= mouseX <= app.width/2-175:
                    app.showSubmit = True
                    app.mood = 0
            elif app.width/2-125 <= mouseX <= app.width/2-75 :
                    app.mood = 1
                    app.showSubmit = True
            elif app.width/2-25 <= mouseX <= app.width/2 + 25:
                    app.mood = 2
                    app.showSubmit = True
            elif app.width/2+75 <= mouseX <= app.width/2 + 125:
                    app.mood = 3
                    app.showSubmit = True
            elif app.width/2 + 175 <= mouseX <= app.width/2 + 225: 
                    app.mood = 4
                    app.showSubmit = True
    
    if app.illumSubmit:
        if (app.width/2+262.5 <= mouseX <= app.width/2+437.5) and (app.height/2+175<=mouseY<=app.height/2+225):
            app.cover = True
            app.popup = True

    if app.popupButton2:
        setActiveScreen('drawCalendar')

            
            
def journalEntry_onKeyPress(app, key):
    if app.inBox:
        app.showMoods = True
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
            
def makeTextBox(app):
    drawLabel(date.today(), app.textBoxLeft, app.textBoxTop-22, size=38, align='left', font='monospace', bold=True)
    # drawLabel(f'||  Hi, {app.name}', app.textBoxLeft + 270, app.textBoxTop-22, size=38, align='left', font='monospace', bold=True)
    drawRect(app.textBoxLeft, app.textBoxTop, app.width-100, app.height/3, border='black', fill='white', opacity=38)
    if len(app.entry) == 0 and len(app.entryList) == 0:
        drawLabel("How are you feeling today?", app.textBoxLeft+7, app.textBoxTop + 15, align='left', fill = 'gray', italic = True, size=20, font='monospace')

def updateTextBox(app):
    currentLine = app.textBoxTop 
    for i in range(len(app.entryList)):
        currentLine = (app.textBoxTop+10) + (15*i)
        drawLabel(app.entryList[i], 57, currentLine, align='left', fill='black', size = 20, font='monospace')

    drawLabel(app.entry, 57, currentLine + 15, align='left', fill='black',size=20, font='monospace')

def journalEntry_onMouseMove(app, mouseX, mouseY):
    if app.height/2 + 75 <= mouseY <= app.height/2 + 125:
        if app.width/2-225<= mouseX <= app.width/2-175:
            app.mood0w = 60
            app.mood1w = app.mood2w = app.mood3w = app.mood4w = 50
        if app.width/2-125 <= mouseX <= app.width/2-75 :
            app.mood1w = 60
            app.mood0w = app.mood2w = app.mood3w = app.mood4w = 50
        if app.width/2-25 <= mouseX <= app.width/2 + 25:
            app.mood2w = 60
            app.mood1w = app.mood0w = app.mood3w = app.mood4w = 50
        if app.width/2+75 <= mouseX <= app.width/2 + 125:
            app.mood3w = 60
            app.mood1w = app.mood2w = app.mood0w = app.mood4w = 50
        if app.width/2 + 175 <= mouseX <= app.width/2 + 225: 
            app.mood4w = 60
            app.mood1w = app.mood2w = app.mood3w = app.mood0w = 50
    else:
        app.mood0w = app.mood1w = app.mood2w = app.mood3w = app.mood4w = 50
    if app.showSubmit:
        if (app.width/2+262.5 <= mouseX <= app.width/2+437.5) and (app.height/2+175<=mouseY<=app.height/2+225):
            app.illumSubmit = True
        else:
            app.illumSubmit = False

    if app.cover == True and app.popup == True:
        if app.height/2+30 <= mouseY <= app.height/2+70:
            if app.width/2-260<=mouseX<=app.width/2-120:
                app.popupButton1 = True
                app.popupButton2 = app.popupButton3 = False
            elif app.width/2-70<=mouseX<=app.width/2+70:
                app.popupButton2 = True
                app.popupButton1 = app.popupButton3 = False
            elif app.width/2+120<=mouseX<=app.width/2+260:
                app.popupButton3 = True
                app.popupButton2 = app.popupButton1 = False

        else:
            app.popupButton1 = app.popupButton2 = app.popupButton3 = False

def drawMoods(app):
    drawLabel("What was your overall mood today?", app.width/2, app.height/2 + 50, align='center', size=20, bold=True, font='monospace')
    drawCircle(app.width/2-200, app.height/2 + 100, app.mood0w/2, fill='blue', opacity=60)
    drawCircle(app.width/2-100, app.height/2 + 100, app.mood1w/2, fill='lightBlue', opacity=60)
    drawCircle(app.width/2, app.height/2 + 100, app.mood2w/2, fill='yellow', opacity=60)
    drawCircle(app.width/2+100, app.height/2 + 100, app.mood3w/2, fill='lightGreen', opacity=60)
    drawCircle(app.width/2+200, app.height/2 + 100, app.mood4w/2, fill='green', opacity=60)
    drawImage(app.sad2, app.width/2 - 200, app.height/2 + 100, width=app.mood0w, height=app.mood0w, align='center')
    drawImage(app.sad1, app.width/2 - 100, app.height/2 + 100, width=app.mood1w, height=app.mood1w, align='center')
    drawImage(app.middle, app.width/2, app.height/2 + 100, width=app.mood2w, height=app.mood2w, align='center')
    drawImage(app.happy1, app.width/2 + 100, app.height/2 + 100, width=app.mood3w, height=app.mood3w, align='center')
    drawImage(app.happy2, app.width/2 + 200, app.height/2 + 100, width=app.mood4w, height=app.mood4w, align='center')

    if app.mood != None and 0 <= app.mood <= 2:
        drawLabel("We're sorry your day hasn't been going well. We hope it improves!", app.width/2, app.height/2 + 150, align = 'center', font='monospace', size=15)
    
def submitButton(app):
    drawRect((app.width/2+350), (app.height/2+200), 175, 50, align='center', fill = None, border='black')
    if app.illumSubmit:
        drawRect((app.width/2+350), (app.height/2+200), 175, 50, align='center', fill = 'lightGreen', opacity=70)
    drawLabel("Save", (app.width/2+350), (app.height/2+200), align='center', font='monospace', size=18)

def makePopUp(app):
    if app.cover == True and app.popup == True:
        drawRect(0, 0, app.width, app.height, fill ='gray', opacity = 85)
        drawRect(app.width/2, app.height/2, 600, 400, fill='white', align='center')
        drawLabel("Thank you for sharing!", app.width/2, app.height/2-110, font='monospace', size=25, bold=True)
        drawLabel("We hope to see you again tommorrow.", app.width/2, app.height/2-80, font='monospace', size=25, bold=True)
        drawRect((app.width/2), (app.height/2+50), 140, 40, align='center', fill = None, border='black')
        drawRect((app.width/2+190), (app.height/2+50), 140, 40, align='center', fill = None, border='black')
        drawRect((app.width/2-190), (app.height/2+50), 140, 40, align='center', fill = None, border='black')
        drawLabel("Home", app.width/2-190, app.height/2+50, align='center', font='monospace', size=15)
        drawLabel("Analytics", app.width/2, app.height/2+50, align='center', font='monospace', size=15)
        drawLabel("Quests", app.width/2+190, app.height/2+50, align='center', font='monospace', size=15)
        if app.popupButton1:
            drawRect((app.width/2-190), (app.height/2+50), 140, 40, align='center', fill = 'lightGreen', opacity=70)
        elif app.popupButton2:
            drawRect((app.width/2), (app.height/2+50), 140, 40, align='center', fill = 'lightGreen', opacity=70)
        elif app.popupButton3:
            drawRect((app.width/2+190), (app.height/2+50), 140, 40, align='center', fill = 'lightGreen', opacity=70)
        

######
# CALENDAR VIEW
######

def drawCalendar_redrawAll(app):
    drawCalendar(app)        

def drawCalendar(app):
    #initializes relevant variables
    months = ['fill', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    boxWidth = app.width // 14
    daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    _, lastDay = calendar.monthrange(app.displayYear, app.displayMonth)
    lastDayOfMonth = calendar.weekday(app.displayYear, app.displayMonth, lastDay)
    currWeek = 0
    currDay = lastDay
    currDayOfWeek = lastDayOfMonth
    
    #adjusts size of vertical boxes
    if app.displayMonth == 2 and app.displayYear % 4 != 0 and lastDayOfMonth == 6:
        rows = 4
        boxHeight = (5 / rows) * boxWidth
    elif lastDayOfMonth + 29 < lastDay:
        rows = 6
        boxHeight = (5 / rows) * boxWidth
    else:
        rows = 5
        boxHeight = boxWidth

    #draws all the boxes  
    for row in range(rows):
        for col in range(7):
            left, top = app.width // 4 + boxWidth * col, app.height - boxHeight * (row + 1) - 100
            drawRect(left, top, boxWidth, boxHeight, fill = None, border = 'black')
                
    #draws all the day labels
    for day in range(lastDay):
        left, top = app.width // 4 + currDayOfWeek * boxWidth, app.height - (currWeek + 1) * boxHeight - 100
        drawRect(left, top, boxWidth, boxHeight, fill=None, border='black')
        drawLabel(str(currDay), left + 8, top + 8, align = 'left-top', size = 18)
        currDay -= 1
        currDayOfWeek = (currDayOfWeek - 1) % 7
        if currDayOfWeek == 6:
            currWeek += 1

    #draws days of the week        
    for i in range(len(daysOfWeek)):
        day = daysOfWeek[i]
        drawLabel(day, app.width // 4 + boxWidth * i + 0.5 * boxWidth, app.height - boxHeight * (row + 1.25) - 100, size = 20)

    #draws month and outside border
    left, top = app.width // 4, app.height - boxHeight * (row + 1) - 100
    drawLabel(months[app.displayMonth] + " " + str(app.displayYear), app.width // 2, 200, size = 70)        
    drawRect(left, top, app.width // 2, boxHeight * (row + 1), fill = None, border = 'black', borderWidth = 4)
    
    #draws bumpers
    drawCircle(app.leftX, app.leftY, app.bumperRadius, opacity = 50)
    drawLabel('<', app.leftX, app.leftY, size = 50)
    drawCircle(app.rightX, app.rightY, app.bumperRadius, opacity = 50)
    drawLabel('>', app.rightX, app.rightY, size = 50)
    
def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def onMousePressCalendar(app, mouseX, mouseY):
    bumpMonth(app, mouseX, mouseY)
    selectDay(app, mouseX, mouseY)

def bumpMonth(app, mouseX, mouseY):
    app.displayMonth -= 1
    if distance(mouseX, mouseY, app.leftX, app.leftY) < 50:
        app.displayMonth -= 1
        if app.displayMonth != app.displayMonth % 12:
            app.displayMonth = app.displayMonth % 12
            app.displayYear -= 1
        app.selectedDay = None
    if distance(mouseX, mouseY, app.rightX, app.rightY) < 50:
        app.displayMonth += 1
        if app.displayMonth != app.displayMonth % 12:
            app.displayMonth = app.displayMonth % 12
            app.displayYear += 1
        app.selectedDay = None
    app.displayMonth += 1

def selectDay(app, mX, mY):
    #initializes relevant variables
    months = ['fill', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    boxWidth = app.width // 14
    daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    _, lastDay = calendar.monthrange(app.displayYear, app.displayMonth)
    lastDayOfMonth = calendar.weekday(app.displayYear, app.displayMonth, lastDay)
    currWeek = 0
    currDay = lastDay
    currDayOfWeek = lastDayOfMonth
    
    #adjusts size of vertical boxes
    if app.displayMonth == 2 and app.displayYear % 4 != 0 and lastDayOfMonth == 6:
        rows = 4
        boxHeight = (5 / rows) * boxWidth
    elif lastDayOfMonth + 29 < lastDay:
        rows = 6
        boxHeight = (5 / rows) * boxWidth
    else:
        rows = 5
        boxHeight = boxWidth

    lRow = rows - 1
    lCol = 6
    left = app.width // 4
    bottom = app.height - 100

    if (left <= mX <= left + (boxWidth * 7)) and (bottom - (boxHeight * rows) <= mY <= bottom):
        nRow = rows - ((bottom - mY) // boxHeight) - 1
        nCol = (mX - L) // boxWidth
        dRow = nRow - lRow
        dCol = nCol - lCol
        app.selectedDay = lastDay + 7 * dRow + 7 * dCol

def quest_redrawAll(app):
    drawLabel("Completing these self care tasks can greatly improve your mood and your overall well-being!", app.width/2, 30, font='monospace', size=30, align='center')
    drawLabel("Check back daily for new tasks!", app.width/2, 50, font='monospace', size=20, align='center')




# class Account():
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#         self.name = None
#         self.calender = UserCalender()

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
    runAppWithScreens(initialScreen='landingPage')

main()