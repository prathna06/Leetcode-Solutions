class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current = 1
        count = 0 
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                count = 0
                nums[current] = nums[i]
                current += 1
            
            
            else:
                count += 1
                if count <= 1:
                    nums[current] = nums[i]
                    current += 1
        
        return current