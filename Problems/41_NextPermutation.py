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

for i in [[8,7,6,8,11,7,10,9,8,7,6,5],[7,6,8,5,2,10,12,7,8,1],[8,12,1,7,8,13,7,8,6,7,5,1,2,8],[9,10,8,7,6,5,4,3,2,1],[9,8,7,6,5,4,3,2,1],[6,6,6,6,6]]: 
    print('---------------------')
    print(i)
    print(Solution().nextPermutation(i))









