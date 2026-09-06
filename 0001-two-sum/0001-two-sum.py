class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        n=len(nums)

        for i,val in enumerate(nums):
            cal=target-val
            if cal in seen:
                return [seen[cal],i]
            else:
                seen[val]=i
        