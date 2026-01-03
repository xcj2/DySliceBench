def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))
n = ii()
A = iil()

cum = 0
ope = 0
# first plus case
for i,item in enumerate(A):
    cum += item
    if i%2 == 0 and cum <= 0:
        ope += abs(cum)+1
        cum = 1
    elif i%2 == 1 and cum >= 0:
        ope += cum+1
        cum = -1
#    print(cum)
tmp = ope

cum = 0
ope = 0
# first minus case
for i,item in enumerate(A):
    cum += item
    if i%2 == 1 and cum <= 0:
        ope += abs(cum)+1
        cum = 1
    elif i%2 == 0 and cum >= 0:
        ope += cum+1
        cum = -1
#print(tmp,ope)
print(min(tmp,ope))