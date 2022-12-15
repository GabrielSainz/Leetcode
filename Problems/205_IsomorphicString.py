'''
205. Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of 
characters. No two characters may map to the same character, but a character may map to itself.


Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:

Input: s = "foo", t = "bar"
Output: false

'''

# build a dictionary for s -> {0: [0], 1:[2,3]}
# build a dictionary for t -> {0: [0], 1:[2,3]}
# compare both dictionaries

def is_isomorphic(s, t): 

    if len(s) != len(t): 
        return False

    dic_s = {}
    dic_t = {}

    for i in range(len(s)): 
        
        if (s[i] not in dic_s.keys()) and (t[i] not in dic_t.keys()): 
            dic_s[s[i]] = t[i]
            dic_t[t[i]] = s[i]

        elif (s[i] not in dic_s.keys()) or (t[i] not in dic_t.keys()): 
            return False

        elif (dic_s[s[i]] == t[i]) and (dic_t[t[i]] == s[i]): 
            pass

        else: 
            return False

        if (dic_s[s[i]] != t[i]) or (dic_t[t[i]] != s[i]): 
            return False

    return True

# O(n) -> n = len(s)



def is_isomorphic1(s, t): 

    if len(s) != len(t): 
        return False

    dic_s = {}
    dic_t = {}

    for i, j in zip(s, t): 

        if (i not in dic_s.keys()) and (j not in dic_t.keys()): 
            dic_s[i] = j
            dic_t[j] = i
        
        elif dic_s.get(i) != j or dic_t.get(j) != i: 
            return False

    return True


s ="foo"
t ="add"

print(is_isomorphic(s, t))
print(is_isomorphic1(s, t))