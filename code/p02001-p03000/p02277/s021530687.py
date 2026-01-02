def Partition(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p,r):
        if (A[j] <= x):
            i += 1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]
    return i+1

def qsort(A,p,r):
    if p < r:
        q = Partition(A,p,r)
        qsort(A,p,q-1)
        qsort(A,q+1,r)

def marge(A,left,mid,right):
    n1 = mid -left
    n2 = right -mid
    L = []
    R = []
    for i in range(left,n1+left):
        L.append(A[i])
    for i in range(mid,n2+mid):
        R.append(A[i])
 
    L.append(card('S 10000000000'))
    R.append(card('S 10000000000'))
 
    r_id,l_id = 0,0
    for k in range(left,right):
        if(L[l_id] <= R[r_id]):
            A[k] = L[l_id]
            l_id += 1
        else:
            A[k] = R[r_id]
            r_id += 1
 
def margeSort(A,left,right):
    if left+1 < right:
        mid = int((left+right)/2)
        margeSort(A,left,mid)
        margeSort(A,mid,right)
        marge(A,left,mid,right)


class card(object):
    def __init__(self, str):
        data = str.split()
        self.symbol,self.num = data[0],int(data[1])
    
    def __le__(self,obj):
        if(self.num <= obj.num):
            return True
        else:
            return False
    def __ge__(self,obj):
        if(self.num >= obj.num):
            return True
        else:
            return False

    def display_card(self):
        print("{0} {1}".format(self.symbol,self.num))

c = []        
n = int(input())
while(n>0):
    c.append(card(input()))
    n -= 1
c_marge = c.copy()
margeSort(c_marge,0,len(c))

qsort(c,0,len(c)-1)

'''
notStable = False
for i in range(1,len(c)):
    if(c[i-1].num == c[i].num):
        firstCard = c[i-1]
        secondCard = c[i]
        is_found_1st = False
        is_found_2nd = False

        for org in c_org:
            if(org == firstCard):
                is_found_1st = True
            if(org == secondCard):
                is_found_2nd = True
                if(is_found_1st == True):
                    break
                else:
                    notStable = True
                    break
if(notstable == 1):
    print('Not stable')
else:
    print('Stable')
for x in c:
    x.display_card()
'''

is_stable = True
for i in range(0,len(c)):
    if(c[i] != c_marge[i]):
        is_stable = False
        break
if(is_stable == True):
    print('Stable')
else:
    print('Not stable')
for i in c:
    i.display_card()