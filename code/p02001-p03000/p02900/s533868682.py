import sys


# \n
def input():
    return sys.stdin.readline().rstrip()

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i

#               arr.append(i)   # こちらにすると素因数分解


            arr.append(i)



    if temp != 1:
        arr.append(temp)

    if arr == []:
        arr.append(n)
    return arr

def euc(a,b):

    while b!=0:
        a,b =b,a%b

    return a


def main():

    A,B=map(int,input().split())
    s =euc(A,B)
    if s==1:
        print(1)
        exit()
    print(len(factorization(s))+1)
if __name__ == "__main__":
    main()
