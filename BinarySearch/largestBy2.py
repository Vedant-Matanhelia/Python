class Solution:
    def solve(self, nums):
        largest = max(nums)
        nums.remove(largest)
        if largest > (max(nums) * 2):
            return True
        else:
            return False