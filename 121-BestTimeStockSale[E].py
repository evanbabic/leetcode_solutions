# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

#1. My initial solution (brute force)

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pairs = []

        for i in range(len(prices)):
            for j in range(i, len(prices)):
                if prices[j] > prices[i]:
                    pairs.append([prices[i], prices[j]])
        print(pairs)
        max_profit = 0

        for k in range(len(pairs)):
            if (pairs[k][1] - pairs[k][0] > max_profit):
                max_profit = pairs[k][1] - pairs[k][0]
        
        return max_profit

#2. More optimal solution:

class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price

            profit = price - min_price

            if profit > max_profit:
                max_profit = profit
        
        return max_profit
