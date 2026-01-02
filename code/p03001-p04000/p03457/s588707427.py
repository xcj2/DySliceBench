import math
def get_while(n):
    ts = [0]
    ans = [[0, 0]]
    for _ in range(n):
        s = list(map(lambda x: int(x), input().split(" ")))
        ts.append(s[0])
        ans.append([s[1], s[2]])
    return ts, ans

def get_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def solve(ts, ps, n):
    for x in range(n):
        d = get_distance(ps[x], ps[x+1])
        if ((ts[x+1] - ts[x]) - d) < 0:
            return "No"
        if ((ts[x+1] - ts[x]) - d) % 2 != 0:
           return "No"
    return "Yes"
        

if __name__ == '__main__':
    n = int(input())
    ts, ps = get_while(n)
    print(solve(ts, ps, n))
