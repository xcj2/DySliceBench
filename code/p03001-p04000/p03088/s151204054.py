MOD = pow(10,9) + 7
# print(MOD)
chars = ["A","C","G","T"]
dict = {
    "A":0,
    "C":1,
    "G":2,
    "T":3
}
invDict = ["A","C","G","T"]
illegalFours = []
for c in chars:
    illegalFours.append("AGC"+c)
    illegalFours.append(c+"AGC")
    illegalFours.append("ACG"+c)
    illegalFours.append(c+"ACG")
    illegalFours.append("GAC"+c)
    illegalFours.append(c+"GAC")
    illegalFours.append("AG"+c+"C")
    illegalFours.append("A"+c+"GC")
illegalFours = list(set(illegalFours))
# print(illegalFours,len(illegalFours))
def isLegal(value):
    f1,q = divmod(value,64)
    f2,q = divmod(q,16)
    f3,q = divmod(q,4)
    f4 = q
    # print(f1,f2,f3,f4)
    string = invDict[f1] + invDict[f2] + invDict[f3] + invDict[f4]
    return(string not in illegalFours)
valueIsLegal = [isLegal(i) for i in range(4**4)]
# print(sum(valueIsLegal))

def calcNextValue(value,x):
    return((value*4 + x)%256)
    
def solve(x):
    if x==3:
        return(61)
    dp = [[0 for _ in range(x+1)] for _ in range(256)]
    for value in range(256):
        if valueIsLegal[value]:
            dp[value][4] = 1
        else:
            dp[value][4] = 0
    for k in range(4,x):
        for v in range(256):
            for i in range(4):
                w = calcNextValue(v,i)
                if valueIsLegal[w]:
                    dp[w][k+1] += dp[v][k]
                    dp[w][k+1] %= MOD
    ans = 0
    for v in range(256):
        ans += dp[v][x]
        ans %= MOD
    return(ans)

N = int(input())
print(solve(N))