from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from LoginUi import LoginUi
import sys
import sqlite3

dataBase = sqlite3.connect("loginSystem.db")
dataBase.row_factory = sqlite3.Row
cursor = dataBase.cursor()


class LoginForm(QMainWindow, LoginUi):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_button.clicked.connect(self.login)
        self.create_acc.clicked.connect(self.create_account)
        self.show()

    def login(self):
        cursor.execute(
            "select * from users WHERE username=? or email=? and password=?",
            (self.username.text(), self.username.text(), self.password.text()),
        )
        data = cursor.fetchone()
        if data is not None:
            print("Login Successful")
        else:
            print("Login Failed")

    def create_account(self):
        print("Create Account button clicked")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = LoginForm()
    sys.exit(app.exec_())
