n, m = map(int, input().split())

"""
    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
"""

# for the first half
for i in range(1, n, 2):
	print((i*".|.").center(m, '-'))

print('WELCOME'.center(m, '-'))
# for the second half
for j in range(n-2, -1, -2):
	print((j*'.|.').center(m, '-'))