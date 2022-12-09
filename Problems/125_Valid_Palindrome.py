'''
125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase 
letters and removing all non-alphanumeric characters, it reads the same forward 
and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example: 
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
'''

class Solution:

    def isPalindrome(self, s):

        letters = "abcdefghijklmnopqrstuvwxyz"
        numbers = '0123456789'
        
        s_clean = [i.lower() for i in s if (i.lower() in letters or i in numbers)]

        return s_clean == s_clean[::-1]


    def remove_special_strings(self, s): 
        letters = "abcdefghijklmnopqrstuvwxyz"
        numbers = '0123456789'
        temp = ""

        for i in s: 
            j = i.lower()
            if (j in letters or j in numbers): 
                temp += j
        
        return temp

  
    def isPalindrome1(self, s):

        s = self.remove_special_strings(s)
        
        for i in range(len(s)//2): 

            if s[i] != s[-i-1]: 
                return False

        return True



s = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))
print(Solution().isPalindrome1(s))


