class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        wordDict={}
        for char in magazine:
            if char not in wordDict:
                wordDict[char]=1
            else:
                wordDict[char] += 1
        for char in ransomNote:
            if char in wordDict and wordDict[char]>0:
                wordDict[char]-=1
            else:
                return False
        return True


                
