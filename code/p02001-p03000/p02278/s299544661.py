def mklist(B,D,V):
    min = 10000
    for key,val in enumerate(B):
        D[val] = key
        V[val] = 0
        if min > val:
            min = val
    return min

def solve(A,V,D,min):
    cost = 0
    for key, val in enumerate(A):
        if V[val] != 0:
            continue
        W = []
        wmin = 10000
        tw = 0
        k1 = key
        v = val
        while(1):
            k2 = D[v]
            if V[v] == 1:
                break
            W.append(v)
            V[v] = 1
            if wmin > v:
                wmin = v
            tw += v
            #print("key={} k1={} k2={} v={} Vv={}".format(key,k1,k2,v,V[v]))
            k1 = k2
            v = A[k1]
        n = len(W)
        t1 = tw + ((n - 2) * wmin)
        t2 = tw + wmin + ((n + 1) * min)
        if t1 < t2:
            cost += t1
        else:
            cost += t2
    return cost

def main():
    num = int(input())
    A = list(map(int,input().split()))
    B = sorted(A)
    D = {}
    V = {}
    min = mklist(B,D,V)
    cost = solve(A,V,D,min)
    print(cost)

if __name__ == '__main__':
    main()