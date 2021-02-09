class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def solve(self, node):
        count = 0
        while node:
            count += 1
            node = node.next
        return node