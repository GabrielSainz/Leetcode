# 66. Plus One


# You are given a large integer represented as an integer array digits, where each digits[i] is the 
# ith digit of the integer. The digits are ordered from most significant to least significant in 
# left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

class Solution:
    def plusOne(self, digits):

        for i in range(len(digits)): 

            if digits[-i-1] != 9:

                digits[-i-1] += 1

                return digits

            else: 
                digits[-i-1] = 0
        
        temp = [1]

        temp.extend(digits)

        return temp


nums = [9]
print(nums)
print(Solution().plusOne(nums))

print(55//10)