class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        pos=1

        for val in nums:

            last_unique=nums[pos-1]
            if val!=last_unique:
                nums[pos]=val
                pos+=1
            
        return pos
        