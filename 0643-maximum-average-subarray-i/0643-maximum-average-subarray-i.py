class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:

        n=len(nums)

        windowSum=sum(nums[:k])
        maxSum=windowSum

        for r in range(k,n):
            windowSum+=nums[r]
            windowSum-=nums[r-k]

            maxSum=max(maxSum,windowSum)
        
        return maxSum/k