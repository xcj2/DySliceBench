import sys
input = sys.stdin.readline
input = sys.stdin.buffer.readline

def RD(): return sys.stdin.read()
def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def TI(): return tuple(map(int,input().split()))


def main():
    A1 = LI()
    A2 = LI()
    A3 = LI()
    N = II()
    b = [int(input()) for i in range(N)]
    ans = 0
    #print(b)

    if b.count(A2[1])!=0:
        if (b.count(A1[0])!=0 and b.count(A3[2])!=0) or (b.count(A3[0])!=0 and b.count(A1[2])!=0) or (b.count(A1[1])!=0 and b.count(A3[1])!=0) or(b.count(A2[0])!=0 and b.count(A2[2])!=0) :
            ans += 1
    if b.count(A1[0])!=0:
        if (b.count(A2[0])!=0 and b.count(A3[0])!=0) or (b.count(A1[1])!=0 and b.count(A1[2])!=0) :
            ans += 1
    if b.count(A3[2])!=0:
        if (b.count(A1[2])!=0 and b.count(A2[2])!=0) or (b.count(A3[0])!=0 and b.count(A3[1])!=0) :
            ans += 1
    if ans != 0:
        print("Yes")
    else:
        print("No")




if __name__ == "__main__":
	main()