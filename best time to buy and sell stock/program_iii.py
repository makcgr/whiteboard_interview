class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        cash = 0            # pocket 1: "cash" (how much money if we are NOT holding stock)
        hold = -prices[0]   # pocket 2: "hold" (how much money if we ARE holding stock) 
                            # NOTE: why -prices[0]: we BORROWED these money to hold stock

        for price in prices[1:]:
            cash = max(cash, hold + price - fee) # “If I want to have NO stock today, what’s my best move?”
            hold = max(hold, cash - price)      # “If I want to HAVE stock today, what’s my best move?”
        return cash


print(Solution().maxProfit([1,3,2,8,4,9],2))


# why this works:
# - every we ask two questions: 
#      1) “If I want to have NO stock today, what’s my best move?”
#      2) “If I want to HAVE stock today, what’s my best move?
# - each day we track best possible wealth in each situation, using previous day's decision
