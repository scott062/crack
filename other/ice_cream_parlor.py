def ice_cream_parlor(prices, money):
    for i in range(len(prices)):
        if prices[i] >= money:
            continue
        diff = money - prices[i]
        try:
            j = prices.index(diff, i)
            if j >= 0:
                return [i,j]
        except ValueError:
            continue

print(ice_cream_parlor([3, 20, 10, 4], 6))
