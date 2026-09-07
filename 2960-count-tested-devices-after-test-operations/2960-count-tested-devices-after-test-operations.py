class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        testedCount=0
        n=len(batteryPercentages)
        for i in range(n):
            
            if batteryPercentages[i]>0:
                testedCount+=1
                for j in range(i+1,n):
                    if batteryPercentages[j]>0:
                        batteryPercentages[j]-=1
                
        
        return testedCount

        