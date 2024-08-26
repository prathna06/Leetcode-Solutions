class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:   
        i=0
        while(i<len(nums)):
            for j in range(i+1,len(nums)):
                total= nums[i]+nums[j]
                if total == target:
                    return[i,j]
            i+=1
        return []