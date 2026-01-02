h,w=map(int,input().split())
maze=[input() for i in range(h)]
class UnionFind:
    #def   -> foo=UnionFind(n,1)  <- 1-based index, default is 0
    #method -> foo.hoge(huga)
    __slots__ = ["_size", "_first_idx", "_parents"]
    def __init__(self, size: int, first_index: int = 0) -> None:
        self._size = size
        self._first_idx = first_index
        self._parents = [[0,0,1] for i in range(size + first_index)]
        for i in range(size):
            self._parents[i][int(maze[i//w][i%w]==".")]=1
    def find(self, x: int) -> int:
        try:
            if type(self._parents[x]) is list:
                return x
        except IndexError:print(x);exit()
        self._parents[x] = self.find(self._parents[x])
        return self._parents[x]
    def same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
    def unite(self, x: int, y: int) -> bool:
        x, y = self.find(x), self.find(y)

        if x == y:
            return False
        if self._parents[x][2] < self._parents[y][2]:
            x, y = y, x
        self._parents[x] = [self._parents[x][i]+self._parents[y][i] for i in range(3)]
        self._parents[y] = x
        return True
ans=0
m=[(0,1),(0,-1),(1,0),(-1,0)]
uf=UnionFind(h*w)
for i in range(h):
    for j in range(w):
        for dx,dy in m:
            if 0<=dx+i<h and 0<=dy+j<w and maze[i][j]!=maze[i+dx][j+dy]:
                uf.unite(i*w+j,(i+dx)*w+j+dy)
for i in uf._parents:
    if type(i)is list:ans+=i[0]*i[1]
print(ans)