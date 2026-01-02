import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = input()
    pre = []

    def win_point(a):
        if a == 'r':
            pre.append('r')
            return p
        elif a == 's':
            pre.append('s')
            return r
        else:
            pre.append('p')
            return s

    ans = 0
    for i, j in enumerate(t):
        if i < k:
            ans += win_point(j)
        elif j != pre[i-k]:
            ans += win_point(j)
        else:
            pre.append('xx')
    print(ans)

if __name__ == '__main__':
    main()
