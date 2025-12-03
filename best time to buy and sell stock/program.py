def maxProfit(prices: list[int]) -> int:
    if len(prices) == 1:
        return 0

    profit = 0
    b, s = 0, 1 # buy, sell indexes
    for i, p in enumerate(prices):
        # sell
        if i > 0 and p >= prices[s]:
            s = i
            profit = max(profit, prices[s] - prices[b])
        # buy
        if p < prices[b]:
            b = i
            s = i+1 

    return profit

def maxProfit2(prices: list[int]) -> int:
    if len(prices) == 1:
        return 0

    profit = 0 # profit
    buy, sell = prices[0], prices[1]
    for p in prices[1:]:
        if p >= sell:
            sell = p
            profit = max(profit, sell - buy)
        if p < buy:
            buy = p
            sell = 0

    return profit

def maxProfit3(prices: list[int]) -> int:
    profit = 0
    buy = prices[0]
    for p in prices:
        buy = min(p, buy)
        profit = max(profit, p - buy)
    return profit

# tests
for prices in [[7,1,5,3,6,4], [7,6,4,3,1], [3,3,5,0,0,3,1,4]]:
    print(maxProfit(prices))
    print(maxProfit2(prices))
    print(maxProfit3(prices))

# Why it works:
# The key to the solution is understanding 
#    - the "sell" must always come after "buy"
#    - the iterative nature of the solution helps us with that (start "sell" from 2nd elem on)
#    - we can do max(profit, "current price" - buy) to find max profit

# Debugging
# ex [7,1,5,3,6,4]

# profit=4

# i=7 p=4
# 0: - 1: - 2: 5>=3,s=2,pr=max(0,5-3)=2 :3 b=3 4: - 5: max(2,3-0)=3 
# 6: - 7: max(3,4)=4

#  [3,3,5,0,0,3,1,4]
#                 ^
#         b       s

