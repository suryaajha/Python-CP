import math

def min_coins(n, denominations):
    memo = [math.inf for _ in range(n + 1)]
    memo[0] = 0
    print(memo)
    for v in range(1, n + 1):
        for denomination in denominations:
            if denomination > v:
                continue
            memo[v] = min(memo[v], memo[v - denomination] + 1)
    print(memo)
    return memo[n]

denominations = [2, 1]
n = 7


print(min_coins(n, denominations))
