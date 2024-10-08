class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix=1
        suffix=1
        result=[1]*length
        for i in range(length):
            result[i]=prefix
            prefix*=nums[i]
        for i in range(length-1,-1,-1):
            result[i]*=suffix
            suffix*=nums[i]
        return result
        

            
            
           
        