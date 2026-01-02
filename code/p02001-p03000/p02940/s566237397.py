n=int(input())
S=input().strip()
mod = 998244353
def mul(a, b):
    return (a * b) % mod

ff = 1
for i in range(n):
    ff=mul(ff, i+1)

def mkrgb():
    return {"R":0,"G":0,"B":0}

def ogb(c):
    if c == "R":
        return "GB"
    if c == "G":
        return "BR"
    if c == "B":
        return "RG"

cc={"R":0,"G":0,"B":0}
cc2={"R":0,"G":0,"B":0}
t=0
l=""
result = 1
for c in S:
    if cc2[c] != 0:
        result = mul(result, cc2[c])
        cc2[c]-=1
    elif cc[c] == 0:
        x,y = ogb(c)
        if cc[x] != 0:
            cc2[y] += 1
            result = mul(result, cc[x])
            cc[x] -= 1
        elif cc[y] != 0:
            cc2[x] += 1
            result = mul(result, cc[y])
            cc[y] -= 1
        else:
            cc[c]+=1
    else:
        cc[c] += 1
#    print(cc,cc2, result)

print(mul(result,ff))


