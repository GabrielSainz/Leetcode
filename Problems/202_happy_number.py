'''
202. Happy Number

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares 
of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops 
endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''


class Solution:
    def isHappy(self,n):

        temp = n
        temp1 = 0
        first = [1, n]

        while True: 

            temp1 = 0

            while temp != 0: 
                temp1 += (temp % 10)**2
                temp = temp // 10

            temp = temp1
            
            if temp in first: 
                break

            first.append(temp)

        return temp == 1


n = 3
print(Solution().isHappy(n))


happy_numbers = {i: Solution().isHappy(i) for i in range(1, 101)}
print(happy_numbers)
