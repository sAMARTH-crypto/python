#reverse of a no.


   class Solution:
   
    def reverse(self, x: int) -> int:
    
        isNegative = x < 0
        x = abs(x)
        reversed = 0
       
        while x!= 0 :
            reversed  = reversed * 10 + x % 10
            x //= 10
        if reversed > 2**31-1 :
            return 0
        else:
            return reversed if not isNegative else -reversed
