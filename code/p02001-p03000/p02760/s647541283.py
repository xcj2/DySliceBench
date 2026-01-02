A1 = list(map(int, input().split()))
A2= list(map(int, input().split()))
A3 = list(map(int, input().split()))
A = A1 + A2 + A3

N = int(input())

B = []
for i in range(N):
    B.append(int(input()))

# 縦のビンゴがある
def isExistTatePair():
    # すべての当選番号を調べる
    for i in range(3):
            sum = 0
            for j in range(3):
                sum += A[3 * j + i]
            
            # ビンゴか調べる
            if sum == 0:
                return True
    return False
    
# 横のビンゴがある
def isExistYokoPair():
    # すべての当選番号を調べる
    for i in range(3):
            sum = 0
            for j in range(3):
                sum += A[3 * i + j]
            
            # ビンゴか調べる
            if sum == 0:
                return True
    return False
    
# ななめのビンゴがある
def isExistNanamePair():
    # 左上から右下へのななめ
    naname1 = A[0] + A[4] + A[8]
    
    if naname1 == 0:
        return True
    
    # 右上から左下へのななめ
    naname2 = A[2] + A[4] + A[6]
    
    if naname2 == 0:
        return True
    
    return False

# 当選番号を見てビンゴカードに穴をあける
for b in B:
    for index in range(len(A)):
        a = A[index]
        if a == b:
            A[index] = 0
    
isExistBingo = isExistTatePair() or isExistYokoPair() or isExistNanamePair()
print('Yes' if isExistBingo else 'No')