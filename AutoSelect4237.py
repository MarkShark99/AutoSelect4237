from PySide2 import QtGui, QtCore, QtWidgets
import sys, json
from lib.network import RoboRIOTransmitter
from lib.widgets import AboutWindow
from lib.frames import GameFrame2019, GameFrame2018, GameFrame2017, GameFrame2016

VERSION = 4.0

class GUI(QtWidgets.QMainWindow):                                                
    iconSize = 75
    
    def __init__(self):
        super(GUI, self).__init__()
        self.initUI()

    """
    Method to create the frames, tabs, and 
    """
    def initUI(self):
        self.teamNumber = self.getTeamNumber()
        print("Team number set to " + str(self.teamNumber))
        self.roboRIOIP = "roborio-" + str(self.teamNumber) + "-frc.local"
        
        self.transmitter = RoboRIOTransmitter.RoboRIOTransmitter(self.roboRIOIP)

        #About window
        self.about = AboutWindow.AboutWindow()
        
        '''
        General
        '''
        
        self.DRMLabel = QtWidgets.QLabel("<font size=8>This program was made by Team 4237.<font>")
        self.DRMLabel.setStyleSheet("QLabel { color : red;}")
        
        self.teamNotFoundLabel = QtWidgets.QLabel("An FRC team number could not be found on this computer, make sure the FRC Driver Station is installed")
        self.teamNotFoundLabel.setStyleSheet("QLabel { color : red; }")
                
        #Actions
        self.exitAction = QtWidgets.QAction('&Exit', self)
        self.exitAction.triggered.connect(self.close)
        
        self.sendToRobotAction = QtWidgets.QAction('&Send To Robot', self)
        self.sendToRobotAction.triggered.connect(self.sendToRobot)

        self.openAboutAction = QtWidgets.QAction('&About', self)
        self.openAboutAction.triggered.connect(self.about.show)
        
        #Icons
        self.strongholdIcon = QtGui.QIcon("img/2016/logos/Stronghold.png")
        self.steamworksIcon = QtGui.QIcon("img/2017/logos/Steamworks.png")
        self.powerupIcon = QtGui.QIcon("img/2018/logos/Powerup.png")
        self.deepspaceIcon = QtGui.QIcon("img/2019/logos/DestinationDeepSpace.png")
        self.windowIcon = QtGui.QIcon("img/general/icons/LanceABotIcon.png")
        
        #Tabs and Frames
        self.frame2016 = GameFrame2016.GameFrame2016()
        self.frame2017 = GameFrame2017.GameFrame2017()
        self.frame2018 = GameFrame2018.GameFrame2018()
        self.frame2019 = GameFrame2019.GameFrame2019()

        #Layout
        self.tabs = QtWidgets.QTabWidget()
        self.tabs.addTab(self.frame2019, self.deepspaceIcon, "")
        self.tabs.addTab(self.frame2018, self.powerupIcon, "")
        self.tabs.addTab(self.frame2017, self.steamworksIcon, "")
        self.tabs.addTab(self.frame2016, self.strongholdIcon, "")
        self.tabs.setIconSize(QtCore.QSize(100, 50))
        
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.tabs)
                
        if self.teamNumber == None:
            print("Error verifying team number")
            self.layout.addWidget(self.teamNotFoundLabel)
        
        self.mainFrame = QtWidgets.QFrame()
        self.mainFrame.setLayout(self.layout)
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(self.exitAction)
        
        robotMenu = menuBar.addMenu('&Robot')
        robotMenu.addAction(self.sendToRobotAction)
        
        helpMenu = menuBar.addMenu('&Help')
        helpMenu.addAction(self.openAboutAction)
        
        self.setCentralWidget(self.mainFrame)
        self.setWindowTitle('AutoSelect 4237 - Version ' + str(VERSION))
        self.setWindowIcon(self.windowIcon)
        self.show()
        
    def closeEvent(self, event):
        self.about.close()
        print("Close Event received")
        
    """
    Base method for sending selected autonomous
    """
    def sendToRobot(self):
        if self.tabs.currentIndex() == 0:
            self.sendToRobot2018()
        elif self.tabs.currentIndex() == 1:
            self.sendToRobot2017()
        elif self.tabs.currentIndex() == 2:
            self.sendToRobot2016()
            
    def sendToRobot2016(self):
        pass
            
    def sendToRobot2017(self):
        pass
        
    def sendToRobot2018(self):
        print(self.frame2018.getJsonData())
        self.transmitter.sendMessage(json.dumps(self.frame2018.getJsonData()))

    '''
    Method to get the current team number from the FRC Driver Station
    '''             
    def getTeamNumber(self):
        print("Searching for team number")
        try:
            with open("C:\\Users\\Public\\Documents\\FRC\\FRC DS Data Storage.ini", 'r') as DSFile:
                lines = DSFile.readlines()
                for x in range(0, len(lines)):
                    if "TeamNumber" in lines[x]:
                        split = lines[x].split("= \"")
                        split[1] = split[1].replace("\"", "")
                        teamNumber = (int)(split[1])
                        return teamNumber
        except:
            print("Team number could not be found")
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = GUI()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()