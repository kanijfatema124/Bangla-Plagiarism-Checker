from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
import sys

import UserInterface

class ApplicationWindow(UserInterface.Ui_windows,QDialog):

    #    set progress value
    def setProgressValue(self,new_value):
        self.progressBar.setProperty("value",new_value)

    def getInputValue(self):
        x = self.inputText.toPlainText()  # this for getting input data from
        return x


    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.progressBar.setProperty("value",0)


