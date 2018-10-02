from PySide2 import QtGui, QtCore, QtWidgets

class RobotPosition(QtWidgets.QLabel):
    clicked = QtCore.Signal()
    
    def __init__(self, image, parent=None):
        super(RobotPosition, self).__init__(parent)
        self.setPixmap(image)
        
    def mousePressEvent(self, event):
        self.clicked.emit()