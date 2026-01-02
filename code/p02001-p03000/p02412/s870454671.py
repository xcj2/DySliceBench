#関数リスト
import sys
input = sys.stdin.readline


def RD(): return input().rstrip()
def I(): return int(input().rstrip())
def MI(): return map(int, input().split())
def MF(): return map(float,input().split())
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float,input().split()))

def main():
    while True:
        n, x = MI()
        if n == 0 and x == 0:
            exit()
        result = 0
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                k = x - i - j
                if k > j and k <= n:
                    result += 1
        print(result)

if __name__ == "__main__":
    main()

