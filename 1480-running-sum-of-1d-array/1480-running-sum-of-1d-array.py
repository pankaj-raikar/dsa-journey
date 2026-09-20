class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        
        i=1
        n=len(nums)
        while i<n:
            nums[i]+=nums[i-1]
            i+=1

        return nums



        