import bisect
import collections

def read():
    N = int(input().strip())
    S = str(input().strip())
    return N, S

def dig(S, T, N):
    k0, k1, k2 = -1, -1, -1
    for i in range(N):
        if S[i] == T[0]:
            k0 = i
            break
    if k0 == -1:
        return False
    for i in range(k0+1, N):
        if S[i] == T[1]:
            k1 = i
            break
    if k1 == -1:
        return False
    for i in range(k1+1, N):
        if S[i] == T[2]:
            k2 = i
            break
    if k2 == -1:
        return False
    return True


def solve(N, S):
    d = [collections.deque() for i in range(10)]
    count = 0
    for p in range(1000):
        T = '{:03d}'.format(p)
        count += 1 if dig(S, T, N) else 0
    return count
    
if __name__ == '__main__':
    inputs = read()
    output = solve(*inputs)
    print("%d" % output)
