class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        garden = [0] + flowerbed + [0]
        for i in range(1,len(garden)-1):
            if garden[i-1] ==0 and garden[i] ==0 and garden[i+1] ==0:
                garden[i] =1
                n-=1
        return n<=0
