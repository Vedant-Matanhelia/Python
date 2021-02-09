import sys

from classes_today import *

inp = sys.argv[1].lower()

if inp in classes:
    open_class(classes[inp])
elif inp == "today" or inp == "-t":
    classes_today()
elif inp=="help" or inp=="-h":
    help_menu()
else:
    print("Invalid Command")
