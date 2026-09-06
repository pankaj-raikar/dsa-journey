class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n=len(nums)
        
        minIdx=nums.index(min(nums))
        maxIdx=nums.index(max(nums))

        left=min(minIdx,maxIdx)
        right=max(maxIdx,minIdx)

        return min((left+1+n-right),(n-left),(right+1))


