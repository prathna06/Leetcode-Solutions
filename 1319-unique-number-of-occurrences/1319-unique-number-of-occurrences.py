class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        set1 = list(set(arr))
        arr1=[]
        for i in range(0,len(set1)):
            arr1.append(arr.count(set1[i]))
        if(len(set1) == len(set(arr1))):
            return True
        else:
            return False
