n = input()
k = int(input())

def solve1(n):
    l = len(n)
    if l > 0:
        return int(n[0]) + 9 * (l-1)
    else:
        return 0

def solve2(n):
    l = len(n)
    if l > 1:
        ret = (int(n[0]) - 1) * 9 * (l-1) + 9 * 9 * (l - 1) * (l - 2)  // 2
        n = n[1:]
        while (n[0] == "0"):
            if (n == "0"):
                n = ""
                break
            
            n = n[1:]
        return ret + solve1(n)
    else:
        return 0

def solve3(n):
    l = len(n)
    if l > 2:
        ret = (int(n[0])-1) * 9 * 9 * (l - 1) * (l - 2) // 2 + 9 * 9 * 9 * (l - 1) * (l - 2) * (l - 3) // 6
        n = n[1:]
        while (n[0] == "0"):
            
            if (n == "0"):
                n = ""
                break
            n = n[1:]
        return ret + solve2(n)
    else:
        return 0

if k == 1:
    print(solve1(n))
elif k == 2:
    print(solve2(n))
else:
    print(solve3(n))
    