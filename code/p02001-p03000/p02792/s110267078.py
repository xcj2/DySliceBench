import sys

def preprocessing():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))

    solve(N)

def solve(N: int):
    counts = [[0] * 10 for _ in range(10)]
    for i in range(10, N + 1):
        b = i % 10 
        while i >= 10:
            i //= 10 # Truncated division (i = i // 10)
        counts[i][b] += 1
    ret = 0
    for i in range(1, min(N + 1, 10)):
        ret += 1
        if counts[i][i] > 0:
            ret += counts[i][i] * 2
    for i in range(1, 10):
        for j in range(1, 10):
            ret += counts[i][j] * counts[j][i]
    print(ret)
    return


 
if __name__ == "__main__":
    preprocessing()