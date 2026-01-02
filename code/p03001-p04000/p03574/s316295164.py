def fa():  # final answer
    global ans
    print(ans)


def getN():
    return int(input())


def getNM():
    return map(int, input().split())


def getList():
    return list(map(int, input().split()))

def check_mine(i,j,place):
    if place[i][j] == "#":
        return "#"

    num = 0
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            try:
                if place[x][y] == "#":
                    if x >= 0 and y >= 0:
                        num += 1
            except:
                pass

    return str(num)

h, w = getList()

place = []
for i in range(h):
    place.append(input())


for i in range(h):
    ans = []
    for j in range(w):
        ans.append(check_mine(i,j,place))
    print("".join(ans))