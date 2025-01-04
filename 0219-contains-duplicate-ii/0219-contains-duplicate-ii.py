class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp1={}
        for i in range(len(nums)):
            if nums[i] in mp1:
                if abs(i-mp1[nums[i]])<=k:
                    return True
                mp1[nums[i]]=i
            mp1[nums[i]]=i
        return False
