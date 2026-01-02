import bisect, collections

def helper(n, d, cur):
    if (n, cur) in d:
        return d[(n, cur)]
    if n == 1:
        return [chr(ord('a')+i) for i in range(0, min(25, cur+1)+1)]
    res = []
    for i in range(0, min(25, cur+1)+1):
        for x in helper(n-1, d, max(cur, i)):
            res.append(chr(ord('a')+i)+x)
    d[(n, cur)] = res
    return res

def solution():
    N = int(input().strip())
    res = []
    d = collections.defaultdict(list)
    for x in helper(N, d, -1):
        print(x)
    


def main():    
    # T = int(input().strip())
    for _ in range(1):
        solution()
    

main()