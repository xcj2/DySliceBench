from  collections import  deque
H , W = map(int, input().split())
mp = []
for i in range(H):
    mp.append(list(input()))


class node():
    def __init__(self):
        self.wall = 0
        self.reaf = []
        self.tansaku = 0
        self.cost = 0


nodelist = [node() for i in range(H * W)]
count = 0
for i in range(len(mp)):
    for j in range(len(mp[i])):
        if mp[i][j] == "#":
            nodelist[count].wall = 1
        count += 1
count2 = 0
for i in range(len(nodelist)):

    if count2 != 0:
        if nodelist[i-1].wall == 0:
            nodelist[i].reaf.append(i-1)
    if count2 != W-1:
        if nodelist[i+1].wall == 0:
            nodelist[i].reaf.append(i+1)
    if i+W < len(nodelist):
        if nodelist[i+W].wall == 0:
            nodelist[i].reaf.append(i+W)
    if i-W >= 0:
        if nodelist[i-W].wall == 0:
            nodelist[i].reaf.append(i-W)

    count2 += 1
    if count2 == W:
        count2 = 0

def tansaku(nodelist,que):
    data = que.popleft()
    for j in nodelist[data].reaf:
        if nodelist[j].tansaku == 0:
            que.append(j)
            nodelist[j].tansaku = 1
            nodelist[j].cost = nodelist[data].cost + 1
    if len(que) != 0:
        tansaku(nodelist, que)


def nodereset(nodelist):
    for i in range(len(nodelist)):
        nodelist[i].tansaku = 0
        nodelist[i].cost = 0
    return nodelist

maxnum = 0

for i in range(len(nodelist)):
    if nodelist[i].wall == 0:
        nodelist = nodereset(nodelist)
        que = deque()
        que.append(i)
        nodelist[i].tansaku = 1
        tansaku(nodelist, que)
        for j in range(len(nodelist)):
            if nodelist[j].cost > maxnum:

                maxnum = nodelist[j].cost
print(maxnum)
