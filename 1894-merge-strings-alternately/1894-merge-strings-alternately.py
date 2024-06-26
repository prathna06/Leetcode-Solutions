class Solution:

    def mergeAlternately(self, word1: str, word2: str) -> str:
        arr=[]
        if len(word1) >= len(word2):
            longword=word1
        else:
            longword=word2
        for i in range(min(len(word1),len(word2))):
            arr.append(word1[i])
            arr.append(word2[i])
        
        return (''.join(arr)+ longword[min(len(word1),len(word2)):])