import queue
import time

N=3
N2=9
diry=[0,1,0,-1]
dirx=[1,0,-1,0]
pos=[[2,2],[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1]]
move=[[1,3],[0,2,4],[1,5],[0,4,6],[1,3,5,7],[2,4,8],[3,7],[4,6,8],[5,7]]

class Puzzle:
    board=""
    space=0

    def __init__(self,board,space):
        self.board=board
        self.space=space

    #盤面を表示
    def showBoard(self):
        for i in range(N2):
            if self.board[i]!=0:
                print(self.board[i],end=' ')
            else:
                print('  ',end='')
            if i%3==2:
                print()
        print()

class State:
    pz=None
    g=0
    h=0
    f=0
    pr=None

    def __init__(self,pz,g,h=0,pr=None):
        self.pz=pz
        self.g=g
        self.h=h
        self.f=g+h
        self.pr=pr

    #初期盤面から1手ずつ表示
    def showRoot(self):
        if self.pr!=None:
            self.pr.showRoot()
        self.pz.showBoard()

    def __lt__(self,other):
        if self.f==other.f:
            return self.g>other.g
        return self.f<other.f

#正解とのマンハッタン距離
def h2(p):
    count=0
    for i in range(N2):
        n=int(p.board[i])
        count+=abs(pos[n][0]-i//N)+abs(pos[n][1]-i%N)
    return count

#h1を用いたヒューリスティック探索
def heuristic(pz,h):
    closedList=set()
    s=State(pz,0,h(pz),None)
    q=queue.PriorityQueue()
    q.put(s)
    while not q.empty():
        s=q.get()
        if s.pz.board in closedList:
            continue
        if s.pz.board=='123456780':
            return s.g
        space=s.pz.space
        for next in move[space]:
            nb=list(s.pz.board)
            nb[space],nb[next]=nb[next],nb[space]
            newb=''.join(nb)
            if not newb in closedList:
                np=Puzzle(newb,next)
                ns=State(np,s.g+1,h(np),s)
                q.put(ns)
        closedList.add(s.pz.board)
    return -1

#初期盤面の読み込み
s=''
for i in range(3):
    s+=input()
initialBoard=s.replace(' ','')

#空白の設定
space=initialBoard.find('0')

#Puzzleオブジェクトの作成
initialPuzzle=Puzzle(initialBoard,space)

if initialBoard=='123456780':
    print(0)
else:
    print(heuristic(initialPuzzle,h2))

