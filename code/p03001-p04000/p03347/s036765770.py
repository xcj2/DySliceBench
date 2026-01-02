import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(500000)

MOD = 1000000007

def smax(a,b):
    if a>b:
        return a
    else:
        return b

def smin(a,b):
    if a<b:
        return a
    else:
        return b

def main():
    N = int(readline())
    A = [int(readline()) for i in range(N)]
    prev = 0
    count = 0
    flag = True
    for i in range(N):
        if A[i]>prev:
            flag = False
            break
        elif A[i]==prev:
            prev+=1
            if prev!=1:
                count += 1
        else:
            prev = A[i]+1
            count += A[i]
    if flag:
        print(count)
    else:
        print(-1)


if __name__ == '__main__':
    main()