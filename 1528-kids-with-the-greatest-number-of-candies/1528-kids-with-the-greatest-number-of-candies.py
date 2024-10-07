class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        newArr=[] 
        highestCandy= max(candies)
        for i in candies:    
            if i +extraCandies >= highestCandy:
                newArr.append(True)
            else:
                newArr.append(False)
        return newArr

        

