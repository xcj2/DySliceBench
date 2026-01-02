import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    S = list(input())
    R = set()
    G = set()
    B = set()

    def MIN(a, b):
        if a > b:
            return b
        else:
            return a
    def MAX(a, b):
        if a > b:
            return a
        else:
            return b

    for i, s in enumerate(S):
        if s == 'R':
            R.add(i)
        elif s == 'G':
            G.add(i)
        else:
            B.add(i)

    b_len = len(B)
    ans = 0
    for r in R:
        for g in G:
            v1 = MIN(r, g)
            v2 = MAX(r, g)
            rg_diff = v2 - v1
            ans += b_len
            if v2 + rg_diff in B:
                ans -= 1
            if v1 - rg_diff in B:
                ans -= 1
            if (r + g) % 2 == 0 and (r + g) // 2 in B:
                ans -= 1
    print(ans)

if __name__ == '__main__':
    main()
