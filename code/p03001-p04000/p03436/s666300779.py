import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    h,w = LI()
    board = [["#" for _ in range(w+2)]]
    num = 0
    for _ in range(h):
        line = ["#"] + list(S()) + ["#"]
        num += line.count(".")
        board.append(line)
    board.append(["#" for _ in range(w+2)])
    
    queue = collections.deque([(1,1)])
    explored = {(1,1)}
    nbh = [[0,1],[0,-1],[1,0],[-1,0]]
    level = 0
    cnt = 0
    
    while len(queue)!=0 and (h,w) not in explored:
        if cnt==0:
            level+=1
            cnt=len(queue)
        nxt = queue.popleft()
        for dx,dy in nbh:
            ex = (nxt[0]+dx, nxt[1]+dy)
            if board[ex[0]][ex[1]] == ".":
                if ex not in explored:
                    explored.add(ex)
                    queue.append(ex)
        cnt -= 1
    ans = num-(level+1) if (h,w) in explored else -1
    print(ans)
main()            
