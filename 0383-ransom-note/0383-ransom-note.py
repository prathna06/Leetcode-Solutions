class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mp1={}
        mp2={}
        flag=True
        for i in range(len(ransomNote)):
            mp1[ransomNote[i]]=ransomNote.count(ransomNote[i])
        for j in range(len(magazine)):
            mp2[magazine[j]]=magazine.count(magazine[j])
        
        for k in mp1:
            if k not in mp2 or mp1[k]>mp2[k]:
                flag =False
        if flag == True:
            return True
        else:
            return False

                
