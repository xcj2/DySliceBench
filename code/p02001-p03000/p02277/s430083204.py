# 関数定義
def partition(A, p, r):
    x = A[r]["number"]
    i = p - 1
    
    for j in range(p, r):
        if A[j]["number"] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    
    A[i + 1], A[r] = A[r], A[i + 1]
    
    return i + 1

def quickSort(A, p, r):
    if p < r:
        q = partition(A, p ,r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)
        
def is_stable(A):
    for i in range(0, len(A) - 1):
        j = i + 1
        #print(A[i]["number"], A[j]["number"], ":", A[i]["order"], A[j]["order"])
        if (A[i]["number"] == A[j]["number"] and A[i]["order"] > A[j]["order"]):
            return False
    return True

# 入力
N = int(input())
A = []
for i in range(N):
    card = input().split()
    A.append({'mark': card[0], 'number': int(card[1]), 'order': i})
    
# ソート
quickSort(A,0,N-1)

# is_stable()
if(is_stable(A)):
    print("Stable")
else:
    print("Not stable")
    
# 中身
for a in A :
    print(a["mark"], a["number"])
