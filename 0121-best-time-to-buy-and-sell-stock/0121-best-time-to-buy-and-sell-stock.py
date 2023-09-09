class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right=1
        profit=0
        maxProfit =0
        while (right < len(prices)) :
            if prices[left] < prices[right]:
                profit = prices[right]-prices[left]
                maxProfit = max(maxProfit,profit)
                
            else:                  
                left =right
            right +=1
                
        print(maxProfit)
        return maxProfit


        



        