# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'evaluate.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(447, 481)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.points = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.points.setFont(font)
        self.points.setObjectName("points")
        self.gridLayout.addWidget(self.points, 3, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 1)
        self.matches = QtWidgets.QComboBox(Dialog)
        self.matches.setObjectName("matches")
        self.matches.addItem("")
        self.matches.addItem("")
        self.matches.addItem("")
        self.matches.addItem("")
        self.matches.addItem("")
        self.gridLayout.addWidget(self.matches, 0, 1, 1, 2)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 0, 1, 3)
        self.calculate = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.calculate.setFont(font)
        self.calculate.setObjectName("calculate")
        #calling of calc function
        self.calculate.clicked.connect(self.calc)
        self.gridLayout.addWidget(self.calculate, 6, 0, 1, 3)
        self.teams = QtWidgets.QComboBox(Dialog)
        self.teams.setObjectName("teams")
        #the name of all teams created/updated will be available in the combo box
        #these names are stored in the 'players' database which can also be retrieved
        import sqlite3 
        conn = sqlite3.connect('players.db')
        sql="select name from teams;"
        cur=conn.execute(sql)
        teams=[]
        for row in cur:
            self.teams.addItem(row[0])        
        conn.close()
        #after this the the connection to database is closed
        self.gridLayout.addWidget(self.teams, 0, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 5, 0, 1, 3)
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 2)
        self.list1 = QtWidgets.QListWidget(Dialog)
        self.list1.setMinimumSize(QtCore.QSize(209, 305))
        self.list1.setObjectName("list1")
        self.gridLayout.addWidget(self.list1, 4, 0, 1, 1)
        self.list2 = QtWidgets.QListWidget(Dialog)
        self.list2.setMinimumSize(QtCore.QSize(209, 305))
        self.list2.setObjectName("list2")
        self.gridLayout.addWidget(self.list2, 4, 1, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def calc(self): #this function is used to calculate and display the score
        import sqlite3
        conn = sqlite3.connect('players.db') #step 1: the database is connected
        team=self.teams.currentText() #this means team = the name of the team selected from the combo box
        self.list1.clear()  #this means the listWidget 'list1' should be clear when any team is selected and the 'calculate' pushbutton is not clicked
        sql1="select players, value from teams where name='"+team+"';" #sql query to get the selected team's players and value
        cur=conn.execute(sql1)
        row=cur.fetchone()
        selected=row[0].split(',')
        self.list1.addItems(selected)#all the players of the team are added to listWidget 'list1'
        teamttl=0
        self.list2.clear() #the 'list2' listWidget is left clear as calculate 'pushbutton' is not clicked
        for i in range(self.list1.count()):
            ttl, batscore, bowlscore, fieldscore=0,0,0,0
            nm=self.list1.item(i).text()
            cursor=conn.execute("select * from match where name='"+nm+"';")
            row=cursor.fetchone()
            #the rules mentioned for calculating batsman score is written in code to calculate batsman score
            batscore=int(row[1]/2)
            if batscore>=50: batscore+=5 
            if batscore>=100: batscore+=10
            if row[1]>0:
                sr=row[1]/row[2]
                if sr>=80 and sr<100: batscore+=2
                if sr>=100:batscore+=4
            batscore=batscore+row[3]
            batscore=batscore+2*row[4]
            #the rules mentioned for calculating bowlers score is written in code to calculate bowlers score
            bowlscore=row[8]*10
            if row[8]>=3: bowlscore=bowlscore+5
            if row[8]>=5: bowlscore=bowlscore=bowlscore+10
            if row[7]>0:
                er=6*row[7]/row[5]
                if er<=2: bowlscore=bowlscore+10
                if er>2 and er<=3.5: bowlscore=bowlscore+7
                if er>3.5 and er<=4.5: bowlscore=bowlscore+4
            #the remaining code is used to calculate fielding score of each and every player based on rules mentioned in problem statement 
            fieldscore=(row[9]+row[10]+row[11])*10            
            ttl=batscore+bowlscore+fieldscore #ttl = overall score of a particular player after calculating batsman, bowlers and fielding score
            self.list2.addItem(str(ttl)) #the ttl score is now displayed in 'list2' listWidget
            teamttl=teamttl+ttl #this statement is for calculating team's score 'teamtt1' by adding 'ttl' score of all the players in the team

        self.points.setText(str(teamttl)) #the team's score 'teamtt1' is finally displayed in 'points' label

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.points.setText(_translate("Dialog", "#"))
        self.label_3.setText(_translate("Dialog", "Players"))
        self.label_4.setText(_translate("Dialog", "Points"))
        self.matches.setItemText(0, _translate("Dialog", "match1"))
        self.matches.setItemText(1, _translate("Dialog", "match2"))
        self.matches.setItemText(2, _translate("Dialog", "match3"))
        self.matches.setItemText(3, _translate("Dialog", "match4"))
        self.matches.setItemText(4, _translate("Dialog", "match5"))
        self.label.setText(_translate("Dialog", "Teams"))
        self.calculate.setText(_translate("Dialog", "Calculate"))
        self.label_2.setText(_translate("Dialog", "Matches"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
