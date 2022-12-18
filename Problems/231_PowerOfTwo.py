'''
231. Power of Two

Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2**x.

Example 1:
Input: n = 1
Output: true
Explanation: 2**0 = 1

Example 2:
Input: n = 16
Output: true
Explanation: 2**4 = 16

Example 3:
Input: n = 3
Output: false

Follow up: Could you solve it without loops/recursion?
'''

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0: return False

        temp = 1

        while temp < n: 
            temp *= 2

        return temp == n
        
    def isPowerOfTwo1(self, n: int) -> bool:
        if n <= 0: return False

        return (n & (n-1)) == 0
        
        

# O(log2(n)) time complexity


# define temp = 1
# while temp <= n: 
#   temp *= 2
# if temp == n: return True
# else: False



n = 4
print(Solution().isPowerOfTwo(n))
print(Solution().isPowerOfTwo1(n))

print(2 & 1)



