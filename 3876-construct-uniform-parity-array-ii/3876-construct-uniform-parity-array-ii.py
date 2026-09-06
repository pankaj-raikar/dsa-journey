class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        minNum=min(nums1)

        if minNum%2==1:
            return True
        
        for val in nums1:
            if val%2==1:
                return False
            

        return True

        