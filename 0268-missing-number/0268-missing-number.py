class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = sum(nums)
        req =len(nums)*(len(nums)+1)/2
        return int(req - ans)