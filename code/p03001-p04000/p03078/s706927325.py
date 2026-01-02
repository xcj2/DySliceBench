def int_raw():
    return int(input())

def ss_raw():
    return input().split()

def ints_raw():
    return list(map(int,ss_raw()))

X,Y,Z,K = ints_raw()

A = list(map(int, input().split()))
B= list(map(int, input().split()))
C= list(map(int, input().split()))
A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)
def main():
    D = []
    for a in A:
        for b in B:
            D.append(a+b)
    D.sort(reverse=True)
    D = D[:K+1]
    E =[]
    for d in D:
        for c in C:
            E.append(d+c)
    E.sort(reverse=True)
    for e in range(K):
        print (E[e])

main()
