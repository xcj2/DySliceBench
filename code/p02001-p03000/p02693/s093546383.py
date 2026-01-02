

############ ---- USER DEFINED INPUT FUNCTIONS ---- ############
def inp():
    return(int(input().rstrip()))
def inlt():
    return(list(map(int,input().rstrip().split())))
def insr():
    s = input().rstrip()
    return(s[:len(s) - 1])
def invr():
    return(map(int,input().rstrip().split()))
################################################################
k = inp()
a,b = invr()

for i in range(a,b + 1):
    if i%k == 0:
        has = True
        break
else:
    has = False
if has:
    print('OK')
else:
    print('NG')
#print('Yes' if '7' in n else 'No')
#print('No')
#print()
