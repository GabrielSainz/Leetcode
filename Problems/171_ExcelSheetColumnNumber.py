'''
171. Excel Sheet Column Number 

Given a string columnTitle that represents the column title as appears in an Excel 
sheet, return its corresponding column number.

For example:
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
'''


class Solution:
    def titleToNumber(self, columnTitle):
        abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        dic_abc = {j: i+1 for (i, j) in enumerate(abc)}

        res = 0

        for i, n in enumerate(columnTitle[::-1]): 
            
            res += (26**i)*dic_abc[n]
        
        return res

    def titleToNumber1(self, columnTitle):

        res = 0

        for i, n in enumerate(columnTitle[::-1]): 
            
            res += (26**i)* (ord(n) - ord('A') + 1)
        
        return res


columnTitle = "FXSHRXW"
print(Solution().titleToNumber(columnTitle))
print(Solution().titleToNumber1(columnTitle))
