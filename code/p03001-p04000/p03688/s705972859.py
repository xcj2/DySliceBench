def ri(): return int(input())
def rli(): return list(map(int, input().split()))
def ris(): return list(input())
def pli(): return "".join(list(map(str, ans)))
 
 
N = ri()
a = rli()
ma = max(a)
mi = min(a)
if(ma - mi > 1):
    print("No")
elif(ma - mi == 1):
    l_ma = a.count(ma)
    l_mi = a.count(mi)
    if(ma <= l_mi):
        print("No")
    elif(l_mi + l_ma/2 >= ma):
        print("Yes")
    else:
        print("No")
else:
    if(a[0] == N-1):
        print("Yes")
    elif(N/a[0] >= 2):
        print("Yes")
    else:
        print("No")