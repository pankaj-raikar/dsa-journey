class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        count=0
        arr=[]
        for i,val in sorted(enumerate(nums),key=lambda x:x[1] ,reverse=True):
            arr.append((i,val))
            count+=1
            if count==k:
                break
        
        arr.sort()
        return [val for i,val in arr]



        