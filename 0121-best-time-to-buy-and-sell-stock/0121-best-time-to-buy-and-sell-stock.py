class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)

        maxProfit=0
        bestBuy=prices[0]
        for i in range(1,n):
            val=prices[i]-bestBuy
            maxProfit=max(maxProfit,val)
            bestBuy=min(bestBuy,prices[i])
            

            
        
        return maxProfit
                
