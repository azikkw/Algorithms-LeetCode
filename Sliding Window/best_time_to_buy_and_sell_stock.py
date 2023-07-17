def max_profit(prices):
    l, r = 0, 1
    res = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            sum = prices[r] - prices[l]
            res = max(res, sum)
        else:
            l = r

        r += 1

    return res

print(max_profit([1, 2]))
