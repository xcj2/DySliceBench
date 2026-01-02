#from statistics import median
#import collections
#aa = collections.Counter(a) # list to list
#from itertools import combinations # (string,3) 3回
#
#
# pythonで無理なときは、pypyでやると正解するかも！！
#
#

mod = 10**9 + 7

def readInts():
  return list(map(int,input().split()))
def main():
    """n = int(input())
    v = []
    for i in range(n):
        v.append([])
    for i in range(n):
        A = int(input())
        for j in range(A):
            human,lie = readInts() # human : 人  lie: 1 が正直者 0 が不親切
            v[human-1].append([human - 1,lie]) # human : 0-based index
    print(v)
    def judge(bit):
        # i 人目の証言を検証する
        print(bin(bit))
        for i in range(n):
            # 証言は意味がないな
            #if not (bit & (1<<i)): # フラグのたってるやつだけみてる
                #continue
            for x,y in v[i]:
                print(x,y,bit)
                # y = 1 なのに 不親切 だったらだめ
                if y == 1 and not (bit & (1 << x)):
                    return False
                # y = 0 なのに 正直ならだめ
                if y == 0 and (bit & (1 << x)):
                    return False
        return True
    res = 0
    for bit in range(1 << n):
        if judge(bit):
            count = 0
            for i in range(n):
                if bit & (1 << i):
                    count += 1
            res = max(res,count)
    print(res)
    """
    n = int(input())
    xy = [[] for _ in range(n)]
    for i in range(n):
        A = int(input())
        for j in range(A):
            x,y = readInts()
            xy[i].append([x,y])
    ans = 0
    for b in range(1 << n):
        for m in range(n):
            if (b >> m) & 1:
                for x,y in xy[m]:
                    if y != (b >> (x-1) & 1):
                        break
                else:
                    continue
                break
        else:
            ans = max(ans,bin(b).count("1"))
    print(ans)
if __name__ == '__main__':
  main()
