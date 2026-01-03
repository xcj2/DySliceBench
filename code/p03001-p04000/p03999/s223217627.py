import sys

def debug(x, table):
    for name, val in table.items():
        if x is val:
            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)
            return None

def solve():
    S = input()
    N = len(S) - 1
    ans = 0

    for i in range(2**N):
        bi = bin(i)[2:].zfill(N)
        # print(bi)
        ans += calc(S, bi)

    print(ans)

def calc(S, bi):
    ret = 0
    k = 0

    for i in range(len(S)):
        if i == 0:
            continue
        else:
            if bi[i-1] == '1':
                ret += int(S[k:i])
                k = i

    ret += int(S[k:])

    return ret

if __name__ == '__main__':
    solve()