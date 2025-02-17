class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        while s and s[-1] == ' ':
         s = s[:-1]
        return len(s.split()[-1])


        