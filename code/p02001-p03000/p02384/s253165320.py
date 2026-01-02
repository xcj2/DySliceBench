num=list(map(int,input().split()))
q=int(input())

def E(ls):
    ls=[ls[3],ls[1],ls[0],ls[5],ls[4],ls[2]]
    return ls

def N(ls):
    ls=[ls[1],ls[5],ls[2],ls[3],ls[0],ls[4]]
    return ls

def R(ls):
    ls=[ls[0],ls[2],ls[4],ls[1],ls[3],ls[5]]
    return ls

for i in range(q):
    num0,num1=list(map(int,input().split()))
    if num.index(num0) in [0,2,3,5]:
        while num[0]!=num0:
            num=E(num)
        while num[1]!=num1:
            num=R(num)
        print(num[2])
    else:
        while num[0]!=num0:
            num=N(num)
        while num[1]!=num1:
            num=R(num)
        print(num[2])
        
