class Solution:
    def solve(self, num):
        num = str(num)
        if num[::-1] == num[::]:
            return True
        else:
            return False