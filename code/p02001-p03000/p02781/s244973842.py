N=int(input())
K=int(input())

M = len(str(N)) # 桁数

def solve_1(n,m):
    ans = 0
    ans += 9*(m-1)
    x = n//(10**(m-1))
    ans += x
    return ans

def solve_2(n,m):
    ans=0
    if m<2:
        return ans
    elif m>2:
        ans+= (9**2)*int((m-2)*(m-1)/2) 

    x = n//(10**(m-1))
    ans+= (x-1)*(m-1)*9

    y=int(str(n)[1:])
    ans+=solve_1(y,len(str(y)))
    # ans+= int(str(n)[1])+9*(m-2)
    return ans

def solve_3(n,m):
    ans=0
    if m<3:
        return ans
    elif m>3:
        ans+=int((9**3)*(1/6)*(m-1)*(m-2)*(m-3))
    
    x = n//(10**(m-1))
    ans+=int((x-1)*(m-1)*(m-2)/2*81)
    
    y= int(str(n)[1:])

    ans+=solve_2(y,len(str(y)))
    return ans

if K==1:
    ans = solve_1(N,M)
if K==2:
    ans = solve_2(N,M)
if K==3:
    ans = solve_3(N,M)

print(ans)