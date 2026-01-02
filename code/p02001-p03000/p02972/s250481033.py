def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
n = getN()
nums = getList()


yaku = [[] for i in range(n + 1)]

for i in range(1, n//2 + 2):
    for j in range(2, n//i + 1):
        yaku[i*j].append(i)

# print(yaku)
ans = [0 for i in range(n)]
# print(nums)
for i in range(n):
    tmp = n - i
    if ans[tmp - 1] != nums[tmp - 1]:
        ans[tmp - 1] = 1
        for y in yaku[tmp]:
            ans[y-1] = (ans[y-1] + 1) % 2
    else:
        ans[tmp - 1] = 0
    # print(tmp, ans)

# print(ans)
pr = [i + 1 for i, x in enumerate(ans) if x == 1]
# print(pr)
print(len(pr))
print(" ".join(list(map(str, pr))))

