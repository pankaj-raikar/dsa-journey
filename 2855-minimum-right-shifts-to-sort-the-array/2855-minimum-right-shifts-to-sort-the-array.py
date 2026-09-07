class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:

        pivotIdx=0
        countPivot=0
        n=len(nums)
        for i in range(1,n):
            
            if nums[i-1]>nums[i]:
                pivotIdx=i
                countPivot+=1

            if countPivot > 1:
                return -1

        if pivotIdx==0:
            return 0
        
        return -1 if nums[n-1] > nums[0] else n-pivotIdx
        