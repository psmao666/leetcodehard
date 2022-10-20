''
Problem link : https://leetcode.com/problems/divide-two-integers/

Solution:

Consider x/y=k is actually x=y*k, and we are looking for k.
Knowing that any number can be represented in binary form, then we find the biggest number g where y*(2^g) <= x
Now we just need to check the bits in range of g.

The time complexity is O(logN)
''

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1
        if dividend < 0 and divisor > 0:
            sign = -1
        elif dividend > 0 and divisor < 0:
            sign = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        tmp = divisor
        res = 0
        ans = 0
        pws = []
        while dividend >= tmp:
            pws.append(tmp)
            tmp += tmp
            ans += 1
        for i in reversed(range(ans)):
            if dividend >= pws[i]:
                dividend -= pws[i]
                res += (1<<i)
        return min(2147483647, res * sign)
            
