# 46. Permutations

# Given an array nums of distinct integers, return all the possible permutations. 
# You can return the answer in any order.

from math import factorial
from unittest import result


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
        temp = Solution().reduction_list(nums)

        while len(temp) != 1:
            len_temp = len(temp)
            temp = Solution().reduction_list(temp, 1)
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
    
    def permute(self, nums):
        temp = self.nextPermutation(nums)
        permutations = [temp]
        
        while temp != nums: 
            temp = self.nextPermutation(temp)
            permutations.append(temp)
        
        return permutations


# nums = [1]

# print(Solution().permute(nums))

class OtherSolution:

    def permute(self, nums):
        temp = []
        if len(nums) == 1: 
            return [nums[:]]

        for i in set(nums): 
            temp_nums = nums[:]
            temp_nums.remove(i)
            for sub_perm in self.permute(temp_nums): 
                temp.extend([[i] + sub_perm])    

        return temp


b = [1,1,1,1]

print(OtherSolution().permute(b))

class OtherSolution2:

    def permute(self, nums):
        result = []

        if (len(nums) == 1): 
            return [nums[:]]

        for i in range(len(nums)): 
            n = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms: 
                perm.append(n)
            
            result.extend(perms)
            nums.append(n)
            
        return result


print(OtherSolution2().permute(b))
