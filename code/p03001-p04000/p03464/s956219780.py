import sys
input = sys.stdin.readline

def ceil(a, b):
    if a%b == 0:
        return a//b
    else:
        return a//b + 1

def f(l, r, a):
    # 区間[l, r]内の，最小・最大のaの倍数があれば返す
    min_ = ceil(l, a) * a
    max_ = (r // a) * a
    if min_ > max_:
        return False, min_, max_
    else:
        return True, min_, max_

def main():
    K = int(input())
    A = list(map(int, input().split()))[::-1]

    min_ = 2
    max_ = 2
    for i in range(K):
        jud, x, y = f(min_, max_, A[i])
        if not jud:
            print(-1)
            return
        min_ = x
        max_ = y + A[i] - 1
        # print(min_, max_)
    
    print(min_, max_)

if __name__ == "__main__":
    main()