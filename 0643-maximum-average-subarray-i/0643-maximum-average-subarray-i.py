class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        windowSum = sum(nums[:k])
        maxWindowSum = windowSum
        i = 0
        while i + k < len(nums):
            windowSum = windowSum - nums[i] + nums[i+k]
            maxWindowSum = max(maxWindowSum, windowSum)
            i += 1
        return (maxWindowSum / k)
