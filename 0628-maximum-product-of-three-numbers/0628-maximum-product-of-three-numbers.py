class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        lis=  sorted(nums)  
        return max(lis[-1]*lis[-2]*lis[-3],lis[0]*lis[1]*lis[-1])