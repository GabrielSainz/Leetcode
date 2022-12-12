'''
136. Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example: 
Input: nums = [2,2,1]
Output: 1

Example: 
Input: nums = [4,1,2,1,2]
Output: 4
'''



class Solution:
    def singleNumber(self, nums) -> int:
        
        dic = {True: [], 
               False: []}

        for i in nums: 

            if i in dic[False]: 
                dic[True].append(i)
                dic[False].remove(i)
            else: 
                dic[False].append(i)

        return dic[False][0]

    def singleNumber1(self, nums) -> int:
        
        single = []

        for i in nums: 

            if i in single: 
                single.remove(i)
            else: 
                single.append(i)

        return single[0]

    def singleNumber2(self, nums) -> int:
        
        res = 0 # xor operator -> num ^ 0 = num

        for i in nums: 
            res = i ^ res

        return res

    def singleNumber3(self, nums) -> int:
        # with dictionaries
        
        dic = {}

        for i in nums: 

            if i not in dic: 
                dic[i] = 1
            else: 
                del dic[i]

        return list(dic.keys())[0]



nums = [1]
print(Solution().singleNumber3(nums))


print(1 ^ 2)
