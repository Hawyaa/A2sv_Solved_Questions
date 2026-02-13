class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        
        while n != 1 and n not in seen:
            seen.add(n)
            
            # Calculate sum of squares of digits
            total = 0
            temp = n
            while temp > 0:
                digit = temp % 10
                total += digit * digit
                temp //= 10
            n = total
        
        return n == 1