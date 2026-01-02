def s0():return input()
def s1():return input().split()
def s2(n):return [input() for x in range(n)]
def s3(n):return [[input().split()] for _ in range(n)]
def n0():return int(input())
def n1():return [int(x) for x in input().split()]
def n2(n):return [int(input()) for _ in range(n)]
def n3(n):return [[int(x) for x in input().split()] for _ in range(n)]

n=n0()
s=s0()

a=[0]*1000
for i in range(1000):
    num=str(i).zfill(3)
    j=0
    for x in s:
        if x==num[j]:
            j+=1
        if j==3:
            a[i]=1
            break
print(sum(a))