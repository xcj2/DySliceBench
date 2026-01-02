#atcoder template
def main():
    import sys
    imput = sys.stdin.readline
    #文字列入力の時は上記はerrorとなる。
    #ここにコード
    #input
    N = int(input())
    A = list(map(int, input().split()))

    #output
    import itertools
    import math
    B = list(itertools.accumulate(A))

    def f(a, i):
        return abs(B[i]-B[a]-B[a])
    def g(b, i):
        return abs(B[-1]-B[b]- (B[b]- B[i]))
    answer = pow(10, 10)
    for i in range(1, N-2):
        left1 = 0
        right1 = i
        while left1 + 2 < right1:
            c1 = left1 + (right1 - left1)//3
            c2 = right1 - (right1 - left1)//3
            if f(c1, i) > f(c2, i):#条件が満たされる:
                left1 = c1
            else:
                right1 = c2
        left2 = i
        right2 = N-1
        while left2 + 2 < right2:
            c3 = left2 + (right2 - left2)//3
            c4 = right2 - (right2 - left2)//3
            if g(c3, i) > g(c4, i):#条件が満たされる:
                left2 = c3
            else:
                right2 = c4
        p = sorted([(f(j, i), j) for j in range(left1, right1+1)])[0][1]
        q = sorted([(g(j, i), j) for j in range(left2, right2+1)])[0][1]
        m = min(B[p], B[i]-B[p], B[q]-B[i], B[-1]-B[q])
        M = max(B[p], B[i]-B[p], B[q]-B[i], B[-1]-B[q])
        answer = min(answer, M-m)

    print(answer)

    #N = 1のときなどcorner caseを確認！
if __name__ == "__main__":
    main()