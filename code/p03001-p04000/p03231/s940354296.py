
N, M = map(int, input().split())
S = input()
T = input()

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    c = a % b
    return gcd(b, c)
 
def lcm(x, y):
    return (x * y) // gcd(x, y)

def my_index(l, x, default=False):
    if x in l:
        return l.index(x)
    else:
        return default

success = False
fans = 0

_lcm = lcm(len(S), len(T))

def isImpble(k, _lcm):
    global success
    global S
    global T
    global fans
    
    ans = k * _lcm
    double_st = []
    
    for i in range(len(S)):
        if (len(T)*i)%len(S) == 0 and (len(T) * i)//len(S) <len(T):
            double_st += [(i * ans)//len(S) + 1]
    isImpossible = False

    for st in double_st:
        s_i = ((st-1) * len(S))//ans
        t_i = ((st-1) * len(T))//ans
        if S[s_i] != T[t_i]:
            isImpossible = True
            break

            
    if isImpossible:
        return True
    else:
        success = True
        fans = k*_lcm
        return False
        

imp = isImpble((len(S) * len(T))//_lcm, _lcm)

if not imp:
    for k in range(1, (len(S) * len(T))//_lcm ):
        imp = isImpble(k, _lcm)
        if success:
            break
    

if not success:
    print(-1)
else:
    print(fans)