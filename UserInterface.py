# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_windows(object):
    def get_input_data(self):
        x = self.inputText.toPlainText()  # this for getting input data from input box
        #print(x)
        return x
    def setupUi(self, windows):
        windows.setObjectName("windows")

        windows.resize(564, 372)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        windows.setWindowIcon(icon)
        windows.setAutoFillBackground(False)
        windows.setStyleSheet("background-color: rgb(255, 255, 255);")
        windows.setSizeGripEnabled(False)
        self.inputText = QtWidgets.QPlainTextEdit(windows)
        self.inputText.setGeometry(QtCore.QRect(20, 60, 251, 221))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        self.inputText.setFont(font)
        self.inputText.setObjectName("inputText")
        self.text = QtWidgets.QLabel(windows)
        self.text.setGeometry(QtCore.QRect(100, 30, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.text.setFont(font)
        self.text.setObjectName("text")
        self.percentage = QtWidgets.QLabel(windows)
        self.percentage.setGeometry(QtCore.QRect(380, 30, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.percentage.setFont(font)
        self.percentage.setObjectName("percentage")
        self.label_3 = QtWidgets.QLabel(windows)
        self.label_3.setGeometry(QtCore.QRect(350, 100, 181, 20))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(windows)
        self.label_4.setGeometry(QtCore.QRect(310, 340, 231, 41))
        self.label_4.setStyleSheet("font: 14pt \"Blackadder ITC\";\n"
"color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.reset = QtWidgets.QPushButton(windows)
        self.reset.setGeometry(QtCore.QRect(20, 310, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.reset.setFont(font)
        self.reset.setAutoFillBackground(False)
        self.reset.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.reset.setObjectName("reset")
        self.check = QtWidgets.QPushButton(windows)
        self.check.clicked.connect(self.get_input_data)
        self.check.setGeometry(QtCore.QRect(290, 310, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.check.setFont(font)
        self.check.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.check.setObjectName("check")
        self.progressBar = QtWidgets.QProgressBar(windows)
        self.progressBar.setGeometry(QtCore.QRect(280, 60, 271, 21))
        self.progressBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.listWidget = QtWidgets.QListWidget(windows)
        self.listWidget.setGeometry(QtCore.QRect(285, 130, 271, 151))
        self.listWidget.setObjectName("listView")
        self.retranslateUi(windows)
        self.reset.clicked.connect(self.inputText.clear)
        self.reset.clicked.connect(self.progressBar.reset)#new edit
        self.reset.clicked.connect(self.listWidget.clear)#new edit
        QtCore.QMetaObject.connectSlotsByName(windows)

    def retranslateUi(self, windows):
        _translate = QtCore.QCoreApplication.translate
        windows.setWindowTitle(_translate("windows", "Bangla Plagiarism Checker"))
        self.inputText.setPlaceholderText(_translate("windows", "Enter Your Bangla Text"))
        self.text.setText(_translate("windows", "Text"))
        self.percentage.setText(_translate("windows", "Percentage"))
        self.label_3.setText(_translate("windows", "Matched Sources"))
        self.label_4.setText(_translate("windows", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">Developed By Raj &amp; Kanij</span></p></body></html>"))
        self.reset.setText(_translate("windows", "Reset"))
        self.check.setText(_translate("windows", "Check"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    windows = QtWidgets.QDialog()
    ui = Ui_windows()
    ui.setupUi(windows)
    windows.show()
    sys.exit(app.exec_())
