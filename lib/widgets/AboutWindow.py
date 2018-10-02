from PySide2 import QtGui, QtCore, QtWidgets

class AboutWindow(QtWidgets.QWidget):
    def __init__(self):
        super(AboutWindow, self).__init__()
        self.lanceABotFullLogoPixmap = QtGui.QPixmap("img/general/logos/LanceABotFullLogo.png")
        self.aboutWindowVBox = QtWidgets.QVBoxLayout()
        self.lanceABotFullLogoLabel = QtWidgets.QLabel()
        self.lanceABotFullLogoLabel.setPixmap(self.lanceABotFullLogoPixmap)
        self.lanceABotFullLogoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.aboutText = QtWidgets.QLabel("FRC Team 4237's Dashboard\n" +
                                      "Credits:\n" +
                                      "Mark Washington: Original design and programming\n" +
                                      "Special thanks to:\n" +
                                      "Jonathan Woodard: Teaching the next generation to program\n" +
                                      "The programming mentors: For everything they do")
        self.aboutText.setAlignment(QtCore.Qt.AlignCenter)
        self.aboutWindowVBox.addWidget(self.lanceABotFullLogoLabel)
        self.aboutWindowVBox.addWidget(self.aboutText)
        self.setLayout(self.aboutWindowVBox)
        #self.setFixedSize(400, 400)
        self.setWindowTitle("About")