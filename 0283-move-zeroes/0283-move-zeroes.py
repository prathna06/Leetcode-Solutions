class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = len(nums) - 1
        while i < len(nums) and i < j:
            if nums[i] == 0:
                nums.pop(i)
                print(nums, i)
                nums.append(0)
                print(nums)
                j -= 1
                i -= 1
            i += 1
        