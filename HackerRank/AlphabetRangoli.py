"""
Print the following pattern:

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

"""

# import the lowercase characters
from string import ascii_lowercase


def print_rangoli(size):
    lines = []
    for row in range(size):
        to_print = '-'.join(ascii_lowercase[row:size])
        lines.append(to_print[::-1] + to_print[1:])
    width = len(lines[0])

    for row in range(size-1, 0, -1):
        print(lines[row].center(width, '-'))

    for row in range(size):
        print(lines[row].center(width, '-'))

if __name__ == "__main__":
    n = int(input())
    print_rangoli(n)
