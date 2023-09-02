class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        counter =0
        i=0
        while(i<len(flowerbed)):
            if flowerbed[i] != 1 :
                if i != len(flowerbed)-1:
                    if flowerbed[i+1] != 1:
                        if i > 0  and flowerbed[i-1] != 1:
                            counter+=1
                            i +=2
                        elif i == 0:
                            counter +=1
                            i +=2
                        
                        else:
                            i +=1
                    else:
                        i +=1
                else:
                    if i > 0  and flowerbed[i-1] != 1:
                        counter+=1
                        i +=2
                    elif i == 0:
                        counter +=1
                        i +=2
                    
                    else:
                        i +=1


            else:
                i +=1

        if n <= counter:
            return True
        else:
            return False
        