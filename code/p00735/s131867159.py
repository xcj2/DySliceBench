from math import floor
# 約数全列挙(ソート済み)
# n = 24 -> [1,2,3,4,6,8,12,24]
def divisor(n):
    left = [1]
    right = [n]
    sup = floor(pow(n,1/2))
    for p in range(2,sup+1):
        if n % p == 0:
            if p == n//p:
                left.append(p)
                continue
            left.append(p)
            right.append(n//p)
    res = left + right[::-1]
    return res

ans_list = []

def main():
    while True:
        ans = solve()
        if ans == "end":
            break
        ans_list.append(ans)
    
    for ans in ans_list:
        print(ans)

def solve():
    n = int(input())
    if n == 1:
        return "end"
    cand = [c for c in divisor(n) if c % 7 in (1,6)]
    ans = "{}:".format(n)
    for c in cand:
        flag = True
        for p in [p for p in divisor(c) if p % 7 in (1,6)]:
            if p not in (1,c):
                flag = False
                break
        if c > 1 and flag is True:
            ans += " {}".format(c)
    return ans

main()
