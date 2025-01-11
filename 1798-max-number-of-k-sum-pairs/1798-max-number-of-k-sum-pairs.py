class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        left = 0
        right = len(nums)-1
        removal = 0
        nums.sort()
        while left<right:
            currSum = nums[left] + nums[right]
            if currSum == k:
                removal+=1
                left += 1
                right -= 1
            elif currSum < k:
                left += 1
            else:
                right -= 1
            
        return removal
        