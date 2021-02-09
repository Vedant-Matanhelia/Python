class Solution:
    vowels = ['a', 'e', 'i', 'o', 'u']
    def solve(self, s):
        vows = []
        cons = []
        for i in s:
            if i in self.vowels:
                vows.append(i)
            else:
                cons.append(i)
        vows.sort()
        cons.sort()
        return ''.join(vows) + ''.join(cons)