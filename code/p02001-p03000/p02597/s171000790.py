import sys

def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def TI(): return tuple(map(int,input().split()))
def RN(N): return [input().strip() for i in range(N)]


def main():
    N = II()
    c = str(input())

    x = 1
    ans = 0
    y = 0

    for i in range(N):
        if y != 0:
            break
        if c[i] == "W":
            for j in range(x, N):
                ii = -j
                if c[ii] == "R" and j < N-i:
                    ans += 1
                    x = j+1
                    break
                if j>= N-i:
                    y += 1
                    break



    print(ans)

if __name__ == "__main__":
	main()