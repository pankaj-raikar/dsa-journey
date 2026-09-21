class Solution:
    def maxPower(self, s: str) -> int:
        currEle=s[0]
        count=1
        maxCount=1
        for i in s[1:]:
            if currEle==i:
                count+=1
                maxCount=max(count,maxCount)
            else:
                count=1
                currEle=i
            
        return maxCount
                

