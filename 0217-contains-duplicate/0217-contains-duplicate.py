class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        lenth = len(set(nums))
        if lenth == len(nums):
            return False
        else:
           return True
         