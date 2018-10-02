from PySide2 import QtGui, QtCore, QtWidgets
import lib.widgets.RobotPosition

'''
Frame for the 2016 game settings
'''
class GameFrame2016(QtWidgets.QFrame):
    def __init__(self):
        super(GameFrame2016, self).__init__()
        #Variables
        self.selectedPosition2016 = 6
        self.selectedObstacle2016 = "None"
        self.iconSize = 75                                                   #number used for scaling the images in the comboboxes
        
        #Images
        self.robotPixmap = QtGui.QPixmap("img/2016/icons/RobotIcon.png")
        self.blankPixmap = QtGui.QPixmap("img/2016/icons/TransparentRobotIcon.png")
        self.blankIcon = QtGui.QIcon("img/2016/defenses/BlankIcon.png")
        self.moatIcon = QtGui.QIcon("img/2016/defenses/Moat.png")
        self.rampartsIcon = QtGui.QIcon("img/2016/defenses/Ramparts.png")
        self.rockWallIcon = QtGui.QIcon("img/2016/defenses/RockWall.png")
        self.portcullisIcon = QtGui.QIcon("img/2016/defenses/Portcullis.png")
        self.roughTerrainIcon = QtGui.QIcon("img/2016/defenses/RoughTerrain.png")
        self.chevalDeFriseIcon = QtGui.QIcon("img/2016/defenses/ChevalDeFrise.png")
        self.sallyPortIcon = QtGui.QIcon("img/2016/defenses/SallyPort.png")
        self.drawBridgeIcon = QtGui.QIcon("img/2016/defenses/Drawbridge.png")
        self.lowBarIcon = QtGui.QIcon("img/2016/defenses/LowBar.png");
        self.lowBarPixmap = QtGui.QPixmap("img/2016/defenses/LowBar.png")
                
        #Combo boxes
        self.lowBarLabel = QtWidgets.QLabel("")
        self.lowBarLabel.setPixmap(self.lowBarPixmap.scaledToWidth(100))
        self.obstacle2Box2016 = QtWidgets.QComboBox() #Box 2
        self.obstacle2Box2016.addItem(self.moatIcon, "Moat")
        self.obstacle2Box2016.addItem(self.rampartsIcon, "Ramparts")
        self.obstacle2Box2016.addItem(self.rockWallIcon, "Rock Wall")
        self.obstacle2Box2016.addItem(self.portcullisIcon, "Portcullis")
        self.obstacle2Box2016.addItem(self.roughTerrainIcon, "Rough Terrain")
        self.obstacle2Box2016.addItem(self.chevalDeFriseIcon, "Cheval De Frise")
        self.obstacle2Box2016.addItem(self.sallyPortIcon, "Sally Port")
        self.obstacle2Box2016.addItem(self.drawBridgeIcon, "Drawbridge")
        #self.Obstacle2Box.addItem(self.LowBarIcon, "Low Bar")
        self.obstacle2Box2016.setIconSize(QtCore.QSize(self.iconSize, self.iconSize))
        
        self.obstacle3Box2016 = QtWidgets.QComboBox() #Box 3
        self.obstacle3Box2016.addItem(self.moatIcon, "Moat")
        self.obstacle3Box2016.addItem(self.rampartsIcon, "Ramparts")
        self.obstacle3Box2016.addItem(self.rockWallIcon, "Rock Wall")
        self.obstacle3Box2016.addItem(self.portcullisIcon, "Portcullis")
        self.obstacle3Box2016.addItem(self.roughTerrainIcon, "Rough Terrain")
        self.obstacle3Box2016.addItem(self.chevalDeFriseIcon, "Cheval De Frise")
        self.obstacle3Box2016.addItem(self.sallyPortIcon, "Sally Port")
        self.obstacle3Box2016.addItem(self.drawBridgeIcon, "Drawbridge")
        #self.Obstacle3Box.addItem(self.LowBarIcon, "Low Bar")
        self.obstacle3Box2016.setIconSize(QtCore.QSize(self.iconSize, self.iconSize))
        self.obstacle3Box2016.setCurrentIndex(1)
                
        self.obstacle4Box2016 = QtWidgets.QComboBox() #Box 4
        self.obstacle4Box2016.addItem(self.moatIcon, "Moat")
        self.obstacle4Box2016.addItem(self.rampartsIcon, "Ramparts")
        self.obstacle4Box2016.addItem(self.rockWallIcon, "Rock Wall")
        self.obstacle4Box2016.addItem(self.portcullisIcon, "Portcullis")
        self.obstacle4Box2016.addItem(self.roughTerrainIcon, "Rough Terrain")
        self.obstacle4Box2016.addItem(self.chevalDeFriseIcon, "Cheval De Frise")
        self.obstacle4Box2016.addItem(self.sallyPortIcon, "Sally Port")
        self.obstacle4Box2016.addItem(self.drawBridgeIcon, "Drawbridge")
        #self.Obstacle4Box.addItem(self.LowBarIcon, "Low Bar")
        self.obstacle4Box2016.setIconSize(QtCore.QSize(self.iconSize, self.iconSize))
        self.obstacle4Box2016.setCurrentIndex(3)
        
        self.obstacle5Box2016 = QtWidgets.QComboBox() #Box 5
        self.obstacle5Box2016.addItem(self.moatIcon, "Moat")
        self.obstacle5Box2016.addItem(self.rampartsIcon, "Ramparts")
        self.obstacle5Box2016.addItem(self.rockWallIcon, "Rock Wall")
        self.obstacle5Box2016.addItem(self.portcullisIcon, "Portcullis")
        self.obstacle5Box2016.addItem(self.roughTerrainIcon, "Rough Terrain")
        self.obstacle5Box2016.addItem(self.chevalDeFriseIcon, "Cheval De Frise")
        self.obstacle5Box2016.addItem(self.sallyPortIcon, "Sally Port")
        self.obstacle5Box2016.addItem(self.drawBridgeIcon, "Drawbridge")
        #self.Obstacle5Box.addItem(self.LowBarIcon, "Low Bar")
        self.obstacle5Box2016.setIconSize(QtCore.QSize(self.iconSize, self.iconSize))
        self.obstacle5Box2016.setCurrentIndex(5)
        
        self.noSetPositionLabel = QtWidgets.QLabel("No Set Position")
        self.noSetPositionLabel.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)

        self.positionButtonGroup = QtWidgets.QButtonGroup()
        self.position1Label = lib.widgets.RobotPosition.RobotPosition(self.blankPixmap.scaledToWidth(self.iconSize))
        self.position2Label = lib.widgets.RobotPosition.RobotPosition(self.blankPixmap.scaledToWidth(self.iconSize))
        self.position3Label = lib.widgets.RobotPosition.RobotPosition(self.blankPixmap.scaledToWidth(self.iconSize))
        self.position4Label = lib.widgets.RobotPosition.RobotPosition(self.blankPixmap.scaledToWidth(self.iconSize))
        self.position5Label = lib.widgets.RobotPosition.RobotPosition(self.blankPixmap.scaledToWidth(self.iconSize))
        self.unpositionedLabel = lib.widgets.RobotPosition.RobotPosition(self.robotPixmap.scaledToWidth(self.iconSize))
        
        self.position1Label.clicked.connect(lambda: self.positionRobotIcon(1))
        self.position2Label.clicked.connect(lambda: self.positionRobotIcon(2))
        self.position3Label.clicked.connect(lambda: self.positionRobotIcon(3))
        self.position4Label.clicked.connect(lambda: self.positionRobotIcon(4))
        self.position5Label.clicked.connect(lambda: self.positionRobotIcon(5))
        self.unpositionedLabel.clicked.connect(lambda: self.positionRobotIcon(6))
        
        #Connections
        self.obstacle2Box2016.currentIndexChanged.connect(lambda: self.positionRobotIcon(position=None)) #This and the three below it are necessary for the obstacle to update itself (in case you have the one you're changing selected)
        self.obstacle3Box2016.currentIndexChanged.connect(lambda: self.positionRobotIcon(position=None))
        self.obstacle4Box2016.currentIndexChanged.connect(lambda: self.positionRobotIcon(position=None))
        self.obstacle5Box2016.currentIndexChanged.connect(lambda: self.positionRobotIcon(position=None))

        
        self.grid2016 = QtWidgets.QGridLayout()
        self.grid2016.addWidget(self.lowBarLabel, 0, 0, QtCore.Qt.AlignCenter)
        self.grid2016.addWidget(self.obstacle2Box2016, 0, 1)
        self.grid2016.addWidget(self.obstacle3Box2016, 0, 2)
        self.grid2016.addWidget(self.obstacle4Box2016, 0, 3)
        self.grid2016.addWidget(self.obstacle5Box2016, 0, 4)
        self.grid2016.addWidget(self.noSetPositionLabel, 0, 5)
        self.grid2016.addWidget(self.position1Label, 1, 0, QtCore.Qt.AlignCenter)
        self.grid2016.addWidget(self.position2Label, 1, 1, QtCore.Qt.AlignCenter)
        self.grid2016.addWidget(self.position3Label, 1, 2, QtCore.Qt.AlignCenter)
        self.grid2016.addWidget(self.position4Label, 1, 3, QtCore.Qt.AlignCenter)
        self.grid2016.addWidget(self.position5Label, 1, 4, QtCore.Qt.AlignCenter)
        self.grid2016.addWidget(self.unpositionedLabel, 1, 5, QtCore.Qt.AlignCenter)
        
        self.setLayout(self.grid2016)
        
    def positionRobotIcon(self, position=None): #Function to position the robot icon
        if position is not None:
            self.position1Label.setPixmap(self.blankPixmap.scaledToWidth(self.iconSize)) #Clears all robot icon positions by setting them to blank
            self.position2Label.setPixmap(self.blankPixmap.scaledToWidth(self.iconSize))
            self.position3Label.setPixmap(self.blankPixmap.scaledToWidth(self.iconSize))
            self.position4Label.setPixmap(self.blankPixmap.scaledToWidth(self.iconSize))
            self.position5Label.setPixmap(self.blankPixmap.scaledToWidth(self.iconSize))
            self.unpositionedLabel.setPixmap(self.blankPixmap.scaledToWidth(self.iconSize))

        if (position == 1): #Set Robot icon to selected space
            self.position1Label.setPixmap(self.robotPixmap.scaledToWidth(self.iconSize))
            self.selectedPosition2016 = 1
            self.selectedObstacle2016 = "Low Bar"
        elif (position == 2):
            self.position2Label.setPixmap(self.robotPixmap.scaledToWidth(self.iconSize))
            self.selectedPosition2016 = 2
            self.selectedObstacle2016 = self.obstacle2Box2016.currentText()
        elif (position == 3):
            self.position3Label.setPixmap(self.robotPixmap.scaledToWidth(self.iconSize))
            self.selectedPosition2016 = 3
            self.selectedObstacle2016 = self.obstacle3Box2016.currentText()
        elif (position == 4):
            self.position4Label.setPixmap(self.robotPixmap.scaledToWidth(self.iconSize))
            self.selectedPosition2016 = 4
            self.selectedObstacle2016 = self.obstacle4Box2016.currentText()
        elif (position == 5):
            self.position5Label.setPixmap(self.robotPixmap.scaledToWidth(self.iconSize))
            self.selectedPosition2016 = 5
            self.selectedObstacle2016 = self.obstacle5Box2016.currentText()
        elif (position == 6):
            self.unpositionedLabel.setPixmap(self.robotPixmap.scaledToWidth(self.iconSize))
            self.selectedPosition2016 = 6
            self.selectedObstacle2016 = "None"