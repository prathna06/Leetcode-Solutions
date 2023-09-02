class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        maxCandies = max(candies)
        result=[]
        for candy in candies:
            if candy+extraCandies >= maxCandies:
                result.append(True)
            else:
                result.append(False)
        return result