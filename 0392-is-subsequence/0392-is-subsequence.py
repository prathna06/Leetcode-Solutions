class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j=0
        string=""
        if len(s) == 0:
            return True
        for i in range(len(t)):
            if s[j]==t[i]:
                j+=1
                string = string + t[i]
            if string==s:
                return True

        return False