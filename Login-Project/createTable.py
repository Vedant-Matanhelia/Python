import sqlite3

dataBase = sqlite3.connect("loginSystem.db")
dataBase.row_factory = sqlite3.Row
cursor = dataBase.cursor()

cursor.execute(
    """
    CREATE table users (
        FirstName TEXT,
        LastName TEXT,
        username TEXT,
        email TEXT,
        password TEXT
    )
    """
)