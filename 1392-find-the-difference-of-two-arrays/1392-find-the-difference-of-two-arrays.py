class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:   
       arr =[]
       arr = set(nums1)-set(nums2)
       y=[]
       y = set(nums2)-set(nums1)
       res =[]
       res.append(arr)
       res.append(y)
       return res