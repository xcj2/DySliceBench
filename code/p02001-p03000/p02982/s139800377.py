import numpy as np
def dist(y, z):
    y = np.array(y)
    z = np.array(z)
    return (sum((y - z) **2)) ** (0.5)

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

def resolve():
    N, D = list(map(int, input().split()))
    X = []
    for _ in range(N):
        X.append(list(map(int, input().split())))
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if is_integer(dist(X[i], X[j])):
                ans+=1
    print(ans)
    return
resolve()