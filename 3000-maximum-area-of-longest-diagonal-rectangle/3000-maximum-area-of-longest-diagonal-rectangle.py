class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        maxDia=0
        res=0

        for a,b in dimensions:
            val=(a**2 + b**2) ** 0.5
            print("currrent val->",val," maxDia-->",maxDia,"res-->",res)
            if val > maxDia:
                maxDia=val
                res=(a*b)
            elif val==maxDia:
                res=max(a*b,res)



        return res

        