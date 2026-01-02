def two_int():
    N, K = map(int, input().split())
    return N,K

def one_int():
    return int(input())

def one_str():
    return input()

def many_int():
    return list(map(int, input().split()))

N,K = two_int()
R,S,P = map(int , input().split())
T=one_str()

dicts={}
dicts["r"] = R
dicts["s"] = S
dicts["p"] = P

checks=[False for i in range(N)]
hand=[]

index=0
output = []
for i in range(N):
    if T[i]=="r":
        output.append("p")
    elif T[i]=="s":
        output.append("r")
    else:
        output.append("s")

sums =0
for i in range(len(output)):
    if i <K:
        sums += dicts[output[i]]
        checks[i]=True
    else:
        if output[i]==output[i-K]:
            if checks[i-K]!=True:
                sums += dicts[output[i]]
                checks[i]=True

        else:
            sums += dicts[output[i]]
            checks[i]=True


print(sums)