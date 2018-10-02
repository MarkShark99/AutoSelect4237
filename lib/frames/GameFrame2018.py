from PySide2 import QtGui, QtCore, QtWidgets
import lib.widgets.RobotPosition

class GameFrame2018(QtWidgets.QFrame):
    def __init__(self):
        super(GameFrame2018, self).__init__()
        self.iconSize = 150
        self.selectedPosition = "None"
        self.selectedTarget = "Switch"
        self.selectedBackupPlan = "Auto Line"

        '''
        Widgets
        '''
        
        self.robotPixmap2018 = QtGui.QPixmap("img/2018/icons/RobotIcon.png")
        self.blankPixmap2018 = QtGui.QPixmap("img/2018/icons/TransparentRobotIcon.png")
        self.switchPixmap = QtGui.QPixmap("img/2018/icons/SwitchIcon.png")
        self.scalePixmap = QtGui.QPixmap("img/2018/icons/ScaleIcon.png")
        self.autoLinePixmap = QtGui.QPixmap("img/2018/icons/AutoLineIcon.png")
        self.transparentSwitchPixmap = QtGui.QPixmap("img/2018/icons/TransparentSwitchIcon.png")
        self.transparentScalePixmap = QtGui.QPixmap("img/2018/icons/TransparentScaleIcon.png")
        self.transparentAutoLinePixmap = QtGui.QPixmap("img/2018/icons/TransparentAutoLineIcon.png")
        
        self.position1Button = lib.widgets.RobotPosition.RobotPosition(self.blankPixmap2018.scaledToWidth(75))
        self.position2Button = lib.widgets.RobotPosition.RobotPosition(self.blankPixmap2018.scaledToWidth(75))
        self.position3Button = lib.widgets.RobotPosition.RobotPosition(self.blankPixmap2018.scaledToWidth(75))
        self.noPositionButton = lib.widgets.RobotPosition.RobotPosition(self.robotPixmap2018.scaledToWidth(75))
        
        self.position1Button.setAlignment(QtCore.Qt.AlignCenter)
        self.position2Button.setAlignment(QtCore.Qt.AlignCenter)
        self.position3Button.setAlignment(QtCore.Qt.AlignCenter)
        self.noPositionButton.setAlignment(QtCore.Qt.AlignCenter)
        
        self.position1Button.clicked.connect(lambda: self.positionRobot(0))
        self.position2Button.clicked.connect(lambda: self.positionRobot(1))
        self.position3Button.clicked.connect(lambda: self.positionRobot(2))
        self.noPositionButton.clicked.connect(lambda: self.positionRobot("None"))

        self.leftPositionLabel = QtWidgets.QLabel("Left")
        self.leftPositionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.centerPositionLabel = QtWidgets.QLabel("Center")
        self.centerPositionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.rightPositionLabel = QtWidgets.QLabel("Right")
        self.rightPositionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.noPositionLabel = QtWidgets.QLabel("None")
        self.noPositionLabel.setAlignment(QtCore.Qt.AlignCenter)
        
        self.planAComboBox = QtWidgets.QComboBox()
        self.planBComboBox = QtWidgets.QComboBox()
        self.planCComboBox = QtWidgets.QComboBox()
        
        self.checkBoxFrame = QtWidgets.QFrame()
        self.checkBoxVBox = QtWidgets.QVBoxLayout()
        
        self.holdCubeForOppositeScaleCheckBox = QtWidgets.QCheckBox("Hold Cube for Opposite Scale")
        
        self.grabSecondCubeCheckBox = QtWidgets.QCheckBox("Grab Second Cube")
        
        self.holdSecondCubeRadioButton = QtWidgets.QRadioButton("Hold second cube")
        self.placeSecondCubeInSwitchRadioButton = QtWidgets.QRadioButton("Place Second Cube in Switch")
        self.placeSecondCubeInScaleRadioButton = QtWidgets.QRadioButton("Place Second Cube in Scale")
        
        self.holdSecondCubeRadioButton.setEnabled(False)
        self.placeSecondCubeInSwitchRadioButton.setEnabled(False)
        self.placeSecondCubeInScaleRadioButton.setEnabled(False)
        
        self.grabSecondCubeCheckBox.clicked.connect(lambda: self.synchronizeCheckBoxes())
        
        self.checkBoxVBox.addWidget(self.holdCubeForOppositeScaleCheckBox)
        self.checkBoxVBox.addWidget(self.grabSecondCubeCheckBox)
        self.checkBoxVBox.addWidget(self.holdSecondCubeRadioButton)
        self.checkBoxVBox.addWidget(self.placeSecondCubeInSwitchRadioButton)
        self.checkBoxVBox.addWidget(self.placeSecondCubeInScaleRadioButton)
        
        self.checkBoxFrame.setLayout(self.checkBoxVBox)
        
        for cb in [self.planAComboBox, self.planBComboBox, self.planCComboBox]:
            cb.addItem(self.switchPixmap, "Left Switch")
            cb.addItem(self.switchPixmap, "Right Switch")
            
            cb.addItem(self.scalePixmap, "Left Scale")
            cb.addItem(self.scalePixmap, "Right Scale")
            
            cb.addItem(self.autoLinePixmap, "Auto Line")
            cb.setIconSize(QtCore.QSize(75, 75))
            
        self.planALabel = QtWidgets.QLabel("Plan A")
        self.planBLabel = QtWidgets.QLabel("Plan B")
        self.planCLabel = QtWidgets.QLabel("Plan C")
        
        self.planALabel.setAlignment(QtCore.Qt.AlignCenter)
        self.planBLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.planCLabel.setAlignment(QtCore.Qt.AlignCenter)
               
        self.layout = QtWidgets.QGridLayout()
        
        self.layout.addWidget(self.planALabel, 0, 0)
        self.layout.addWidget(self.planBLabel, 0, 1)
        self.layout.addWidget(self.planCLabel, 0, 2)
        
        self.layout.addWidget(self.planAComboBox, 1, 0)
        self.layout.addWidget(self.planBComboBox, 1, 1)
        self.layout.addWidget(self.planCComboBox, 1, 2)
        self.layout.addWidget(self.checkBoxFrame, 1, 3)
        
        self.layout.addWidget(self.position1Button, 2, 0)
        self.layout.addWidget(self.position2Button, 2, 1)
        self.layout.addWidget(self.position3Button, 2, 2)
        self.layout.addWidget(self.noPositionButton, 2, 3)
        
        self.layout.addWidget(self.leftPositionLabel, 3, 0)
        self.layout.addWidget(self.centerPositionLabel, 3, 1)
        self.layout.addWidget(self.rightPositionLabel, 3, 2)
        self.layout.addWidget(self.noPositionLabel, 3, 3)
        
        self.setLayout(self.layout)

        
    def synchronizeCheckBoxes(self):
        self.holdSecondCubeRadioButton.setEnabled(self.grabSecondCubeCheckBox.isChecked())
        self.placeSecondCubeInSwitchRadioButton.setEnabled(self.grabSecondCubeCheckBox.isChecked())
        self.placeSecondCubeInScaleRadioButton.setEnabled(self.grabSecondCubeCheckBox.isChecked())

        if not self.grabSecondCubeCheckBox.isChecked():
            self.holdSecondCubeRadioButton.setChecked(False)
            self.placeSecondCubeInSwitchRadioButton.setChecked(False)
            self.placeSecondCubeInScaleRadioButton.setChecked(False)
            
        
    def positionRobot(self, position):
        self.selectedPosition = position
        
        self.position1Button.setPixmap(self.blankPixmap2018.scaledToWidth(75))
        self.position2Button.setPixmap(self.blankPixmap2018.scaledToWidth(75))
        self.position3Button.setPixmap(self.blankPixmap2018.scaledToWidth(75))
        self.noPositionButton.setPixmap(self.blankPixmap2018.scaledToWidth(75))
                
        if position is 0:
            self.selectedPosition = "Left"
            self.position1Button.setPixmap(self.robotPixmap2018.scaledToWidth(75))
        elif position is 1:
            self.selectedPosition = "Center"
            self.position2Button.setPixmap(self.robotPixmap2018.scaledToWidth(75))
        elif position is 2:
            self.selectedPosition = "Right"
            self.position3Button.setPixmap(self.robotPixmap2018.scaledToWidth(75))
        elif position is "None":
            self.selectedPosition = "None"
            self.noPositionButton.setPixmap(self.robotPixmap2018.scaledToWidth(75))
        
    def getJsonData(self):
        data = {}
        data["selectedPosition"] = self.selectedPosition
        data["planA"] = self.planAComboBox.currentText()
        data["planB"] = self.planBComboBox.currentText()
        data["planC"] = self.planCComboBox.currentText()
        data["grabSecondCube"] = self.grabSecondCubeCheckBox.isChecked()
        data["holdSecondCube"] = self.holdSecondCubeRadioButton.isChecked()
        data["placeSecondCubeInSwitch"] = self.placeSecondCubeInSwitchRadioButton.isChecked()
        data["placeSecondCubeInScale"] = self.placeSecondCubeInScaleRadioButton.isChecked()
        data["holdCubeForOppositeScale"] = self.holdCubeForOppositeScaleCheckBox.isChecked()
        return data