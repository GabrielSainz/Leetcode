'''
118. Pascal's Triangle

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

'''


class Solution:
    def generate(self, numRows):

        output = []
        temp = []

        for i in range(numRows+1): 

            for j in range(i): 
                if (j == 0) or (j == i-1): 
                    temp.append(1)

                else: 
                    nxt = output[-1][j-1] + output[-1][j]
                    temp.append(nxt)
            
            output.append(temp)
            temp = []

        return output[1:]

    def generate_ytv(self, numRows):
        res = [[1]]

        for i in range(numRows - 1): 
            temp = [0] + res[-1] + [0]
            row = []

            for j in range(len(res[-1]) + 1): 
                row.append(temp[j] + temp[j+1])
            
            res.append(row)

        return res





numRows = 10
print(Solution().generate(numRows))
print(Solution().generate_ytv(numRows))
