'''
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.


Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): return False 
        if set(s) != set(t): return False

        dic_t = {}
        dic_s = {}

        for n, m in zip(s, t): 

            if n in dic_s.keys(): 
                dic_s[n] += 1

            else: 
                dic_s[n] = 1
            

            if m in dic_t.keys(): 
                dic_t[m] += 1

            else: 
                dic_t[m] = 1

        for key in dic_t.keys(): 

            if dic_t[key] != dic_s[key]: return False

        return True

    def isAnagram1(self, s: str, t: str) -> bool:

        if len(s) != len(t): return False 
        if set(s) != set(t): return False

        for i in set(s): 
            
            if s.count(i) != t.count(i): return False

        return True




# check if len(s) == len(t)
# check if set(s) == set(t)
# make two dictionaries -> s and t 
# for loop len(s)
# compare both dictionaries

# Time Complexity -> O(len(s))


s = "anagram"
t = "nagaram"
# s = "rat"
# t = "car"
print(Solution().isAnagram(t, s))
print(Solution().isAnagram1(t, s))




