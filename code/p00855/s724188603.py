# coding: utf-8
# Your code here!
# input
def horizontal_input(T=str,debug=False):
    data = list(map(T,input().split()))
    if debug:
        print(*data)
    return data

def vertical_input(n,T=str,sep=False,septype=list,debug=False):
    data=[]
    if sep:
        for i in range(n):
            data.append(septype(map(T,input().split())))
    else:
        for i in range(n):
            data.append(T(input()))
    if debug:
        print(*data,sep='\n')
    return data

# Eratosthenes
def eratosthenes(n):
    prime_table = [False,False,True]+[False if i%2!=0 else True for i in range(n-2)]
    i=3
    while i*i<=n:
        if prime_table[i]:
            j=i*i
            while j<=n:
                prime_table[j]=False
                j+=i
        i+=2
    return prime_table

prime_table = eratosthenes(2000000)
primes=[]
for i in range(len(prime_table)):
    if prime_table[i]:
        primes.append(i)

while 1:
    n=int(input())
    if n==0:
        break
    i=0
    while primes[i]<=n:
        i+=1
    i=primes[i-1]
    if i==n:
        print(0)
    else:
        count=1
        j=i+1
        while 1:
            if prime_table[j]:
                break
            j+=1
            count+=1
        print(count)
