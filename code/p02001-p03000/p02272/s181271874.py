n = int(input())
A = list(map(int, input().split()))
SWAP = 0

def conquer(A, left, mid, right):
  L, R = A[left:mid], A[mid:right]
  # L, Rの末尾にINFTYを入れないと、L[-1] or R[-1]が評価されない
  INFTY = 2 ** 30
  L.append(INFTY)
  R.append(INFTY)
  # i : position in L, j : position in R
  i, j = 0, 0

  swap_times =  0

  # 元のArrayを変えたいため、kを生成
  for k in range(left, right):
    # print(i, j, L, R, A)
    if L[i] <= R[j]:
      A[k] = L[i]
      i = i + 1
    else:
      A[k] = R[j]
      j = j + 1
    swap_times += 1

  return swap_times

def divide(A, left, right):
  # print(left, right)

  # A[right-left]が2つ以上の場合に
  if left+1 < right:
    mid = (left+right)//2

    countL = divide(A, left, mid)
    countR = divide(A, mid, right)

    return conquer(A, left, mid, right) + countL + countR

  return 0

def mergeSort(A):
  return divide(A, 0, len(A))

swap = mergeSort(A)

print(" ".join([ str(i) for i in A]))
print(swap)
