from PySide2 import QtGui, QtCore, QtWidgets
import lib.widgets.RobotPosition

class GameFrame2019(QtWidgets.QFrame):
    def __init__(self):
        super(GameFrame2019, self).__init__()
        self.iconSize = 150

        '''
        Widgets
        '''

        self.robotPixmap2019 = QtGui.QPixmap("img/2018/icons/RobotIcon.png")
        self.blankPixmap2019 = QtGui.QPixmap("img/2018/icons/TransparentRobotIcon.png")

        self.layout = QtWidgets.QGridLayout()

        self.setLayout(self.layout)