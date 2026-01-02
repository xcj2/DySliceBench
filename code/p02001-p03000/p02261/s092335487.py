import math
import itertools

def getNum(card: str) -> int:
  return int(card[1])

def checkStable(origin: list, sorted: list) -> str: # Stable or Not stable
  N_origin = [[] for _ in range(9)]
  for item in origin:
    num = getNum(item)
    N_origin[num-1].append(item)

  for item in sorted:
    num = getNum(item)    

    if N_origin[num-1][0] != item:
      return False
    else:
      N_origin[num-1].pop(0)

  return True

def main():
  n = int(input())
  A = list(input().split())
  len_A = len(A)  
  B = list(A)
  C = list(A)

  # bubble sort
  for i in range(len_A): 
    for j in reversed(range(i+1, len_A)):
      if getNum(B[j]) < getNum(B[j-1]):
        tmp = B[j]
        B[j] = B[j-1]
        B[j-1] = tmp

  # select sort
  for i in range(len_A):
    min = i
    for j in range(i, len_A):
      if getNum(C[j]) < getNum(C[min]):
        min = j
    
    if min != i:
      tmp = C[min]
      C[min] = C[i]
      C[i] = tmp

  print(*B) #bubble sort
  if checkStable(A, B):
    print('Stable')
  else:
    print('Not stable')
  print(*C) #select sort
  if checkStable(A, C):
    print('Stable')
  else:
    print('Not stable')

if __name__ == '__main__':
  main()
