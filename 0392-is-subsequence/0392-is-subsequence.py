class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        i,j=0,0
        lens=len(s)
        lent=len(t)
        while i<lens and j < lent:
            if s[i]==t[j]:
                i+=1
            j+=1
    

        return i==lens