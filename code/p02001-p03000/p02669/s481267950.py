import sys
sys.setrecursionlimit(700000)

def s_in():
    return input()

def n_in():
    return int(input())

def l_in():
    return list(map(int, input().split()))


t=n_in()


def execute(n, memo, setting):
    if n in memo:
        return memo[n]

    res = setting[1]*n
    for k in [2,3,5]:
        if n%k == 0:
            res = min(res, execute(n//k, memo, setting) + setting[k])
        else:            
            down = (n//k)*k
            res = min(res, execute(down//k, memo, setting) + setting[k] + (n-down)*setting[1])
            up = (n//k)*k+k
            res = min(res, execute(up//k, memo, setting) + setting[k] + (up-n)*setting[1])

    memo[n] = res
    return res

    

for _ in range(t):
    n,a,b,c,d = l_in()

    setting={2: a, 3: b, 5: c, 1: d}
    memo={1: d, 0: 0}

    print(execute(n,memo,setting))
    
