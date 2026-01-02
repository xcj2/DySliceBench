N,M = map(int,input().split())
S = input()
T = input()

def gcd(x, y):
    while y > 0:
        x, y = y, x%y
    return x
 
def lcm(x, y):
    return int(x/gcd(x, y)*y)

lenx = lcm(N,M)

s_list = list(S)
t_list = list(T)

baisuu_s = int(lenx/N)
baisuu_t = int(lenx/M)
def check():
    for i in range(0,lenx,baisuu_s):
        if i % baisuu_s==0 and i%baisuu_t == 0:
            if s_list[int(i/baisuu_s)] == t_list[int(i/baisuu_t)]:
                pass
            else:
                return False
    return True

if check():
    print(lenx)
else:
    print(-1)