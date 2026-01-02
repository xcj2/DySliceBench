import sys, copy
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**10
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    N = I()
    C_tmp = LSS()
    C = [{'suit':'', 'value':0} for _ in range(N)]
    for i in range(N):
        C[i]['suit'] = C_tmp[i][0]
        C[i]['value'] = int(C_tmp[i][1:])

    def BubbleSort(C, N):
        for i in range(N):
            for j in range(N-1, i, -1):
                if C[j]['value'] < C[j-1]['value']:
                    C[j], C[j-1] = C[j-1], C[j]
        return C

    def SelectionSort(C, N):
        for i in range(N):
            minj = i
            for j in range(i, N):
                if C[j]['value']<C[minj]['value']:
                    minj = j
            if i!=minj:
                C[i], C[minj] = C[minj], C[i]
        return C

    def isStable(C, C_s):
        isStable = True
        for i in range(1, 10):
            if [j['suit'] for j in C if j['value']==i]!=[j['suit'] for j in C_s if j['value']==i]:
                isStable = False
        ret = 'Stable' if isStable else 'Not stable'
        return ret

    C_bs = BubbleSort(copy.deepcopy(C), N)
    print(*[i['suit']+str(i['value']) for i in C_bs])
    print(isStable(C, C_bs))

    C_ss = SelectionSort(copy.deepcopy(C), N)
    print(*[i['suit']+str(i['value']) for i in C_ss])
    print(isStable(C, C_ss))

if __name__ == '__main__':
    resolve()
