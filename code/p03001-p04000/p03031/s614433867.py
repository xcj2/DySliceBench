def getN():
    return int(input())

def getMN():
    return list(map(int, input().split()))

def getlist():
    return list(map(int, input().split()))

n, m = getMN()

sws = []
for i in range(m):
    sw = getlist()
    sws.append(sw[1:])
ans = 0
mods = getlist()
# パターンごと
for i in range(2**n):
    flags = bin(i)[2:]
    flags = "0"*(n-len(flags)) + flags

    # 電球ごと
    right = 0
    for idx, sw in enumerate(sws):
        tmp = 0
        # スイッチごと
        for s in sw:
            if flags[s-1] == "1":
                tmp +=1

        if tmp % 2 == mods[idx]:
            right += 1

        if right == m:
            ans += 1
print(ans)