# 31. Next Permutation
# For example, for arr = [1,2,3], the following are all the permutations of arr: 
#       [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
# The next permutation of an array of integers is the next lexicographically 
# greater permutation of its integer. More formally, if all the permutations of 
# the array are sorted in one container according to their lexicographical order, 
# then the next permutation of that array is the permutation that follows it in the 
# sorted container. If such arrangement is not possible, the array must be 
# rearranged as the lowest possible order (i.e., sorted in ascending order).

# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does 
# not have a lexicographical larger rearrangement.
# Given an array of integers nums, find the next permutation of nums.

# The replacement must be in place and use only constant extra memory.

class Solution:
    def reduction_list(self, nums, n = 0): 
        max_num = max(nums[n:])
        return nums[n:][nums[n:].index(max_num):]

    def nextPermutation(self, nums):
        """
        Return the result
        """
        if not nums: 
            return nums
        i = 0
        temp = self.reduction_list(nums)

        while len(temp) != 1:
            len_temp = len(temp)
            temp = self.reduction_list(temp, 1)
            if len_temp == len(temp) + 1: 
                i += 1
            else: 
                i = 0

        sub_nums = nums[-(i + 2):]

        temp_num = sub_nums[0]
        min_num = 0
        for j in sub_nums[1:]: 
            temp = j-sub_nums[0]
            if (temp > 0) & (j != sub_nums[0]):
                min_temp = min(temp, temp_num)
                temp_num = j

        if sub_nums.index(temp_num) == 0: 
            result = sub_nums
            result.sort()
            nums = result
        else: 
            a = sub_nums[:sub_nums.index(temp_num)] + sub_nums[sub_nums.index(temp_num)+1:]
            a.sort()
            result = nums[:-(i + 2)] + [temp_num] + a
            nums = result

        return result

class Solution1:
    def reduction_list(self, nums, n = 0): 
        max_num = max(nums[n:])
        return nums[n:][nums[n:].index(max_num):]

    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums: 
            return nums
        i = 0
        temp = self.reduction_list(nums)

        while len(temp) != 1:
            len_temp = len(temp)
            temp = self.reduction_list(temp, 1)
            if len_temp == len(temp) + 1: 
                i += 1
            else: 
                i = 0

        sub_nums = nums[-(i + 2):]

        temp_num = sub_nums[0]
        min_num = 0
        for j in sub_nums[1:]: 
            temp = j-sub_nums[0]
            if (temp > 0) & (j != sub_nums[0]):
                min_temp = min(temp, temp_num)
                temp_num = j

        if sub_nums.index(temp_num) == 0: 
            nums[:] = sub_nums[:]
            nums.sort()
        else: 
            a = sub_nums[:sub_nums.index(temp_num)] + sub_nums[sub_nums.index(temp_num)+1:]
            a.sort()
            result = nums[:-(i + 2)] + [temp_num] + a
            nums[:] = result[:]


class OtherSolution:
    
    def nextPermutation(self, nums):
        """
        Return the result
        """
        flag = False
        temp = nums[-1]
        for i, num in enumerate(nums[::-1]): 
            
            if temp > num: 
                position = i
                temp = num
                flag = True
                break
                
            temp = num
            position = i
        
        for i, num in enumerate(nums[::-1][:position]): 
            if num-temp >0: 
                nums[len(nums)-position-1],nums[len(nums)-i-1] = nums[len(nums)-i-1],nums[len(nums)-position-1]
                break
        
        if flag: 
            nums[-position:] = nums[-position:][::-1]
        else: 
            nums[::] = nums[::-1]



class YoutubeSolution: 
    def nextPermutation(self, nums): 
        lenght = len(nums)
        if lenght <=2: 
            return nums.reverse()
        pointer = lenght -2

        while pointer >= 0 and nums[pointer] >= nums[pointer+1]: 
            pointer -= 1
        
        if pointer == -1: 
            return nums.reverse()
        
        for x in range(lenght-1, pointer, -1): 
            if nums[pointer] < nums[x]:
                nums[pointer], nums[x] = nums[x], nums[pointer]
                break
        
        nums[pointer + 1: ] = reversed(nums[pointer + 1:])


# ---------------------------------- SPEED TEST ----------------------------------

import random 
import cProfile
import timeit
import numpy as np

n = 1_000_000
test = True

# SOLUTION
import_module = "import random"

testcode = '''

class Solution1:
    def reduction_list(self, nums, n = 0): 
        max_num = max(nums[n:])
        return nums[n:][nums[n:].index(max_num):]

    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums: 
            return nums
        i = 0
        temp = self.reduction_list(nums)

        while len(temp) != 1:
            len_temp = len(temp)
            temp = self.reduction_list(temp, 1)
            if len_temp == len(temp) + 1: 
                i += 1
            else: 
                i = 0

        sub_nums = nums[-(i + 2):]

        temp_num = sub_nums[0]
        min_num = 0
        for j in sub_nums[1:]: 
            temp = j-sub_nums[0]
            if (temp > 0) & (j != sub_nums[0]):
                min_temp = min(temp, temp_num)
                temp_num = j

        if sub_nums.index(temp_num) == 0: 
            nums[:] = sub_nums[:]
            nums.sort()
        else: 
            a = sub_nums[:sub_nums.index(temp_num)] + sub_nums[sub_nums.index(temp_num)+1:]
            a.sort()
            result = nums[:-(i + 2)] + [temp_num] + a
            nums[:] = result[:]

i = [random.randint(0, 100) for i in range(20)]
Solution1().nextPermutation(i)
'''

if test: 
    print("Solution1: ")
    print(timeit.timeit(stmt=testcode, setup=import_module, number=n))

# OTHER SOLUTION

import_module = "import random"

testcode = '''
class OtherSolution:
    
    def nextPermutation(self, nums):
        """
        Return the result
        """
        flag = False
        temp = nums[-1]
        for i, num in enumerate(nums[::-1]): 
            
            if temp > num: 
                position = i
                temp = num
                flag = True
                break
                
            temp = num
            position = i
        
        for i, num in enumerate(nums[::-1][:position]): 
            if num-temp >0: 
                nums[len(nums)-position-1],nums[len(nums)-i-1] = nums[len(nums)-i-1],nums[len(nums)-position-1]
                break
        
        if flag: 
            nums[-position:] = nums[-position:][::-1]
        else: 
            nums[::] = nums[::-1]

i = [random.randint(0, 100) for i in range(20)]
OtherSolution().nextPermutation(i)
'''

if test: 
    print("OtherSolution: ")
    print(timeit.timeit(stmt=testcode, setup=import_module, number=n))


# YOUTUBE SOLUTION

import_module = "import random"

testcode = '''
class YoutubeSolution: 
    def nextPermutation(self, nums): 
        lenght = len(nums)
        if lenght <=2: 
            return nums.reverse()
        pointer = lenght -2

        while pointer >= 0 and nums[pointer] >= nums[pointer+1]: 
            pointer -= 1
        
        if pointer == -1: 
            return nums.reverse()
        
        for x in range(lenght-1, pointer, -1): 
            if nums[pointer] < nums[x]:
                nums[pointer], nums[x] = nums[x], nums[pointer]
                break
        
        nums[pointer + 1: ] = reversed(nums[pointer + 1:])

i = [random.randint(0, 100) for i in range(20)]
YoutubeSolution().nextPermutation(i)
'''

if test: 
    print("YoutubeSolution: ")
    print(timeit.timeit(stmt=testcode, setup=import_module, number=n))


