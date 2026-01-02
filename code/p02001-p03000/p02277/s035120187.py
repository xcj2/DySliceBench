n = int(input())
a = [0]*n


class card:
    def __init__(self, s, input_idx):
        self.m = s.split()[0]
        self.num = int(s.split()[1])
        self.t = s
        self.input_idx = input_idx
 
for i in range(n):
    a[i] = card(input(), i)
    
def partition(A, p, r):
    x = A[r].num
    i = p-1
    for j in range(p,r):
        if A[j].num <= x:
            i = i+1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    
    return i+1

def quickSort(A, p, r):
   if p < r:
     q = partition(A, p, r)
     quickSort(A, p, q-1)
     quickSort(A, q+1, r)

quickSort(a, 0, n-1)

stable = True
for i in range(1, n):
    if a[i].num==a[i-1].num and a[i].input_idx<a[i-1].input_idx:
        stable = False
        
if stable:
    print('Stable')
else:
    print('Not stable')
    
for item in a:
    print(item.t)

