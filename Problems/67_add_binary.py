# 67. Add Binary
# Given two binary strings a and b, return their sum as a binary string. 

# Example 1: 
# Input: a = "11", b = "1"
# Output: b: "100"

from typing import *

class Solution:
    def binary_to_decimal(self,num): 

        return sum([int(i)*2**k for (k,i) in enumerate(num[::-1])])


    def decimal_to_binary(self,num): 
        
        res = ''

        while num != 0: 
            res = res + str(num % 2)
            num = num//2

        return res[::-1]


    def addBinary(self, a: str, b: str) -> str:

        num1, num2 = self.binary_to_decimal(a), self.binary_to_decimal(b)
        
        if num1 + num2: 
            return self.decimal_to_binary(num1 + num2)
        else: 
            return "0"
            
    def addBinary1(self, a: str, b: str) -> str:
        res = ""
        carry = 0

        a, b = a[::-1], b[::-1]

        for i in range(max(len(a), len(b))): 
            digitA = ord(a[i]) - ord("0") if i < len(a) else 0 
            digitB = ord(b[i]) - ord("0") if i < len(b) else 0 

            total = digitA + digitB + carry
            char = str(total % 2)
            res = char + res
            carry = total//2

        if carry: 
            res = "1" + res
        return res



num1 = "1010011"
num2 = "1011001111000"

print(Solution().addBinary(num1, num2))
print(Solution().addBinary1(num1, num2))