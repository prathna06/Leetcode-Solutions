
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        mp={}
        res=0
        for i in range(101):            
            mp[i]=nums.count(i)
            res =res + (mp[i]*(mp[i]-1)//2)
        return res
        
        