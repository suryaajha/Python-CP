weights = [1, 2, 3]
values = [10, 15, 40]
max_weight = 6

memo = [[0 for _ in range(max_weight + 1)] for _ in range(len(values) + 1)]

for row in range(1, len(values) + 1):
    for col in range(1, max_weight + 1):
        choosed = 0
        if weights[row - 1] <= col:
            choosed = values[row - 1] + memo[row - 1][col - weights[row - 1]]
        memo[row][col] = max(choosed, memo[row - 1][col]) 

print(memo)
print(memo[len(values)][max_weight])