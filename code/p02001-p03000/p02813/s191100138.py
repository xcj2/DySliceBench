n = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

def fact(n):
  if n==1:
    return 1
  else:
    return n*fact(n-1)

def hoge(n,lis):
    for i in range(len(lis)):
        if n==lis[i]:
            return i
        
def cnt(lis):
    #input: list
    l = list(range(1,len(lis)+1)) #[1,2,...,n]
    ret = 1
    for i in range(len(lis)-1):
        ret += (hoge(int(lis[i]),l)) * fact(len(l)-1)
#         print((int(lis[i])-1) * fact(len(l)-1))
        l.remove(lis[i])
#         print(l)
    return ret

print(abs(cnt(P) - cnt(Q)))