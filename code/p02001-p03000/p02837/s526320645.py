def read():
    N = int(input().strip())
    A = []
    X = []
    Y = []
    for i in range(N):
        
        a = int(input().strip())
        A.append(a)
        x = [-1 for i in range(a)]
        y = [-1 for i in range(a)]
        for i in range(a):
            x[i], y[i] = list(map(int, input().strip().split()))
            x[i] -= 1
        X.append(x)
        Y.append(y)
    return N, A, X, Y

def is_honest(ptn, x):
    return (ptn >> x) & 1

def count_honest(ptn, N):
    count = 0
    for i in range(N):
        if is_honest(ptn, i):
            count += 1
    return count

def check_ptn(ptn, N, A, X, Y):
    count = 0
    for i in range(N):
        if is_honest(ptn, i) == 1:
            for x, y in zip(X[i], Y[i]):
                if is_honest(ptn, x) != y:
                    return False
    return True


def solve(N, A, X, Y):
    ptns = 1 << N
    max_honest = 0
    for ptn in range(ptns):
        if check_ptn(ptn, N, A, X, Y):
            n_honest = count_honest(ptn, N)
            if n_honest > max_honest:
                max_honest = n_honest
    return max_honest

if __name__ == '__main__':
    inputs = read()
    print("%d" % solve(*inputs))
