# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_acc_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class CreateAccUi(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(497, 460)
        MainWindow.setMaximumSize(QtCore.QSize(529, 491))
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
        self.frame.setGeometry(QtCore.QRect(0, 0, 501, 461))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(190, 10, 101, 51))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 131, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(260, 110, 131, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(30, 200, 131, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(260, 200, 131, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(30, 290, 131, 41))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(260, 290, 221, 41))
        self.label_7.setObjectName("label_7")
        self.first_name = QtWidgets.QLineEdit(self.frame)
        self.first_name.setGeometry(QtCore.QRect(30, 150, 171, 31))
        self.first_name.setObjectName("first_name")
        self.last_name = QtWidgets.QLineEdit(self.frame)
        self.last_name.setGeometry(QtCore.QRect(260, 150, 191, 31))
        self.last_name.setObjectName("last_name")
        self.username = QtWidgets.QLineEdit(self.frame)
        self.username.setGeometry(QtCore.QRect(30, 240, 171, 31))
        self.username.setObjectName("username")
        self.email = QtWidgets.QLineEdit(self.frame)
        self.email.setGeometry(QtCore.QRect(260, 240, 211, 31))
        self.email.setObjectName("email")
        self.password = QtWidgets.QLineEdit(self.frame)
        self.password.setGeometry(QtCore.QRect(30, 330, 171, 31))
        self.password.setObjectName("password")
        self.confirm_password = QtWidgets.QLineEdit(self.frame)
        self.confirm_password.setGeometry(QtCore.QRect(260, 330, 221, 31))
        self.confirm_password.setObjectName("confirm_password")
        self.submit = QtWidgets.QPushButton(self.frame)
        self.submit.setGeometry(QtCore.QRect(90, 392, 301, 41))
        self.submit.setObjectName("submit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "New User"))
        self.label.setText(_translate("MainWindow", "SIGN UP"))
        self.label_2.setText(_translate("MainWindow", "First Name"))
        self.label_3.setText(_translate("MainWindow", "Last Name"))
        self.label_4.setText(_translate("MainWindow", "Username"))
        self.label_5.setText(_translate("MainWindow", "Email"))
        self.label_6.setText(_translate("MainWindow", "Password"))
        self.label_7.setText(_translate("MainWindow", "Confirm Password"))
        self.first_name.setPlaceholderText(_translate("MainWindow", "First Name"))
        self.last_name.setPlaceholderText(_translate("MainWindow", "Last Name"))
        self.username.setPlaceholderText(_translate("MainWindow", "Username"))
        self.email.setPlaceholderText(_translate("MainWindow", "Email"))
        self.password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.confirm_password.setPlaceholderText(_translate("MainWindow", "Confirm Password"))
        self.submit.setText(_translate("MainWindow", "SUBMIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = CreateAccUi()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())