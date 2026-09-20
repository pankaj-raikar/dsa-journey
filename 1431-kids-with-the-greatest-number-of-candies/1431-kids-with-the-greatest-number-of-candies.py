class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        maxCandies=max(candies)
        n=len(candies)
        for i in range(n):
            if candies[i]+extraCandies>=maxCandies:
                candies[i]=True
            else:
                candies[i]=False
            
        return candies