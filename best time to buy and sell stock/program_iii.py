class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        profit = 0
        LEN = len(prices)
        if LEN < 2:
            return 0
        b, s = 0, 1 # buy, sell
        
        while s <= LEN - 1:
            # find the beginning of trade (first upward trend)
            while s < LEN - 1 and prices[s] <= prices[b]: # move to upward trend beginning
                s += 1
                b += 1

            while (s < LEN - 1 
                   and prices[s] - prices[b] - fee <= 0): # update sell point to the upward trend end
                s += 1

            if prices[s] - prices[b] - fee > 0:
                profit += prices[s] - prices[b] - fee
                b = s
                s += 1
            else:
                s += 1
                b += 1
        return profit

print(Solution().maxProfit([1,3,2,8,4,9], 2))
print(Solution().maxProfit([1,3,7,5,10,3], 3))
# PRICE
# |                      9
# |              8
# |
# |
# |
# |                  4
# |      3          
# |          2      
# |  1 
# -----------------------------
#    1   2   3   4   5   6  DAY
#                    ^   ^

# Breakdown of the problem:
# 1) find beginning of upward trend (next day's price > prev day's price)
# 2) find most low, find most high, until trend changes
# needed trend change: next day's price < prev day's price

# buy low, sell high
# more deals = more profit (but only if profit is > than fee)
#   do not proceed with deal if the fee exceeds or = profit
# if trend is upward => wait for better price

# Solution (explanation):
# Two pointers: buy (left), sell (right)
# Going from left to right
# Starting with 0 for b, 1 for s

# while s <= LEN-1:
# Move to upward trend beginning (find b and s such that p[s] > p[b])
# Update sell point to the sensible selling points (sell - buy - fee > 0)
# Sell if there is profit (minding the fee), update b, s to next day (b = s, s = s + 1)
# Else update b, s to next day (+1 each)

# Pseudocode
# while s <= LEN-1:
    # while s < LEN-1 and p[s] <= [b]: # move to upward trend beginning
    #     s += 1
    #     b += 1
    ## Update sell point to the sensible selling points (sell - buy - fee > 0)
    # while s < LEN-1 and p[s]-p[b]-fee < 0:
    #   s += 1
    ## Sell if there is profit (minding the fee)
    # if p[s] - p[b] - fee > 0:
    #   profit += p[s] - p[b] - fee
    #   b, s  = s, s + 1
    # else
    #   update b, s to next day (+1 each)

