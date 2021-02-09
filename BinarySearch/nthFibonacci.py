class Solution:
    def solve(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.solve(n) + self.solve(n-1)

solve = Solution()
print(Solution.solve(2))