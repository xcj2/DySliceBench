import sys
import itertools
input = sys.stdin.readline
 
def SI(): return str(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
   
    H, W, K = MI()
    grid = [SI().rstrip('\n') for _ in range(H)]

    n = H + W
    ans = 0
    
    for i in itertools.product(range(2),repeat = H):
        for j in itertools.product(range(2),repeat = W):
            count = 0
            for k in range(H):
                if i[k] == 1:
                    continue
                for l in range(W):
                    if j[l] == 1:
                        continue
                    if grid[k][l] == "#":
                        count += 1
            if count == K:
                ans +=1
    print(ans)
main()