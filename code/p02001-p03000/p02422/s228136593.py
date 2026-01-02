def Print(st,a,b):
    print(st[a:b])
    
def Reverse(st,a,b):
    rev = st[a:b]
    st = st[:a] + rev[::-1] + st[b:]
    
    return st

def Replace(st,a,b,p):
    rep = str(p)
    st = st[:a] + rep + st[b:]
    
    return st

st = input()
num = int(input())
while num > 0:
    com = input().split()
    a = int(com[1])
    b = int(com[2])
    
    if(com[0] == "print"):
        Print(st,a,b+1)
    elif(com[0] == 'reverse'):
        st = Reverse(st,a,b+1)

    elif(com[0] == 'replace'):
        p = str(com[3])
        st = Replace(st,a,b+1,p)
    num -= 1


