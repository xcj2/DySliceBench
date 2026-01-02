N = int(input())
A = list(input().split(" "))

class Card:
    def __init__(self,suit,num):
        self.suit = suit
        self.value = int(num)
        self.id = suit+num
        
    

B_bubble = [Card(a[0],a[1])for a in A]
B_selection = [b for b in B_bubble]

B_id = [b.id for b in B_bubble]

def BubbleSort(C,N):
    for i in range(N):
        for j in range(N-1,i,-1):
            if C[j].value < C[j-1].value:
                tmp = C[j]
                C[j] = C[j-1]
                C[j-1] = tmp
        #print([b.id for b in C])
    return C
    
def SelectionSort(C, N):
    for i in range(N):
      minj = i
      for j in range(i,N):
        if C[j].value < C[minj].value:
          minj = j
      tmp = C[i]
      C[i] = C[minj]
      C[minj] = tmp
      #print([b.id for b in C])
    return C

def stable_check(B_id,C_id):
    tmp = C_id[0]
    for i in range(1,len(C_id)):
        c = C_id[i]
        if c[1]!=tmp[1]:
            tmp = c
            continue
        if B_id.index(tmp)>B_id.index(c):
            return "Not stable" 
        tmp = c
    return "Stable"
    

C_bubble =  [b.id for b in BubbleSort(B_bubble,N)]
print(" ".join(C_bubble))
#C_bubble_id = [b.id for b in C_bubble]
print(stable_check(B_id,C_bubble))

C_selection =  [b.id for b in SelectionSort(B_selection,N)]
print(" ".join(C_selection))
#C_selection_id = [b.id for b in C_selection]
print(stable_check(B_id,C_selection))


