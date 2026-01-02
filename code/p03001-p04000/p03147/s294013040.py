def q1():
    a,b,c = map(int, input().split(" "))
    r = int(a*b/2)
    print(r)

def q2():
    def f(n):
        if n%2 == 0:
            return n//2
        else:
            return 3*n+1
    def solver(v):
        ary = []
        for i in range(10**6):
            if i == 0:
                ary.append(v)
            else:
                v = f(ary[-1])
                if v in ary:
                    return i+1
                else:
                    ary.append(v)
    s = int(input())
    print(solver(s))


"""
1. 最低値を数える (1)
2. 配列全体から最低値を減算する
3. 0で配列を分割する
4. 分割した配列に1～の処理を行う
5. 配列の長さが0になったら終わる
6. 全ての最低値を足した値が答え
"""
n = int(input())
h = list(map(int, input().split(" ")))

def water(ary):
    # 5
    if len(ary) == 0:
        return 0
    elif len(ary) == 1:
        return ary[0]

    # 1
    m = min(ary)
    #print("min = %d" % m)
    # 2
    new_ary = list(map(lambda x:x-m, ary))
    # 3
    tmp = []
    multi_ary = []
    for n in new_ary:
        if n != 0:
            tmp.append(n)
        else:
            multi_ary.append(tmp)
            tmp = []
    else:
        multi_ary.append(tmp)
    #print("%s -> %s -> %s" % (ary, new_ary, multi_ary))
    # 4
    cnt = sum(map(water, multi_ary))
    # 6
    #print("%d + %d" % (cnt,m))
    return cnt +m

print(water(h))
