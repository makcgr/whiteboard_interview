class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) < 2:
            return 0

        profit = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                profit += prices[i+1] - prices[i]

        return profit

#8|
#7|   *
#6|                   *
#5|           *       
#4|                       *
#3|                       
#2|               *       
#1|       *               
# |______________________________
#     1   2   3   4   5   6
#buy                  ^     
#sell                     ^

# why this works:
# 1) buy low, sell high
# 2) there is no transaction fee, so we can operate every day
# 3) if yesterday we bought lower, we can sell today
# 4) since we can do as many transactions as we can, we can immediately buy another share
#    to sell on the next day, if the next day's price will be  higher than today's as well 

print(Solution().maxProfit([7,1,5,3,6,4]))
print(Solution().maxProfit([1,2,3,4,5]))
print(Solution().maxProfit([7,6,4,3,1]))
