class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        arr1=[]
        arr2 =[]

        for i in set1:
            if i not in set2:
                arr1.append(i)
        for j in set2:
            if j not in set1:
                arr2.append(j)
        return [arr1,arr2]