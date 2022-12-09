'''
121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on 
the ith day.

You want to maximize your profit by choosing a single day to buy one stock and 
choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot 
achieve any profit, return 0.

'''

class Solution:

    def maxProfit(self, prices):
        '''
        brute force
        '''
        
        res = 0

        for i in range(len(prices)): 
    
            for j in range(i,len(prices)): 

                if res <= prices[j] - prices[i]: 

                    res = prices[j] - prices[i]
        
        return res


    def maxProfit1(self, prices):

        j, h = prices[0], prices[0]
        temp_j, temp_h = 0, 0
        res = 0

        for i in prices: 
            
            temp_j = i - j

            if res < temp_j: res = temp_j

            if i < j and i < h:
                h = i
            
            temp_h = i - h

            if res < temp_h: 
                j = h
                res = temp_h

        return res


import random

list_prices = [[random.randint(0,100) for _ in range(20)] for _ in range(1000)]

print(sum([Solution().maxProfit1(prices) == Solution().maxProfit(prices) for prices in list_prices]))

# print(prices)

# print(Solution().maxProfit(prices))
# print(Solution().maxProfit2(prices))