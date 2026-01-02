import sys


def input():
    return sys.stdin.readline().rstrip()

def euc(a,b):

    while b!=0:
        a,b =b,a%b

    return a

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append(i)

    if temp != 1:
        arr.append(temp)

    if arr == []:
        arr.append(n)
    return arr



def main():

    N =int(input())
    A =list(map(int,input().split()))

    PS =set()

    current =A[0]
    for i in range(N-1):
        current =euc(current,A[i+1])
        if current ==1:
            break

    else:
        print("not coprime")
        exit()


    for i in range(N):
        if A[i]==1:
            continue
        aa =factorization(A[i])
        for i in aa:
            if i in PS:
                print("setwise coprime")
                exit()
            else:
                PS.add(i)

    print("pairwise coprime")
    exit()



if __name__ == "__main__":
    main()
