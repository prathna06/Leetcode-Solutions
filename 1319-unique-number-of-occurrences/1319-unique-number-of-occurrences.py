class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count=0
        freq={}
        lis=[]
        for num in arr:
            if num in freq:
               freq[num] +=1
            else:
                freq[num] =1
        print(freq)
        for i in freq:
            lis.append(freq[i])
        print(lis)
        if len(lis) == len(list(set(lis))):
            return True
        else:
            return False
