#unionfind木_集合の管理_同じ集合の数を数える場合：
#parには集合の数と親の名前を同時にメモ化する（根なら-size, 子なら親）
def find(k):#要素k
    if par[k] < 0:#初期はparがすべて負の値
        return k
    else:
        par[k] = find(par[k])
        return par[k]

def unite(i, j):
    i = find(i)
    j = find(j)
    if i==j:#すでに同じ集合
        return False
    else:
        #sizeが大きい方がi
        if i > j:#sizeはマイナス管理なので、i>jの時jの方がサイズが大きい
            i, j = j, i
        par[i] += par[j] #親は負の値で大きくなる
        par[j] = i
        return True

def size(x):
    return -par[find(x)]

n, m = map(int, input().split())

par = [-1]*n#初めは自分自身が親

for i in range(m):
    a, b = map(lambda x:int(x)-1, input().split())
    unite(a, b)

ans = 0
for i in range(n):
    if -par[i]>0:
        ans += 1
print(ans-1)

