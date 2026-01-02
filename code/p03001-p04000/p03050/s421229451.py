from math import sqrt

def cal_dummy(N):
    output = 0
    for m in range(1,N):
        if N // m == N % m:
            output += m
    return output

def cal(N):
    #N == m*q+r(0 <= r < m)としてq==rのとき
    #N == (m+1)*r(0 <= r <= m-1)
    if N == 1:
        return 0
    else:
        output = 0
        for r in range(1,int(sqrt(N))+1):
            if N % r == 0:
                m = (N // r) - 1
                if (N//m) == r:
                    output += m
        return output

def main():
    N = int(input())

    print(cal(N))

if __name__ == "__main__":
    main()
