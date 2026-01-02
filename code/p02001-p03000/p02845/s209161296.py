def read():
    N = int(input().strip())
    A = list(map(int, input().strip().split()))
    return N, A


def next_state(c, a, n_patterns):
    # c := c[0] >= c[1] >= c[2]
    idx = -1
    for i in range(3):
        if c[i] == a:
            idx = i
            break
    if idx == -1:
        return -1, -1
    n_equals = 1
    n_equals += 1 if c[idx%3] == c[(idx + 1) % 3] else 0
    n_equals += 1 if c[idx%3] == c[(idx + 2) % 3] else 0
    c[idx%3] += 1
    n_patterns *= n_equals
    n_patterns %= 1000000007
    return c, n_patterns

def solve(N, A):
    c = [0, 0, 0]
    n = 1
    for a in A:
        c, n = next_state(c, a, n)
        if c == -1 and n == -1:
            return 0
    return n
    
if __name__ == '__main__':
    inputs = read()
    output = solve(*inputs)
    print("%d" % output)
