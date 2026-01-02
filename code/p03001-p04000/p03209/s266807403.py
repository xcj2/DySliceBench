bargarls = [0]*51;patyls = [0]*51
def bargar(n):
        global bargarls
        if n==1:
                bargarls[n-1] = 1
                return 1
        else:
                num = 2*bargar(n-1) + 3
                bargarls[n-1] = num
                return num
def paty(n):
        global patyls
        if n == 1:
                patyls[n-1] = 1
                return 1
        else:
                num = 2*paty(n-1) + 1
                patyls[n-1] = num
                return num
bargar(51)
paty(51)
def ans(n,x):
        global patyls 
        global bargarls
        if n >= x:return 0
        elif (bargarls[n]+1)//2 > x:return ans(n-1,x-1)
        elif (bargarls[n]+1)//2 == x:return (patyls[n]+1)//2
        elif bargarls[n] == x:return patyls[n]
        else:return (patyls[n]+1)//2 + ans(n-1,x-(bargarls[n]+1)//2)
n,x = map(int,input().split())
print(ans(n,x))