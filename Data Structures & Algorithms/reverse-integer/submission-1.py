class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2**31 - 1
        MIN = -2**31
        
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        res = 0
        
        while x != 0:
            digit = x % 10
            x //= 10
            
            # overflow check BEFORE update
            if res > MAX // 10 or (res == MAX // 10 and digit > 7):
                return 0
            
            res = res * 10 + digit
        
        return sign * res