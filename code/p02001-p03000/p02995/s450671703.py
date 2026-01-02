#@k0gane_p 
a, b, c, d = [int(i) for i in input().split()]
def gcd(x,y):#最大公約数
    while y:
        x,y = y, x%y
    return x
def lcm(x,y):#最小公倍数
    return x*y // gcd (x,y)
def count(A,B,C):#A以下で、BでもCでも割り切れない個数
    D=A//B
    E=A//C
    F=A // lcm(B,C)
    return A-D-E+F
ans = count(b, c, d) - count(a-1, c, d)
#A以上B以下の整数のうち、CでもDでも割り切れないものの個数
#if(a % c != 0 and a % d != 0):
    #ans += 1#AがCでもDでも割り切れないなら、足す１
print(ans)