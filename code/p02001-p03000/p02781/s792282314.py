
def f(i,k):#i桁目がnum未満
    if i == 0:
        return 0
    num = int(s[-i])
    if k == 0:
        if num ==0:return 0
        else: return 1
    if num==0:
        return 0
    return (num-1)* ncr(i-1,k-1)*9**(k-1)+ncr(i-1,k)*9**k


def g(i,k):#i桁目がnum
    if i == 0:
        if k==0:return 1
        else:return 0
    num = int(s[-i])
    if k == 0:
        if num ==0:return 1
        else:return 0

    if num==0:
        return f(i-1,k) +g(i-1,k)
    else:
        return f(i-1,k-1) + g(i-1,k-1)



def ncr(n,r):##　n>>r の場合のncr　O(r) r>nなら0
    x = 1
    y = 1
    for i in range(r):
        x*=(n-i)
        y*=(i+1)
    return x//y

s = input()
k = int(input())
l= len(s)
print(f(l,k)+g(l,k))
