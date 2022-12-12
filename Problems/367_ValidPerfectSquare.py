'''
367. Valid Perfect Square

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.


Example 1: 
Input: num = 16
Output: true

Example 2: 
Input: num = 14
Output: false
'''

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # print(num)

        if num == 1: return True

        lim_inf = 1
        lim_sup = num // 2

        while True: 

            med = (lim_inf + lim_sup)//2
            sq_inf = lim_inf * lim_inf
            sq_sup = lim_sup * lim_sup
            sq_med = med * med

            if (sq_inf == num) or (sq_sup == num) or (sq_med == num): 
                return True

            elif (sq_inf > num) or (lim_inf == lim_sup) or (lim_inf > lim_sup): 
                return False

            elif (sq_med > num): 
                lim_inf += 1
                lim_sup = med - 1
            
            else: 
                lim_inf = med + 1
                lim_sup -= 1


print(Solution().isPerfectSquare(25**2))

dic = {i: Solution().isPerfectSquare(i) for i in range(7, 1001)}
print(dic)


