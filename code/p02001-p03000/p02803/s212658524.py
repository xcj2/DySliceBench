import sys
from collections import deque

input = sys.stdin.readline
H,W=map(int,input().rstrip().split())
maze=[list(input().rstrip()) for i in range(H)]
def resolve():
    seen=[[0 for i in range(W)] for j in range(H)]
    ans=0
    for i in range(H):
        for j in range(W):
            if maze[i][j]=="#":
                continue
            #maze[k][l]=1#end
            buf=bfs(maze,seen,i,j)
            ans=max(ans,buf)
            seen = [[0 for i in range(W)] for j in range(H)]
            #maze[k][l]="."
    print(ans)

def bfs(maze, seen, sh, sw): #sh,swはスタート
    stack = deque([[sh, sw]])
    seen[sh][sw] = 1
    expandcount=0#今のdepthに展開されたノードを親ノードとしたときの子ノードの数
    expanded=-1#今のdepthに展開されたノード数、最初は-1にする
    popcount=0#popした数、今のdepthでの探索回数
    depth=0#ルートからの深さ
    while stack:
        h, w = stack.popleft()
        popcount+=1
        
        for j, k in ([1, 0], [-1, 0], [0, 1], [0, -1]):
            new_h, new_w = h+j, w+k
            if new_h < 0 or new_h >= H or new_w < 0 or new_w >= W:
                continue

            elif maze[new_h][new_w] != "#" and  seen[new_h][new_w] == 0:#未発見
                seen[new_h][new_w] = 1#発見済みにする
                stack.append([new_h, new_w])#隣接を探索予定に
                expandcount+=1

        if popcount==expanded or expanded==-1:#今のdepthが全て探索済みなら、下のdepthの探索に移る
            expanded=expandcount
            popcount=0
            expandcount=0
            depth+=1

    return depth-1
"""
    for i in range(H):
        for j in range(W):
            if(S[i][j]=="#"):
                for dir in range(4):
                    nx=j+dx[dir]
                    ny=i+dy[dir]

                    if(nx<0 or nx>=W):
                        continue
                    if(ny<0 or ny>=H):
                        continue

                    if(S[i][j]==S[ny][nx]):
                        break
                else:
                    print("No")
                    return
    print("Yes")
"""
import sys
from io import StringIO
import unittest

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_入力例_1(self):
        input = """3 3
...
...
..."""
        output = """4"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """3 5
...#.
.#.#.
.#..."""
        output = """10"""
        self.assertIO(input, output)

if __name__ == "__main__":
    #unittest.main()
    resolve()