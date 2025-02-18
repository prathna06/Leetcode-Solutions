class Solution:
    def canJump(self, nums: List[int]) -> bool:
        canReachIndexes  = []
        length = len(nums) - 1
        if length == 0:
            return True
        for i in range(len(nums)-2,-1,-1):         
            if length - i <= nums[i]:
                canReachIndexes.append(i)
            else:
                for j in range(1,nums[i]+1):
                    if (i + j) in canReachIndexes:
                        canReachIndexes.append(i)
                        break
        return 0 in canReachIndexes


            


