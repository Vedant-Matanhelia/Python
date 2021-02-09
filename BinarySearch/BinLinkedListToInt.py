class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def solve(self, node):
        nums = []
        num = 0
        while node:
            nums.append(str(node.val))
            node = node.next
        num = int("".join(nums), 2)
        return num