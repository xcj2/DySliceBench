import sys
import math
input = sys.stdin.readline
input = sys.stdin.buffer.readline

def RD(): return sys.stdin.read()
def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def TI(): return tuple(map(int,input().split()))
def RN(N): return [input().strip() for i in range(N)]


def main():
    X = II()
    i = 0
    M = 100
    
    while True:
        i += 1
        M = M + math.floor(M * 0.01)
        if M>=X:
            break
    
    print(i)



if __name__ == "__main__":
	main()