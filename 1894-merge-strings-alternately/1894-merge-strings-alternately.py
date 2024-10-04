class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        newStr=''
        l1,l2= len(word1),len(word2)
        for i in range(min(l1,l2)):
           newStr +=word1[i]
           newStr += word2[i]
        newStr+= word1[i+1:] if l1>l2 else word2[i+1:]

        return newStr


