from PySide2 import QtGui, QtCore, QtWidgets
import json
import lib.widgets.RobotPosition

class GameFrame2017(QtWidgets.QFrame):
    def __init__(self):
        super(GameFrame2017, self).__init__()
        self.iconSize = 75

        self.selectedPosition2017 = None
        self.settingsFrame2017 = QtWidgets.QFrame()
        
        self.autonomousSpeed2017 = QtWidgets.QDoubleSpinBox()
        self.autonomousSpeed2017.setValue(1.0)
        self.autonomousSpeed2017.setRange(0.3, 1.0)
        
        self.robotPixmap2017 = QtGui.QPixmap("img/2017/icons/RobotIcon.png")
        self.blankPixmap2017 = QtGui.QPixmap("img/2017/icons/TransparentRobotIcon.png")
        
        self.leftGearPixmap = QtGui.QPixmap("img/2017/icons/LeftGearIcon.png")
        self.centerGearPixmap = QtGui.QPixmap("img/2017/icons/CenterGearIcon.png")
        self.rightGearPixmap = QtGui.QPixmap("img/2017/icons/RightGearIcon.png")
        self.noGearPixmap = QtGui.QPixmap("img/2017/icons/NoGearIcon.png")
        self.transparentLeftGearPixmap = QtGui.QPixmap("img/2017/icons/TransparentLeftGearIcon.png")
        self.transparentCenterGearPixmap = QtGui.QPixmap("img/2017/icons/TransparentCenterGearIcon.png")
        self.transparentRightGearPixmap = QtGui.QPixmap("img/2017/icons/TransparentRightGearIcon.png")
        self.transparentNoGearPixmap = QtGui.QPixmap("img/2017/icons/TransparentNoGearIcon.png")
        
        self.leftBoilerIcon = QtGui.QIcon("img/2017/icons/LeftBoilerIcon.png")
        self.rightBoilerIcon = QtGui.QIcon("img/2017/icons/RightBoilerIcon.png")
        self.transparentLeftBoilerIcon = QtGui.QIcon("img/2017/icons/TransparentLeftBoilerIcon.png")
        self.transparentRightBoilerIcon = QtGui.QIcon("img/2017/icons/TransparentRightBoilerIcon.png")
        
        self.leftGearLabel = QtWidgets.QLabel("Left Gear")
        self.centerGearLabel = QtWidgets.QLabel("Center Gear")
        self.rightGearLabel = QtWidgets.QLabel("Right Gear")
        self.noGearLabel = QtWidgets.QLabel("<font size=10>No Gear</font>")
        self.leftGearLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.centerGearLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.rightGearLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.noGearLabel.setAlignment(QtCore.Qt.AlignCenter)
        
        self.leftGearLabel.setPixmap(self.leftGearPixmap.scaledToWidth(self.iconSize))
        self.centerGearLabel.setPixmap(self.centerGearPixmap.scaledToWidth(self.iconSize))
        self.rightGearLabel.setPixmap(self.rightGearPixmap.scaledToWidth(self.iconSize))
        #self.noGearLabel.setPixmap(self.noGearPixmap.scaledToWidth(self.iconSize))
        
        self.leftBoilerButton = QtWidgets.QToolButton()
        self.rightBoilerButton = QtWidgets.QToolButton()
        
        self.leftBoilerButton.setIcon(self.leftBoilerIcon)
        self.rightBoilerButton.setIcon(self.transparentRightBoilerIcon)
        
        self.leftBoilerButton.setText("Left Boiler")
        self.rightBoilerButton.setText("Right Boiler")
        self.selectedBoiler2017 = "Left"
                
        self.leftBoilerButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.rightBoilerButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        
        self.leftBoilerButton.setIconSize(QtCore.QSize(102, 210))
        self.rightBoilerButton.setIconSize(QtCore.QSize(102, 210))
        
        self.leftBoilerButton.clicked.connect(lambda: self.chooseBoiler(0))
        self.rightBoilerButton.clicked.connect(lambda: self.chooseBoiler(1))
        
        self.position1Label2017 = lib.widgets.RobotPosition.RobotPosition(self.blankPixmap2017.scaledToWidth(self.iconSize))
        self.position2Label2017 = lib.widgets.RobotPosition.RobotPosition(self.blankPixmap2017.scaledToWidth(self.iconSize))
        self.position3Label2017 = lib.widgets.RobotPosition.RobotPosition(self.blankPixmap2017.scaledToWidth(self.iconSize))
        self.position4Label2017 = lib.widgets.RobotPosition.RobotPosition(self.robotPixmap2017.scaledToWidth(self.iconSize))
        
        self.position1Label2017.setAlignment(QtCore.Qt.AlignCenter)
        self.position2Label2017.setAlignment(QtCore.Qt.AlignCenter)
        self.position3Label2017.setAlignment(QtCore.Qt.AlignCenter)
        self.position4Label2017.setAlignment(QtCore.Qt.AlignCenter)
        
        self.selectedPosition2017 = "None"
        
        self.position1Label2017.clicked.connect(lambda: self.positionGearIcon(0))
        self.position2Label2017.clicked.connect(lambda: self.positionGearIcon(1))
        self.position3Label2017.clicked.connect(lambda: self.positionGearIcon(2))
        self.position4Label2017.clicked.connect(lambda: self.positionGearIcon())
        
        '''
        Settings
        '''
        #HSL
        self.settingsGroupBox2017 = QtWidgets.QGroupBox("Settings")

        self.hueLow2017 = QtWidgets.QDoubleSpinBox() 
        self.hueHigh2017 = QtWidgets.QDoubleSpinBox()
        
        self.hueLow2017.setRange(0, 179.99)
        self.hueHigh2017.setRange(0.01, 180)
        self.hueLow2017.valueChanged.connect(lambda: self.watchHSL("low"))
        self.hueHigh2017.valueChanged.connect(lambda: self.watchHSL("high"))
        
        self.saturationLow2017 = QtWidgets.QDoubleSpinBox()
        self.saturationHigh2017 = QtWidgets.QDoubleSpinBox()
        self.saturationLow2017.setRange(0, 254.99)
        self.saturationHigh2017.setRange(0.01, 255)
        self.saturationLow2017.valueChanged.connect(lambda: self.watchHSL("low"))
        self.saturationHigh2017.valueChanged.connect(lambda: self.watchHSL("high"))
        
        self.luminanceLow2017 = QtWidgets.QDoubleSpinBox()
        self.luminanceHigh2017 = QtWidgets.QDoubleSpinBox()
        self.luminanceLow2017.setRange(0, 254.99)
        self.luminanceHigh2017.setRange(0.01, 255)
        self.luminanceLow2017.valueChanged.connect(lambda: self.watchHSL("low"))
        self.luminanceHigh2017.valueChanged.connect(lambda: self.watchHSL("high"))

        self.autoShootingToggle = QtWidgets.QCheckBox("Shooting in auto")
        self.autoShootingToggle.setChecked(True)
        
        self.batteryIDComboBox = QtWidgets.QComboBox()
        self.batteryIDComboBox.addItems(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
        self.batteryIDComboBox.setToolTip("Battery ID")
        
        self.testModeToggle = QtWidgets.QCheckBox("Test Mode")
        
        '''
        Layout
        '''
        
        self.settingsgrid = QtWidgets.QGridLayout()
        self.settingsgrid.addWidget(QtWidgets.QLabel("Hue"), 0, 0, 1, 1)
        self.settingsgrid.addWidget(self.hueLow2017, 1, 0)
        self.settingsgrid.addWidget(QtWidgets.QLabel("-"), 1, 1)
        self.settingsgrid.addWidget(self.hueHigh2017, 1, 2)
        
        self.settingsgrid.addWidget(QtWidgets.QLabel("Saturation"), 2, 0, 1, 1)
        self.settingsgrid.addWidget(self.saturationLow2017, 3, 0)
        self.settingsgrid.addWidget(QtWidgets.QLabel("-"), 3, 1)
        self.settingsgrid.addWidget(self.saturationHigh2017, 3, 2)
        
        self.settingsgrid.addWidget(QtWidgets.QLabel("Luminance"), 4, 0, 1, 1)
        self.settingsgrid.addWidget(self.luminanceLow2017, 5, 0)
        self.settingsgrid.addWidget(QtWidgets.QLabel("-"), 5, 1)
        self.settingsgrid.addWidget(self.luminanceHigh2017, 5, 2)
        
        self.settingsgrid.addWidget(self.autoShootingToggle, 6, 0, 1, 3)
        self.settingsgrid.addWidget(self.batteryIDComboBox, 7, 0, 1, 3)
        self.settingsgrid.addWidget(self.testModeToggle, 8, 0, 1, 3)
        
        self.settingsGroupBox2017.setLayout(self.settingsgrid)
        
        self.grid = QtWidgets.QGridLayout()
        self.grid.addWidget(self.leftBoilerButton, 0, 0, 2, 1)
        self.grid.addWidget(self.leftGearLabel, 0, 1)
        self.grid.addWidget(self.centerGearLabel, 0, 2)
        self.grid.addWidget(self.rightGearLabel, 0, 3)
        self.grid.addWidget(self.noGearLabel, 0, 4)
        self.grid.addWidget(self.rightBoilerButton, 0, 5, 2, 1)
        #self.grid.addWidget(self.settingsGroupBox2017, 0, 6, 2, 1)
        self.grid.addWidget(self.settingsGroupBox2017,0, 6, 2, 1)
        self.grid.addWidget(self.position1Label2017, 1, 1)
        self.grid.addWidget(self.position2Label2017, 1, 2)
        self.grid.addWidget(self.position3Label2017, 1, 3)
        self.grid.addWidget(self.position4Label2017, 1, 4)
        self.setLayout(self.grid)

    def positionGearIcon(self, position=None):
        #None = No gear
        #0 = left
        #1 = center
        #2 = right
        self.position1Label2017.setPixmap(self.blankPixmap2017.scaledToWidth(self.iconSize))
        self.position2Label2017.setPixmap(self.blankPixmap2017.scaledToWidth(self.iconSize))
        self.position3Label2017.setPixmap(self.blankPixmap2017.scaledToWidth(self.iconSize))
        self.position4Label2017.setPixmap(self.blankPixmap2017.scaledToWidth(self.iconSize))
        if position is not None:
            if position == 0:
                self.selectedPosition2017 = "Left"
                self.position1Label2017.setPixmap(self.robotPixmap2017.scaledToWidth(self.iconSize))
            elif position == 1:
                self.selectedPosition2017 = "Center"
                self.position2Label2017.setPixmap(self.robotPixmap2017.scaledToWidth(self.iconSize))
            elif position == 2:            
                self.selectedPosition2017 = "Right"
                self.position3Label2017.setPixmap(self.robotPixmap2017.scaledToWidth(self.iconSize))
        else:
            self.selectedPosition2017 = "None"
            self.position4Label2017.setPixmap(self.robotPixmap2017.scaledToWidth(self.iconSize))
        print(self.selectedPosition2017)
        
    '''
    Function to change between left and right boiler    
    '''    
    def chooseBoiler(self, boiler=0):
        if boiler is not None:
            self.leftBoilerButton.setIcon(self.transparentLeftBoilerIcon)
            self.rightBoilerButton.setIcon(self.transparentRightBoilerIcon)
            if boiler == 0:
                self.leftBoilerButton.setIcon(self.leftBoilerIcon)
                self.selectedBoiler2017 = "Left"
            elif boiler == 1:
                self.rightBoilerButton.setIcon(self.rightBoilerIcon)
                self.selectedBoiler2017 = "Right"

    def watchHSL(self, whichSpinBox):
        #Check to make sure HSL values can't go over or under each other
        if (self.hueLow2017.value() >= self.hueHigh2017.value() and whichSpinBox == "low"):
            self.hueLow2017.setValue(self.hueHigh2017.value() - 1)
        elif (self.hueHigh2017.value() <= self.hueLow2017.value() and whichSpinBox == "high"):
            self.hueHigh2017.setValue(self.hueLow2017.value() + 1)
            
        if (self.saturationLow2017.value() >= self.saturationHigh2017.value() and whichSpinBox == "low"):
            self.saturationLow2017.setValue(self.saturationHigh2017.value() - 1)
        elif (self.saturationHigh2017.value() <= self.saturationLow2017.value() and whichSpinBox == "high"):
            self.saturationHigh2017.setValue(self.saturationLow2017.value() + 1)
        
        if (self.luminanceLow2017.value() >= self.luminanceHigh2017.value() and whichSpinBox == "low"):
            self.luminanceLow2017.setValue(self.luminanceHigh2017.value() - 1)
        elif (self.luminanceHigh2017.value() <= self.luminanceLow2017.value() and whichSpinBox == "high"):
            self.luminanceHigh2017.setValue(self.luminanceLow2017.value() + 1)
    