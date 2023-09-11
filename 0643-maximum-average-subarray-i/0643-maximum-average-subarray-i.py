class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start = 0
        end = k
        maxSum=0
        subset= nums[start:end] 
        sumValue = sum(subset)
        maxSum = sumValue
        if (k == len(nums)):
            maxSum = sumValue
        while end < len(nums):
            sumValue = sumValue - nums  [start] +nums[end]
            maxSum = max(maxSum,sumValue)
            start +=1
            end +=1
        return maxSum/k



        