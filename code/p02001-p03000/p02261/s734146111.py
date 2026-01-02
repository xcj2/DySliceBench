def BubbleSort(C, N):
    '''C: list of str((S|H|C|D)+str(int)) -> list of str, str
    '''
    cli = C.copy()
    for i in range(N):
        for j in range(N - 1, i, -1):
            if int(cli[j][1:]) < int(cli[j - 1][1:]):
                cli[j], cli[j-1] = cli[j-1], cli[j]
    return cli, "Stable"

def SelectionSort(C,N):
    '''C: list of str((S|H|C|D)+str(int)) -> list of str, str
    '''
    cli = C.copy()
    for i in range(N):
        minj = i
        for j in range(i, N):
            if int(cli[j][1:]) < int(cli[minj][1:]):
                minj = j
        cli[i], cli[minj] = cli[minj], cli[i]
    return cli, isStable(cli, C)
def isStable(L1, L2):
    '''list of str(sorted), list of str -> str('Stable' or 'Not stable')
    '''
    s1, s2 = None, None
    #i1, i2 = None, None
    for i in range(len(L1)-1):
        for j in range(i+1, len(L1)):
            if int(L1[i][1:]) == int(L1[j][1:]):
                s1, s2 = L1[i], L1[j]  #i < j
                if L2.index(s1) >= L2.index(s2):
                    return 'Not stable'
    return 'Stable'
def printlist(L):
    for itm in L[:-1]:
        print(itm, end = ' ')
    print(L[-1])

N = int(input())
C = list(input().split())

L, s = BubbleSort(C, N)
printlist(L)
print(s)
L, s = SelectionSort(C, N)
printlist(L)
print(s)

