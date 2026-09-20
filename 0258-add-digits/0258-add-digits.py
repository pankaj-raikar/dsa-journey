class Solution:
    def addDigits(self, num: int) -> int:

        run=True
        while(run):
            sum=0
            for i in str(num):
                sum+=int(i)
            
            num=sum
            if sum>=0 and sum<=9:
                return num



        