class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=0
        i=0
        while(i<len(nums)):
        
            if nums[i]==0:
                count +=1
                del nums[i]
            else:
                i+=1
        i=0
        while(i<count):
         nums.append(0)
         i+=1

