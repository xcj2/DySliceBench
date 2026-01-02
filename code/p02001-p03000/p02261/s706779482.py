import copy

def show (a,n):
  for i in range(n):
    if i > 0:
      print("",end=" ")
    print(a[i],end="")
  print("")

def selectionSort(a,n):
  for i in range(n):
    minj = i
    for j in range(i,n):
      if a[j][1] < a[minj][1]:
        minj = j
    a[minj],a[i] = a[i],a[minj]
  show(a,n)

def BubbleSort(a, n):
  for i in range(n):
    for j in range(n-1,i,-1):
      if a[j][1] < a[j-1][1]:
        a[j], a[j-1] = a[j-1],a[j]
  show(a,n)

n = int(input())
a1 = list(input().split())
a2 = copy.copy(a1)

BubbleSort(a1,n)
print("Stable")
selectionSort(a2,n)

for k in range(n):
  if a1[k] != a2[k]:
    print("Not stable")
    exit()

print("Stable")
