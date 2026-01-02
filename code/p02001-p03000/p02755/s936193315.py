import sys
import math
input = sys.stdin.readline
input = sys.stdin.buffer.readline

def RD(): return sys.stdin.read()
def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def TI(): return tuple(map(int,input().split()))


def main():
    A, B = MI()
    x = 10*B
    n = 0

    for i in range(1001):
        if  math.floor(x*0.08) == A:
            break
        x += 1

        if i == 1000:
            x = 10*B
            break
    for i in range(1001):
        x += -1
        if math.floor(x*0.08) != A or math.floor(x*0.1) != B:
            x += 1
            break

    if math.floor(x*0.08) == A and math.floor(x*0.1) == B:
        print(x)
    else:
        print(-1)





if __name__ == "__main__":
	main()