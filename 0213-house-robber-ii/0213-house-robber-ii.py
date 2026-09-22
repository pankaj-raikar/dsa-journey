class Solution:
    def helper(self,nums,start,end):

        prev1=nums[start]
        prev2=max(nums[start+1],nums[start])
        result=prev2
        for i in range(start+2,end+1):
            result=max(prev2,prev1+nums[i])
            prev1=prev2
            prev2=result

        return result

    def rob(self, nums: list[int]) -> int:
        if len(nums)==1:
            return nums[0]
        
        if len(nums)==2:
            return max(nums[0],nums[1])

        return max(self.helper(nums,0,len(nums)-2),self.helper(nums,1,len(nums)-1))
        
        