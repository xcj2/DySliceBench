N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N)]
A = [a for a,b in AB]
B = [b for a,b in AB]
C = list(range(N))

def val(x):
  return B[x]

def merge(la, lb):
  na = len(la)
  nb = len(lb)
  ans = [None] * (na+nb)
  ia = 0
  ib = 0
  
  while ia<na and ib<nb:
    if val(la[ia]) < val(lb[ib]):
      ans[ia+ib] = la[ia]
      ia += 1
    else:
      ans[ia+ib] = lb[ib]
      ib += 1
      
  if ia<len(la):
    ans[ia+ib:] = la[ia:]
  if ib<len(lb):
    ans[ia+ib:] = lb[ib:]
  return ans
    
def mergeSort(x):
    l = len(x)
    if l <= 1:
        return x
    d = l // 2 
    left = mergeSort(x[:d])
    right = mergeSort(x[d:])
    return merge(left,right)

C = mergeSort(C)

ans = "Yes"
t = 0
for i in range(N):
    t += A[C[i]]
    if t > B[C[i]]:
        ans = "No"

print(ans)

