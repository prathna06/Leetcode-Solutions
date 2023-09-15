class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        index =0
        while(index<len(nums)):
            sumRightArr = sum(nums[index+1:len(nums)])
            if index ==0:
                sumLeftArr =0
            else:     
                sumLeftArr = sum(nums[0:index])            
            if sumRightArr == sumLeftArr:
                return index
            index +=1
        return -1
            