from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(975, 787)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.TeamName = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.TeamName.setFont(font)
        self.TeamName.setObjectName("TeamName")
        self.verticalLayout.addWidget(self.TeamName)
        self.Selection = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Selection.setFont(font)
        self.Selection.setObjectName("Selection")
        self.verticalLayout.addWidget(self.Selection)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.batsman = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.batsman.setFont(font)
        self.batsman.setObjectName("batsman")
        self.horizontalLayout.addWidget(self.batsman)
        self.batsmancount = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.batsmancount.setFont(font)
        self.batsmancount.setObjectName("batsmancount")
        self.horizontalLayout.addWidget(self.batsmancount)
        self.bowlers = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.bowlers.setFont(font)
        self.bowlers.setObjectName("bowlers")
        self.horizontalLayout.addWidget(self.bowlers)
        self.bowlerscount = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bowlerscount.setFont(font)
        self.bowlerscount.setObjectName("bowlerscount")
        self.horizontalLayout.addWidget(self.bowlerscount)
        self.allrounder = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.allrounder.setFont(font)
        self.allrounder.setObjectName("allrounder")
        self.horizontalLayout.addWidget(self.allrounder)
        self.allroundercount = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.allroundercount.setFont(font)
        self.allroundercount.setObjectName("allroundercount")
        self.horizontalLayout.addWidget(self.allroundercount)
        self.wicketkeepers = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.wicketkeepers.setFont(font)
        self.wicketkeepers.setObjectName("wicketkeepers")
        self.horizontalLayout.addWidget(self.wicketkeepers)
        self.wkcount = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.wkcount.setFont(font)
        self.wkcount.setObjectName("wkcount")
        self.horizontalLayout.addWidget(self.wkcount)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ptavail = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.ptavail.setFont(font)
        self.ptavail.setObjectName("ptavail")
        self.horizontalLayout_2.addWidget(self.ptavail)
        self.ptavail_count = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ptavail_count.setFont(font)
        self.ptavail_count.setObjectName("ptavail_count")
        self.horizontalLayout_2.addWidget(self.ptavail_count)
        self.ptused = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.ptused.setFont(font)
        self.ptused.setObjectName("ptused")
        self.horizontalLayout_2.addWidget(self.ptused)
        self.ptused_count = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ptused_count.setFont(font)
        self.ptused_count.setObjectName("ptused_count")
        self.horizontalLayout_2.addWidget(self.ptused_count)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_3.setContentsMargins(0, 20, -1, 20)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Batsman_2 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Batsman_2.setFont(font)
        self.Batsman_2.setTabletTracking(False)
        self.Batsman_2.setAcceptDrops(False)
        self.Batsman_2.setToolTipDuration(20)
        self.Batsman_2.setStyleSheet("Batmans")
        self.Batsman_2.setObjectName("Batsman_2")
        self.horizontalLayout_3.addWidget(self.Batsman_2)
        self.Wk_2 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Wk_2.setFont(font)
        self.Wk_2.setObjectName("Wk_2")
        self.horizontalLayout_3.addWidget(self.Wk_2)
        self.Allrounder_2 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Allrounder_2.setFont(font)
        self.Allrounder_2.setChecked(False)
        self.Allrounder_2.setObjectName("Allrounder_2")
        self.horizontalLayout_3.addWidget(self.Allrounder_2)
        self.Bowlers_2 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Bowlers_2.setFont(font)
        self.Bowlers_2.setObjectName("Bowlers_2")
        self.horizontalLayout_3.addWidget(self.Bowlers_2)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setMinimumSize(QtCore.QSize(472, 501))
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_4.addWidget(self.listWidget)
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setMinimumSize(QtCore.QSize(472, 501))
        self.listWidget_2.setObjectName("listWidget_2")
        self.horizontalLayout_4.addWidget(self.listWidget_2)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 975, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuManage_Team = QtWidgets.QMenu(self.menubar)
        self.menuManage_Team.setObjectName("menuManage_Team")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Team = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.actionNew_Team.setFont(font)
        self.actionNew_Team.setObjectName("actionNew_Team")
        self.actionOpen_Team = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.actionOpen_Team.setFont(font)
        self.actionOpen_Team.setObjectName("actionOpen_Team")
        self.actionSave_Team_2 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.actionSave_Team_2.setFont(font)
        self.actionSave_Team_2.setObjectName("actionSave_Team_2")
        self.actionEvaluate_Score = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.actionEvaluate_Score.setFont(font)
        self.actionEvaluate_Score.setObjectName("actionEvaluate_Score")
        self.menuManage_Team.addAction(self.actionNew_Team)
        self.menuManage_Team.addSeparator()
        self.menuManage_Team.addAction(self.actionOpen_Team)
        self.menuManage_Team.addSeparator()
        self.menuManage_Team.addAction(self.actionSave_Team_2)
        self.menuManage_Team.addSeparator()
        self.menuManage_Team.addAction(self.actionEvaluate_Score)
        self.menubar.addAction(self.menuManage_Team.menuAction())

        #calling the functions removel1 and removel2
        self.listWidget.itemDoubleClicked.connect(self.removel1)
        self.listWidget_2.itemDoubleClicked.connect(self.removel2)

        #calling category function
        self.Batsman_2.toggled.connect(self.category)
        self.Bowlers_2.toggled.connect(self.category)
        self.Allrounder_2.toggled.connect(self.category)
        self.Wk_2.toggled.connect(self.category) 

        #calling the functions close and choices
        self.menuManage_Team.triggered[QtWidgets.QAction].connect(self.choices)
        self.pushButton.clicked.connect(self.close)

        #initializing the default values of no. of players
        self.bat=0
        self.bwl=0
        self.ar=0
        self.wk=0
        self.avl=1000
        self.used=0

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Selection.setText(_translate("MainWindow", "Your Selections:"))
        self.batsman.setText(_translate("MainWindow", " Batsman (Bat)"))
        self.batsmancount.setText(_translate("MainWindow", "##"))
        self.bowlers.setText(_translate("MainWindow", " Bowlers (Bowl)"))
        self.bowlerscount.setText(_translate("MainWindow", "##"))
        self.allrounder.setText(_translate("MainWindow", "    All-Rounders (All)"))
        self.allroundercount.setText(_translate("MainWindow", "##"))
        self.wicketkeepers.setText(_translate("MainWindow", " Wicket-Keepers(WK)"))
        self.wkcount.setText(_translate("MainWindow", "##"))
        self.ptavail.setText(_translate("MainWindow", " Points Available:"))
        self.ptavail_count.setText(_translate("MainWindow", "##"))
        self.ptused.setText(_translate("MainWindow", " Points Used:"))
        self.ptused_count.setText(_translate("MainWindow", "##"))
        self.TeamName.setText(_translate("MainWindow", "No Team Selected"))
        self.Batsman_2.setText(_translate("MainWindow", "Batsman"))
        self.Wk_2.setText(_translate("MainWindow", "WicketKeeper"))
        self.Allrounder_2.setText(_translate("MainWindow", "All-Rounder"))
        self.Bowlers_2.setText(_translate("MainWindow", "Bowlers"))
        self.pushButton.setText(_translate("MainWindow", "Exit Game"))
        self.menuManage_Team.setTitle(_translate("MainWindow", "Manage Team"))
        self.actionNew_Team.setText(_translate("MainWindow", "New Team"))
        self.actionOpen_Team.setText(_translate("MainWindow", "Open Team"))
        self.actionSave_Team_2.setText(_translate("MainWindow", "Save Team"))
        self.actionEvaluate_Score.setText(_translate("MainWindow", "Evaluate Score"))


    def close(self): #function to exit the application
        import sys
        self.showdlg("We hope you enjoyed the Game!!")
        sys.exit()

    def choices(self,action):  #The menu with options creating and saving a new team, opening and updating an existing team and evaluating score
        txt=(action.text())
    
        if txt=='New Team': #the choice to create new team

            #at first when a new team is created the no. of players selected are set zero as no players are selected from 'listWidget1'
            #also 'listWidget1' and 'listWidget2' are cleared and 'available points' is set 1000 while 'points used' is still 0 
            self.bat=0
            self.bwl=0
            self.ar=0
            self.wk=0
            self.avl=1000
            self.used=0
            self.listWidget.clear()
            self.listWidget_2.clear()
            text, done=QtWidgets.QInputDialog.getText(MainWindow, "Team", "Enter team name:")
            if done:
                self.TeamName.setText(str(text))
                
            self.display()

        if txt=='Save Team': #the choice to save a new team and update an existing team
            count=self.listWidget_2.count()
            selected=""
            #after initialising 'selected' variable all the selected players present in 'listWidget_2' are saved to the database this done in the code below
            for i in range(count):
                selected+=self.listWidget_2.item(i).text() #at first all the players from 'listWidget_2' are added to 'selected' variable one by one which followed by a ","
                if i<(count-1):
                    selected+=","
                    
            self.save(self.TeamName.text(),selected,self.used) #finally save function is called which contains team name, the selected player's names as arguments

        if txt=='Open Team': #the choice to open an existing team

            #actually at first when this menu option is selected a dialog box appears with a combox box which contains names of team saved in the database
            #as well as no. of players for all the categories are set 0 as well as 'points available' and 'points used' are set 1000 and 0, respectively as for now no team is selected
            self.bat=0
            self.bwl=0
            self.ar=0
            self.wk=0
            self.avl=1000
            self.used=0
            #along with no. of players, 'points available' and 'points used', 'listWidget' and 'listWidget_2' are cleared 
            self.listWidget.clear()
            self.listWidget_2.clear()
            self.display() 
            self.open() #after that the open function is called which will display no. of selected players, points available and used, players in listWidget and listWidget_2 as per the data saved in the 'teams' database when a team is selected..

        if txt=='Evaluate Score': #the choice to evaluate a team's score. this is done by opening Python file 'evaluate.py'
            from evaluate import Ui_Dialog
            Dialog = QtWidgets.QDialog()
            ui = Ui_Dialog()
            ui.setupUi(Dialog)
            ret=Dialog.exec()

    def display(self): #this function is used to show no. of batsman(self.bat), bowlers(self.bwl), allrounders(self.ar) and wicket-keepers(self.wk) selected
        #also displays points available(self.avl) and points used(self.used)
        self.batsmancount.setText(str(self.bat))
        self.bowlerscount.setText(str(self.bwl))
        self.allroundercount.setText(str(self.ar))
        self.wkcount.setText(str(self.wk))
        self.ptavail_count.setText(str(self.avl))
        self.ptused_count.setText(str(self.used))

    def crt(self,ctgr,item): #this function is used to see criteria while selecting no. of players with 'ctgr' and 'item' as arguments
        msg='' #crt function does the logical tasks in the game
        if ctgr=="BAT" and self.bat>=5:msg="Batsmen should not be more than 5"
        if ctgr=="BWL" and self.bwl>=5:msg="bowlers should not be more than 5"
        if ctgr=="AR" and self.ar>=3:msg="Allrounders should not be more than 3"
        if ctgr=="WK" and self.wk>=1:msg="Wicketkeepers should not be more than 1"
        if msg!='':
            self.showdlg(msg)
            return False
        
        if self.avl<=0: #this condition is used to display a dialog box with message 'No Points left' when points available(self.avl) is less than or equal to 0
            msg="No points left"
            self.showdlg(msg)
            return False
        
        #these conditions means:
        #when a player with category 'BAT' is selected then no. of batsman(self.bat) will increase by 1
        #similar is the case for no. of bowlers(self.bwl), all-rounders(self.ar), and wicket-keepers(self.wk)
        if ctgr=="BAT":self.bat+=1 
        if ctgr=="BWL":self.bwl+=1
        if ctgr=="AR":self.ar+=1
        if ctgr=="WK":self.wk+=1

        
        sql="SELECT value from stats where player='"+item.text()+"'" #sql query to get the value of the selected player
        cur=conn.execute(sql)
        row=cur.fetchone()
        if self.avl < int(row[0]): #this condition is used when the value of a player selected, int(row[0]), is more than points available(self.avl)
            msg="No more player possible" #this condition is followed by displaying a dialog box with message 'No more player possible'
            #the task will not end here, beacause though the player will not be selected the no. of players will still change
            #so to avoid the no. of players to change, we need to decrease the the no. of players by 1
            if ctgr=="BAT":self.bat-=1
            if ctgr=="BWL":self.bwl-=1
            if ctgr=="AR":self.ar-=1
            if ctgr=="WK":self.wk-=1
            self.showdlg(msg)
            return False

        else: #if evrything goes well after selecting the player from 'listWidget', points available will decrease by thevalue of the selected player
            #and points will increase by the value of the selected player
            self.avl-=int(row[0])
            self.used+=int(row[0])
            return True
        
    
    def removel1(self,item):   #this function is used to add a player(item) of particular category item from listWiget(available players) to listWidget_2(selected players)
        
        ctgr='' #first, the ctgr is just initialized
        #after that, if the radio button for batsman(self.Batsman_2) is checked them ctgr is set 'BAT'
        #similarly it is same for bowlers(self.Bowlers_2), all-rounders(self.Allrounder_2) and wicket-keepers(self.Wk_2) where ctgr is set 'BWL', 'AR', and 'WK', respectively
        if self.Batsman_2.isChecked()==True:ctgr='BAT'
        if self.Bowlers_2.isChecked()==True:ctgr='BWL'
        if self.Allrounder_2.isChecked()==True:ctgr='AR'
        if self.Wk_2.isChecked()==True:ctgr='WK'
        ret=self.crt(ctgr,item) #now the crt function is called with ctgr and item as arguments
        
        if ret==True: #if everything goes right after calling the crt function the player(item) is added to 'listWidget_2' and removed from 'listWidget'
            self.listWidget.takeItem(self.listWidget.row(item))
            
            self.listWidget_2.addItem(item.text())
            self.display() #after that display function is called..

    def category(self):   #this function is used to check which category of player is selected 
        ctgr=''
        #first, the ctgr is just initialized
        #after that, if the radio button for batsman(self.Batsman_2) is checked them ctgr is set 'BAT'
        #similarly it is same for bowlers(self.Bowlers_2), all-rounders(self.Allrounder_2) and wicket-keepers(self.Wk_2) where ctgr is set 'BWL', 'AR', and 'WK', respectively
        if self.Batsman_2.isChecked()==True:ctgr='BAT'
        if self.Bowlers_2.isChecked()==True:ctgr='BWL'
        if self.Allrounder_2.isChecked()==True:ctgr='AR'
        if self.Wk_2.isChecked()==True:ctgr='WK'
       	
        self.fillIt(ctgr) #after that the fillIt function is called with 'ctgr' as its argument

    def removel2(self,item): #this function is used to add a particular player(item) from listWiget_2(selected players) to listWidget(available players)

        #at first the item is removed from listWidget_2 
        self.listWidget_2.takeItem(self.listWidget_2.row(item))

        #secondly, the player which is removed from list_Widget2 is searched in database
        cursor = conn.execute("SELECT player,value, ctg from stats where player='"+item.text()+"'") #this is the query to get the name, catgegory(ctg), and value of the player
        row=cursor.fetchone()
        #after that, points available is increased by the value of the removed player
        #as well as, points used is decreased by the value of the removed player
        self.avl=self.avl+int(row[1])
        self.used=self.used-int(row[1])
        ctgr=row[2]
        #the conditions below, are used to add the removed player back to available players list(listWidget)
        #if the category(ctgr) of the removed player is "BAT" then  no. of batsman(self.bat) is reduced by 1
        #similar is the case for all other categories
        if ctgr=="BAT":
            self.bat-=1
            if self.Batsman_2.isChecked()==True:self.listWidget.addItem(item.text())
        if ctgr=="BWL":
            self.bwl-=1
            if self.Bowlers_2.isChecked()==True:self.listWidget.addItem(item.text())
        if ctgr=="AR":
            self.ar-=1
            if self.Allrounder_2.isChecked()==True:self.listWidget.addItem(item.text())
        if ctgr=="WK":
            self.wk-=1
            if self.Wk_2.isChecked()==True:self.listWidget.addItem(item.text())
        self.display() #finally the display function is called

    def fillIt(self,ctgr): #this function is used to display players name in both the lists based on various logical operations where 'ctgr' is its arugment
        if self.TeamName.text()=='No Team Selected': #if team name is not entered, then at first it should be entered
            self.showdlg("Please Enter the Team Name to continue!!!")
            return
        
        self.listWidget.clear() #intially the available players list(listWidget) is cleared
        sql="SELECT player from stats where ctg='"+ctgr+"';" #this query is used to display the player name(player) from 'stats' table where category(ctg) is 'ctgr'
        cur=conn.execute(sql)
        #after that both the lists are filled as per the query
        for row in cur:
            selected=[]
            for i in range(self.listWidget_2.count()):
                selected.append(self.listWidget_2.item(i).text())
            if row[0] not in selected:self.listWidget.addItem(row[0])

    def open(self): #the main function of the Open Team to open an existing team
        
       
        sql="select name from teams;" #sql query to get the name of all the teams
        cur=conn.execute(sql)
        teams=[]
        for row in cur:
            teams.append(row[0])
        
        team, ok=QtWidgets.QInputDialog.getItem(MainWindow,"Team Window","Choose Your Team",teams,0,False) #a Dialog window with a combo box is displayed, where all the teams present in the database can be viewed by selecting the item from the combo box
        if ok and team: #if the team is selected, its name will be displayed
            self.TeamName.setText(team)
        
        sql1="SELECT players,value from teams where name='"+team+"';" #this query is used to get value and name(player) of the team selected
        cur=conn.execute(sql1)
        row=cur.fetchone()
        selected=row[0].split(',')
        self.listWidget_2.addItems(selected) #after that the players are added to selected players list(listWidget_2) one by one
        self.used=row[1] #points used(self.used) is equal to value of the team selected(row[1])
        
        self.avl=1000-row[1]  #points available(self.avl) is equal to 1000 - value of the team selected(row[1])
        count=self.listWidget_2.count()
        for i in range(count): #after that no. of players of each and every category available in the selected team are displayed
            ply=self.listWidget_2.item(i).text()
            sql="select ctg from stats where player='"+ply+"';"
            
            cur=conn.execute(sql)
            
            row=cur.fetchone()
            ctgr=row[0]
            if ctgr=="BAT":self.bat+=1
            if ctgr=="BWL":self.bwl+=1
            if ctgr=="AR":self.ar+=1
            if ctgr=="WK":self.wk+=1  

        self.display() #to display everything necessary, display function is used

    def save(self,nm,ply,val):  #the main function of the Save Team to save a new team or update an existing team where name of team(nm), players in the team(ply), and value(val) of the team are its arguments
        
        if self.bat+self.bwl+self.ar+self.wk>11: #A message as 'No. of players are exceeding!!' is displayed when the summation of players of all the categories is greater than 11 
            self.showdlg("No. of players are exceeding!!")
            return

        if self.bat+self.bwl+self.ar+self.wk<11: #A message as 'No. of players are exceeding!!' is displayed when the summation of players of all the categories is less than 11 
            self.showdlg("No. of players selected are insufficient!!")
            return
        
        sql2="SELECT COUNT(name) FROM teams where name='"+nm+"';" #this query is used to calculate no. of teams avaliable in the database with the name(nm) this can either be 0 or 1
                                                                  #0 is when no team exist 

        num=conn.execute(sql2)
        r=num.fetchone()
        count=r[0]
        if count==0:
            sql="INSERT INTO teams (name,players,value) VALUES ('"+nm+"','"+ply+"','"+str(val)+"');" #sql query to save a new team

        if nm=='No Team Selected': #A special case when a player tries to save a team without mentioning team name
            team_name, enter=QtWidgets.QInputDialog.getText(MainWindow, "Team", "Please enter your team name:")
            if enter:
                self.TeamName.setText(str(team_name))
                sql="INSERT INTO teams (name,players,value) VALUES ('"+str(team_name)+"','"+ply+"','"+str(val)+"');"

        if count>0:
            sql="UPDATE teams SET players='"+ply+"', value='"+str(val)+"' where name='"+nm+"';" #sql query to update an existing team
           
        try: #if all goes correct the indent inside try: will be executed
            cur=conn.execute(sql)
            self.showdlg("Team Saved Succesfully...\nUse Evaluate Score to see how much points your team scored")
            conn.commit()
        except: #else indent inside except: will be executed
            self.showdlg("Error Occured :(")
            conn.rollback()


    def showdlg(self,msg): #function to display dialog box while doing any type of operation
        Dialog=QtWidgets.QMessageBox()
        Dialog.setText(msg)
        Dialog.setWindowTitle("GAME Window")
        ret=Dialog.exec()

if __name__ == "__main__":
    import sqlite3
    conn = sqlite3.connect('players.db')
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
