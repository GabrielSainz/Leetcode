'''
119. Pascal's Triangle II

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's 
triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above 
it as shown:


Example:

Input: rowIndex = 3
Output: [1,3,3,1]

'''

class Solution:
    def getRow(self, rowIndex):
        last_row = [1]
        new_row = [0] + last_row + [0]
        res = []

        for j in range(rowIndex): 

            for i in range(len(new_row)-1):

                res.append(new_row[i] + new_row[i+1])

            last_row = res.copy()
            new_row = [0] + last_row + [0]
            res = []
        
        return last_row


rowIndex = 0

print(Solution().getRow(rowIndex))