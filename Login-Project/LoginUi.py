# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class LoginUi(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(411, 421)
        MainWindow.setMaximumSize(QtCore.QSize(486, 421))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("*{\n"
"    font-family: century gothic;\n"
"    font-size : 24px;\n"
"}\n"
"QFrame{\n"
"    background: rgba(0,0,0,0.8);\n"
"    border-radius: 15px;\n"
"}\n"
"QLabel{\n"
"    color: white;\n"
"    background: transparent;\n"
"}\n"
"QPushButton{\n"
"    background: red;\n"
"    color: white;\n"
"    border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"    background: #49ebff;\n"
"    color: #333;\n"
"    border-radius: 15px;\n"
"}\n"
"QLineEdit{\n"
"    background: transparent;\n"
"    border: none;\n"
"    color: #717072;\n"
"    border-bottom: 1px solid #717072;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 411, 421))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lbl = QtWidgets.QLabel(self.frame)
        self.lbl.setGeometry(QtCore.QRect(120, 20, 101, 31))
        self.lbl.setObjectName("lbl")
        self.create_acc = QtWidgets.QPushButton(self.frame)
        self.create_acc.setGeometry(QtCore.QRect(20, 340, 361, 51))
        self.create_acc.setObjectName("create_acc")
        self.username = QtWidgets.QLineEdit(self.frame)
        self.username.setGeometry(QtCore.QRect(20, 130, 351, 41))
        self.username.setText("")
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.frame)
        self.password.setGeometry(QtCore.QRect(20, 230, 351, 41))
        self.password.setText("")
        self.password.setObjectName("password")
        self.lbl_2 = QtWidgets.QLabel(self.frame)
        self.lbl_2.setGeometry(QtCore.QRect(20, 100, 131, 31))
        self.lbl_2.setObjectName("lbl_2")
        self.lbl_3 = QtWidgets.QLabel(self.frame)
        self.lbl_3.setGeometry(QtCore.QRect(20, 190, 131, 31))
        self.lbl_3.setObjectName("lbl_3")
        self.login_button = QtWidgets.QPushButton(self.frame)
        self.login_button.setGeometry(QtCore.QRect(20, 282, 361, 51))
        self.login_button.setObjectName("login_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.lbl.setText(_translate("MainWindow", "LOGIN"))
        self.create_acc.setText(_translate("MainWindow", "NEW USER"))
        self.username.setPlaceholderText(_translate("MainWindow", "Username or email"))
        self.password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.lbl_2.setText(_translate("MainWindow", "Username"))
        self.lbl_3.setText(_translate("MainWindow", "Password"))
        self.login_button.setText(_translate("MainWindow", "LOGIN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = LoginUi()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
