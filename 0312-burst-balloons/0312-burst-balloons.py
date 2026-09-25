class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        nums=[1]+nums+[1]

        memo={}

        def dp(left,right):
            key=(left,right)

            if key in memo:
                return memo[key]
            if left>right:
                return 0

            best=0

            for k in range(left,right+1):
                left_best=dp(left,k-1)
                right_best=dp(k+1,right)
                score=nums[left-1]*nums[k]*nums[right+1]
                best=max(best,left_best+right_best+score)
            
            memo[key]=best
            return best
        
        return dp(1,len(nums)-2)



