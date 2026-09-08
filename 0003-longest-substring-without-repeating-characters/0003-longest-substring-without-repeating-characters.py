class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        hashmap = {}
        n= len(s)
        l=0
        r=0
        maxLen=0

        while (r<n):
            if s[r] in hashmap:
                if hashmap[s[r]] >= l:
                    l=hashmap[s[r]]+1
            
            leng=r-l+1
            maxLen=max(leng,maxLen)
            hashmap[s[r]]=r
            r+=1
        

        return maxLen


