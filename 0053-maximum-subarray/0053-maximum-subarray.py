class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxSum=float(-inf)

        sumTemp=0

        for val in nums:
            sumTemp+=val
            maxSum=max(sumTemp,maxSum)
            if sumTemp<0:
                sumTemp=0

        return maxSum
        