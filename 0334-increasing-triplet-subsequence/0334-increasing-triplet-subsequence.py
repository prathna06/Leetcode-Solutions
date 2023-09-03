class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        val1=val2=float('inf') # so that we can find the smallest values in the array
        for num in nums:
            if num <= val1:
                 val1=num
            elif num <= val2:
                val2=num
            else:
                return True
        return False