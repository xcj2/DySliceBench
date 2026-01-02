# Sort II - Quick Sort
class Card():
    def __init__(self,suit,num):
        """suit and num are str"""
        self.s = suit
        self.n = int(num)
    def __str__(self):
        return self.s + ' ' + str(self.n)

def partition(A,p,r):
    x = A[r].n
    i = p - 1
    for j in range(p,r,1):
        if A[j].n <= x:
            i += 1
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp
    tmp = A[i+1]
    A[i+1] = A[r]
    A[r] = tmp
    return i + 1
def quick_sort(A,p,r):
    if p < r:
        q = partition(A,p,r)
        quick_sort(A,p,q-1)
        quick_sort(A,q+1,r)
def is_stable(Org,A):
    cop = A[:]
    for org in Org:
        i = cop.index(org)
        if i > 0:
            if A[i - 1].n == org.n:
                return False
        del cop[i]
    return True
n = int(input())
A = [Card(*input().split()) for _ in range(n)]
Or = A[:]
quick_sort(A,0,len(A)-1)
if is_stable(Or,A): print('Stable')
else: print('Not stable')
for a in A: print(a)
