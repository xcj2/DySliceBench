def solve():
    n = int(input())
    dp = [0 for _ in range(n+1)] 

    for i in range(1, n+1):
        options = find_options(i)
        selected = min(map(lambda x: [x, dp[i - x]], options), key=lambda x: x[1])
        dp[i] = selected[1] + 1

    print(dp[n])

def find_options(n):
    sixs = find_sixs(n)
    nines = find_nines(n)
    options = [1]
    options.extend(sixs)
    options.extend(nines)
    return options


def find_sixs(n):
    sixs = 1
    powers = [] 
    count = 0
    while n > sixs:
        count += 1
        sixs *= 6
        powers.append(sixs)
    
    if sixs == n:
        return powers
    else:
        powers.pop()
    return powers

def find_nines(n):
    nines = 1
    powers = [] 
    count = 0
    while n > nines:
        count += 1
        nines *= 9
        powers.append(nines)
    
    if nines == n:
        return powers
    else:
        powers.pop()
    return powers

if __name__ == "__main__":
    solve()