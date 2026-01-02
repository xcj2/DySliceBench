N = int(input())
K = int(input())
def nonzero1(N):
    m = len(str(N))
    a = int(str(N)[-m]) 
    return a + 9*(m-1)
def nonzero2(N):
    m = len(str(N))
    a = int(str(N)[-m])
    n = N - a * (10**(m-1))
    s = ((m-1)*(m-2)*9*9)//2 + (m-1)*(a-1)*9
    return s + nonzero1(n)
def nonzero3(N):
    m = len(str(N))
    a = int(str(N)[-m])
    n = N - a * (10**(m-1))
    s = ((m-1)*(m-2)*(m-3)*9*9*9)//6 +((m-1)*(m-2)*9*9*(a-1))//2
    return s + nonzero2(n)
if K == 1:
    print(nonzero1(N))
elif K == 2:
    print(nonzero2(N))
else:
    print(nonzero3(N))