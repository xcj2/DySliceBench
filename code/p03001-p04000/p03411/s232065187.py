def MI(): return map(int, input().split())
def II(): return int(input())
def IS(): return input()
def LI(): return list(map(int, input().split()))


n = II()
reds = [LI() for i in range(n)]
blues = [LI() for i in range(n)]
count = 0

blues.sort(key=lambda x: x[0])

for blue in blues:
    tmps = []
    for red in reds:
        if blue[0] > red[0]:
            tmps.append(red)
    tmps.sort(key=lambda x: x[1], reverse=True)
    for tmp in tmps:
        if blue[1] > tmp[1]:
            count += 1
            reds.pop(reds.index(tmp))
            break
print(count)
