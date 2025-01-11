class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum,rightSum = 0, sum(nums)

        for ind,ele in enumerate(nums):
            rightSum -= ele
            if leftSum == rightSum:
                return ind

            leftSum += ele

        return -1

        


        