def resolve():
    X, Y, Z, K = list(map(int, input().split()))
    A = sorted(list(map(int, input().split())), reverse=True)
    B = sorted(list(map(int, input().split())), reverse=True)
    C = sorted(list(map(int, input().split())), reverse=True)
    
    # 「美味しさの和がp以上である組み合わせがK個以上存在する」ならtrue
    def isOk(p):
        cnt = 0
        for i in range(X):
            for j in range(Y):
                for k in range(Z):
                    if A[i]+B[j]+C[k] < p: # sorted
                        break
                    cnt += 1
                    if cnt >= K:
                        return True
        return False
    
    # p以上の美味しさの和をすべて返す
    def values_higher_than(p):
        sums = []
        for i in range(X):
            for j in range(Y):
                for k in range(Z):
                    if A[i]+B[j]+C[k] < p: # sorted
                        break
                    sums.append(A[i]+B[j]+C[k])
        return sums
    
    left = -1
    right = 10**11
    while (right - left) > 1:
        mid = left + (right - left) // 2
        if isOk(mid):
            left = mid
        else:
            right = mid
    
    #print(left)
    ans = sorted(values_higher_than(left), reverse=True)
    for i in range(K):
        if i < len(ans):
            print(ans[i])
        else:
            print(left)


if '__main__' == __name__:
    resolve()