#関数リスト
def main():
    import sys
    input = sys.stdin.readline

    def I(): return int(input())
    def MI(): return map(int, input().split())
    def LI(): return list(map(int, input().split()))
    def ruiseki(mydata):
        res = [0]*(len(mydata)+1)
        for i in range(len(mydata)):
            res[i+1] = res[i] + mydata[i]
        return res

    n, k , m = MI()
    a = ruiseki(LI())
    b = ruiseki(LI())

    result = 0
    index = k
    for i, ii in enumerate(a):
        if ii > m:
            break
        while b[index] + ii > m:
            index -= 1
        result = max(result, i+index)
    print(result)
    
main()
