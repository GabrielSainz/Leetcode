'''
258. Add Digits

Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

Example 1:
Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.

Example 2:
Input: num = 0
Output: 0
'''

# recursion function
# AddDigits(num)
# if num // 10 == 0: return num
# temp = 0
# while num // 10 != 0: num // 10 = 3
#    temp += num % 10
#    num = num // 10
# temp += num % 10
# return AddDigits(temp)
# 

class Solution:

    def addDigitsRecursion(self, num: int) -> int:
        if num // 10 == 0: 
            return num
        
        temp = 0

        while num // 10 != 0: 
            temp += num % 10
            num = num // 10
        
        temp += num % 10

        return self.addDigitsRecursion(temp)


    def addDigits(self, num: int) -> int:
        
        while len(str(num)) != 1: 
            temp = 0

            for i in str(num): 
                temp += int(i)
            
            num = temp
        
        return num


print(Solution().addDigitsRecursion(569874123))
print(Solution().addDigits(569874123))





