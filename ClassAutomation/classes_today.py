# This file contains all the functions used by the class automator

import webbrowser
import calendar
from datetime import datetime

subjects = {
    'monday': ['physics', 'chemistry', 'maths', 'ctp'],
    'tuesday': ['', 'chemistry', 'phy', 'maths'],
    'wednesday': ['chemistry', 'phy', 'eng', 'activity'],
    'thursday': ['cs', '', 'chemistry', 'english'],
    'friday': ['phy', 'maths', 'cs', ''],
    'saturday': ['', 'maths', 'english', '']
}

classes = {
    "physics": "https://meet.google.com/lookup/bd2mrm5c6z?authuser=0&hs=179",
    "chemistry": "https://meet.google.com/lookup/cxj7nndo6y?authuser=0&hs=179",
    "maths": "https://meet.google.com/lookup/d2armv3ezo?authuser=0&hs=179",
    "ctp": "https://meet.google.com/lookup/e646suwucd?authuser=0&hs=179",
    "english": "https://meet.google.com/lookup/h7sqmulydo?authuser=0&hs=179",
    "activity": "https://meet.google.com/lookup/gjjdzop72v?authuser=0&hs=179",
    "cs": "https://meet.google.com/lookup/fdm7irokpb?authuser=0&hs=179"
}


def find_day() -> str:
    """
    This function tells the day
    :return: day
    """
    date_and_time = datetime.now()
    date = str(date_and_time.day) + ' ' + str(date_and_time.month) + ' ' + str(date_and_time.year)
    date = datetime.strptime(date, '%d %m %Y').weekday()
    day = calendar.day_name[date]
    return day.lower()


def find_classes() -> list:
    """
    This function makes a list of all the classes of the day returned by find_day and joins them with there timings
    :return: subs
    """
    subs = []
    today = find_day()
    lectures = subjects[today]
    timings = ['09:30 am - 10:30 am', '11:00 am - 12:00 pm', '12:30 pm - 13:30 pm', '15:00 pm - 16:40 pm']
    for i in range(4):
        formatted = '{} {}'.format(timings[i], lectures[i])
        subs.append(formatted)
    return subs


def classes_today() -> None:
    """
    Tells the time-table and tells what class is going on right now
    :return: None
    """
    subs = find_classes()
    for i in subs:
        time = datetime.now().strftime("%H:%M:S")
        time = time.split(":")
        if time[0] == i[0:2] and time[1] <= i[3:5]:
            print(i, " <-- Current Session")
        elif time[0] == i[11:13] and time[1] <= i[14:16]:
            print(i, " <-- Current Session")
        else:
            print(i)


def help_menu() -> None:
    """
    This is the help menu
    :return: None
    """
    print("class HELP or -h for the help menu")
    print("class [subject_name] to open the link")
    print("class TODAY or -t to list today\'s classes")


def open_class(url) -> None:
    """
    Open the class link on google
    :param url: -> the link to join
    :return: None
    """
    webbrowser.open(url)
