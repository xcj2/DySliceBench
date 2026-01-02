ii = lambda:int(input())
li = lambda:list(map(int,input().split()))
lix = lambda x:list(li() for _ in range(x))
##########
def main(n,a):
    res = 0
    ran = 2**n
    for tar in range(1,ran):
        check = True
        for i in range(n):
            if tar>>i & 1 and not isHonest(tar, a[i]):
                check = False
                break
        if check : res = max(res, count(tar,n))
    return res                

def count(tar, n):
    res = 0
    for i in range(n):
        if tar>>i & 1 : res += 1
    return res

def isHonest(tar, a):
    res = True
    for i in range(len(a)):
        x,y = a[i]
        if tar>>(x-1) & 1 != y : return False
    return True

n = ii()
a = []
for i in range(n):
    c = ii()
    a.append(lix(c))
print(main(n,a))