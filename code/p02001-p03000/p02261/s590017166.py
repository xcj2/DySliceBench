n = int(input())
clist = list(map(list, input().split()))

def BubbleSort(C, n):
    for i in range(n-1):
        for w in range(i+1, n):
            j = n-w+i
            if (C[j][1] < C[j-1][1]):
                a = C[j]
                C[j] = C[j-1]
                C[j-1] = a
def SelectionSort(C, n):
    for i in range(n):
        mini = i
        for j in range(i+1,n):
            if (C[j][1] < C[mini][1]):
                mini = j
        if(mini != i):
            a = C[i]
            C[i] = C[mini]
            C[mini] = a
## l[1]이 str 이라는것에 주의 int(l[1])을 해줘야함 --> 이거 때문에 20분 디버깅 소비
def stable(A,B):
    count = [0 for i in range(9)]
    for l in A:
        count[int(l[1]) - 1] += 1
    ilist = [] ##安定なiのリスト
    for i in range(1,10):
        if (count[i-1] > 1):
            awlist = []
            for l in A:
                if(int(l[1]) == i):
                    awlist.append(l[0])
            bwlist = []
            for l in B:
                if(int(l[1]) == i):
                    bwlist.append(l[0])
            if (awlist == bwlist):
                ilist.append(i)
            
        else:
            ilist.append(i)
    if (len(ilist) == 9):
        print('Stable',end = '')
    else:
        print('Not stable', end = '')
                  

Blist = list(clist)
BubbleSort(Blist, n)
for i in range(n):
    if (i == n-1):
        print('{}{}'.format(Blist[i][0],Blist[i][1]), end = '')
    else : 
        print('{}{}'.format(Blist[i][0],Blist[i][1]), end = ' ')
print()
stable(clist, Blist)
print()

Slist = list(clist)
SelectionSort(Slist, n)
for i in range(n):
    if(i == n-1):
        print('{}{}'.format(Slist[i][0],Slist[i][1]), end = '')
    else:
        print('{}{}'.format(Slist[i][0],Slist[i][1]), end = ' ')
print()
stable(clist, Slist)
print()

