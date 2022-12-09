# 35. Search Insert Positon

# Given a sorted array of distinct integers and a target value, return the index if the target is 
# found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

# Example
# Input: nums = [1,3,5,6], target = 5
# Output: 2

class Solution:
    def searchInsert(self, nums, target):
    # O(n)   
        temp = 0

        for i in nums: 

            if i >= target:

                return temp

            temp += 1
        
        return temp


class Solution1:
    def searchInsert(self, nums, target):
    # Binary Search O(log n)
        init = 0

        final = len(nums)-1

        while init <= final: 

            mid = (init + final)//2

            if target == nums[mid]: 
                return mid 
            
            if nums[mid] < target: 
                init = mid + 1
                
            else: 
                final = mid - 1
        
        return init
            



nums = [1,3,5,6]
target = 7

print(Solution().searchInsert(nums, target))
print(Solution1().searchInsert(nums, target))

