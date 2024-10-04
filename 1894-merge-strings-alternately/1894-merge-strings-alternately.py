class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        newarr=[]
        for i in range(min(len(word1),len(word2))):
            newarr.append(word1[i])
            newarr.append(word2[i])
        if len(word1)>len(word2): 
            newStr =newarr +list(word1)[i+1:]
            return (''.join(newStr))
        if len(word1)<len(word2): 
            newStr =newarr +list(word2)[i+1:]
            return (''.join(newStr))
        else:
            return (''.join(newarr))


