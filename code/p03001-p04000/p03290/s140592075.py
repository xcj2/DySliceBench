#from statistics import median
#import collections
#aa = collections.Counter(a) # list to list
#from itertools import combinations # (string,3) 3回

mod = 10**9 + 7

def readInts():
  return list(map(int,input().split()))
d,g = readInts()
cl = [readInts() for _ in range(d)]
ans = float("inf")
def dfs(i,sum,count,nokori):
    global ans
    #まだ解いてない配点をnokori
    if i == d:
        # G点に満たなければ nokoriのうち1番大きい物を解く
        if sum < g:
            use = max(nokori)
            # 解く問題が問題数を超えないように注意
            n = min(cl[use - 1][0], -(-(g-sum) // (use * 100)))
            count += n
            sum += n * use * 100
        if sum >= g:
            ans = min(ans,count)
    else:
        dfs(i + 1, sum, count, nokori)
        #print(i+1,nokori,nokori - {i+1})
        dfs(i + 1, sum + cl[i][0] * (i + 1) * 100 + cl[i][1], count + cl[i][0], nokori - {i + 1})

def main():


    dfs(0,0,0,set(range(1,d+1)))
    print(ans)




if __name__ == '__main__':
  main()
