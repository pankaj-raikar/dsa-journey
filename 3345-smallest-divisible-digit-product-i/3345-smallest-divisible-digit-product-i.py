class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

        def findDigitProduct(num):
            if num == 0:
                return 0
            
            num = abs(num)
            product = 1
            
            while num > 0:
                last_digit = num % 10
                product *= last_digit
                num //= 10
                
            return product
        
        prod=0
        while True:
            prod=findDigitProduct(n)
            print(prod)
            if prod % t==0:
                break
            n+=1

        return n
        