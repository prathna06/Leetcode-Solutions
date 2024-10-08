class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        res=[]
        for i in range(len(s)):
            res.append(s[i])       
        return " ".join(res[::-1])