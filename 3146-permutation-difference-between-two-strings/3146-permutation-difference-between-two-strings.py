class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        sum=0

        n=len(s)

        for i in range(n):
            for j in range(n):
                if s[i]==t[j]:
                    sum+=abs(i-j)
                

        return sum