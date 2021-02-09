class Solution:
    def solve(self, s):
        words = s.split(" ")
        acronym = []
        for i in words:
            if i.lower() == 'and':
                continue
            else:
                acronym.append(i[0].upper())
        return ''.join(acronym) 