class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        maxCounter = counter = 0
        for i in range(len(s)-k+1):
            string=s[i:k]
            counter=string.count('a')+string.count('e')+string.count('i')+string.count('o')+string.count('u')
            k+=1
            maxCounter = max(maxCounter,counter)
        return maxCounter