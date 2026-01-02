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
    F=A // lcm(B,C)#Fは両方で割り切れる、最小公倍数で割り切れる
    return A-D-E+F#包除原理
ans = count(b, c, d) - count(a-1, c, d)
#A以上B以下の整数のうち、CでもDでも割り切れないものの個数
#Aを引く１することで、A以上が分かる
#if(a % c != 0 and a % d != 0):
    #ans += 1#AがCでもDでも割り切れないなら、足す１
print(ans)