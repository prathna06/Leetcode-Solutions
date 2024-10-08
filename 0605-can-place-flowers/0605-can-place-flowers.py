class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count =0
        for i in range(len(flowerbed)):
            if len(flowerbed)==1 and flowerbed[0]==0:
                flowerbed[i]="*"
                return True
            if n==0:
                return True
            if flowerbed[0]==0 and flowerbed[1]==0:
                count +=1
                print("hey1")
                flowerbed[0]="*"
                if count >= n:
                    return count
                else:
                    continue
                
            elif flowerbed[i]==0 and flowerbed[i-1]==0 and flowerbed[i+1]==0:
                count +=1
                flowerbed[i]="*"
                print("hey2")
                if count >= n:
                    return count
                else:
                    continue
                
            elif flowerbed[-1]==0 and flowerbed[-2]==0:
                count +=1
                flowerbed[-1]="*"
                print("hey3")
                if count >= n:
                    return count
                else:
                    continue
            
            
        
         