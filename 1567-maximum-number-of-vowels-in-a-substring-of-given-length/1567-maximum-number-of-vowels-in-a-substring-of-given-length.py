class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        start=0
        vowels=["a","e","i","o","u"]
        counter =0
        maxCounter =0
        for i in range(k):
            if s[i] in vowels:
                counter +=1
            maxCounter = counter
        i=0  
        while(k<len(s)):
            if maxCounter == k:
                return maxCounter
            if s[i] in vowels:
                counter -=1                       
            if s[k] in vowels:
                counter +=1
            k+=1
            i+=1  
            maxCounter = max(maxCounter,counter)
        return maxCounter
            