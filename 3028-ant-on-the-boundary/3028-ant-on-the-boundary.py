class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        
        countb=0
        sumStep=0
        for i in nums:
            sumStep+=i
            if sumStep == 0:
                countb+=1
            
        return countb