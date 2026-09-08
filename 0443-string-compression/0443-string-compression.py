
class Solution:
    def compress(self, chars: List[str]) -> int:
        
        n=len(chars)

        idx=0
        i=0

        while(i<n):
            count=0

            curr_char=chars[i]

            while(i<n and chars[i]==curr_char):
                count+=1
                i+=1

            #now doing assingment
            chars[idx]=curr_char
            idx+=1
            if (count>1):
                count_str=str(count)

                for e in count_str:
                    chars[idx]=e
                    idx+=1

        return idx

