def solve():
    max_weight, list_of_weight_and_value = read()
    result = think(max_weight, list_of_weight_and_value)
    write(result)
 
 
def read():
    n, max_weight = read_int(2)
    list_of_weight_and_value = []
    for i in range(n):
        list_of_weight_and_value.append(read_int(2))
    return max_weight, list_of_weight_and_value
 
 
def read_int(n):
    return list(map(lambda x: int(x), read_line().split(' ')))[:n]
 
 
def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]
 
 
def think(max_weight, list_of_weight_and_value):
    MAX_WEIGHT = 10 ** 5
    MAX_N = 100
    INVALID_VALUE = MAX_WEIGHT * MAX_N + 1
 
    # dp[w] means max value at total weight 'w'
    dp = [INVALID_VALUE for x in range(max_weight + len(list_of_weight_and_value) + 1)]
    dp[0] = 0
 
    for weight, value in list_of_weight_and_value:
        for i in range(len(dp) - 1, -1, -1):
            if dp[i] != INVALID_VALUE and i + weight < len(dp):
                if dp[i + weight] == INVALID_VALUE:
                    dp[i + weight] = dp[i] + value
                else:
                    dp[i + weight] = max(dp[i + weight], dp[i] + value)
    return max(filter(lambda x: x != INVALID_VALUE, dp[:max_weight + 1]))
 
 
def write(result):
    print(result)
 
 
if __name__ == '__main__':
    solve()