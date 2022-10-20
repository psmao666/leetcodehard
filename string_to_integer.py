'''
Problem Link: https://leetcode.com/problems/string-to-integer-atoi/

Solution:

Just implementation, except very annoying side cases
'''

class Solution:
    def myAtoi(self, s: str) -> int:
        ans = 0
        gotNumber = False
        gotSign = False
        sign = 1
        exceeded = False
        gotAnything = False
        for ch in s:
            if ch == ' ' and gotAnything == False:
                continue
            elif gotAnything == False:
                if ch != '-' and ch != '+' and (ch < '0' or ch > '9'):
                    break
                gotAnything = True
            
            if ch == '-':
                if gotNumber == True or gotSign == True:
                    break
                sign = -1
                gotSign = True
            elif ch == '+':
                if gotNumber == True or gotSign == True:
                    break
                sign = 1
                gotSign = True
            elif ch >= '0' and ch <= '9':
                ans = ans * 10 + int(ch) - int('0')
                gotNumber = True
                if ans > 2**31-1:
                    exceeded = True
                    ans = 2**31-1
            else:
                break
        ans = ans * sign
        if exceeded == True and sign == -1:
            ans = (-2)**31
        return ans
