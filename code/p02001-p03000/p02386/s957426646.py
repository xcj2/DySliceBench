#ITP1_11-D Dice 4
store=[]
str=["N","S","E","W"]
rep={
    "N":[4,0,2,3,5,1],
    "S":[1,5,2,3,0,4],
    "E":[2,1,5,0,4,3],
    "W":[3,1,0,5,4,2]
}

def rotate_dice(b,s):
    result = [0,0,0,0,0,0]
    for i in range(6):
        result[i]=b[rep[s][i]]
    return result
    
def generate(b):
    if (b in store)==False:
        store.append(b)
        for s in str:
            generate(rotate_dice(b,s))

def check(a,b):
    generate(b)
    if a in store:
        return False
    else:
        return True

n=int(input())
dices=[0]*n
for i in range(n):
    dices[i]=input().split()
result = 1
i=0
while i < n-1:
    j=i+1
    while j < n:
        r = check(dices[i],dices[j])
        store = []
        result *= r
        j+=1
    i+=1

if result == 1:
    print("Yes")
else:
    print("No")