import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


s = S()
ans = 'Yes'
for i in range(len(s)):
    # print(s[i])
    if i % 2 == 0 and s[i] in {'R', 'U', 'D'}:
        # print('goo even')
        continue
    elif i % 2 != 0 and s[i] in {'L', 'U', 'D'}:
        # print('goo odd')
        continue
    # print('no...')
    ans = 'No'
    break
print(ans)
