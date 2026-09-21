class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:

        res=[]
        
        for i in range(left,right+1):
            canAdd=True
            for j in str(i):
                if int(j)==0 or (i % int(j) != 0):
                    canAdd=False
                    break
            
            if canAdd:
                res.append(i)
            
        return res
                    