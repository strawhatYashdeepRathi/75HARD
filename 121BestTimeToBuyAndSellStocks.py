
# Stock Buy And Sell
# Problem Statement: You are given an array of prices where prices[i] is the price of a given stock on an ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Examples
# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and 
# sell on day 5 (price = 6), profit = 6-1 = 5.


def maxProfit(prices):
    max_p = 0
    mini_day = float('inf')
    for i in range(len(prices)):
        if prices[i] - mini_day <= 0:
            mini_day = prices[i]
        max_p = max(max_p, prices[i]-mini_day)
    return max_p





arr = [7, 1, 5, 3, 6, 4]
maxPro = maxProfit(arr)
print("Max profit is:", maxPro)

