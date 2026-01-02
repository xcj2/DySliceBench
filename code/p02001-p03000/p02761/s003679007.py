import sys
input = sys.stdin.readline
input = sys.stdin.buffer.readline

def RD(): return sys.stdin.read()
def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def TI(): return tuple(map(int,input().split()))


def main():
    N,M = LI()
    s = [0]*M
    c = [0]*M
    n = [0]*3
    for i in range(M):
        Sn,Cn = LI()
        s[i] = Sn
        c[i] = Cn

    if N == 1:
        ans = [0]
    elif N == 2:
        ans = [1, 0]
    elif N == 3:
        ans = [1, 0, 0]

    for k in range(0, M):
        if ans[s[k]-1] != c[k]:
            n[s[k]-1] += 1
        ans[s[k]-1] = c[k]


    if (ans[0] == 0 and N != 1) or  n[0]>=2 or n[1]>=2 or n[2]>=2:
        print(-1)
    else:
        ans = map(str,ans)
        print(''.join(ans))




if __name__ == "__main__":
	main()