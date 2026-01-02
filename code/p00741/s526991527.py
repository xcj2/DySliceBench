import sys #追加
sys.setrecursionlimit(500*500) #再起上限回数突破

class Node:
    def __init__(self, data):
        self.data = data
        self.f_search = False
        
    def __repr__(self):
        return str(self.data) + "," + str(self.f_search)
        

data_set = list()

while(1):
    w, h = map(int, input().split() )
    if w == 0 and h == 0:
        break

    aa = list()
    for _ in range(h):
        a = list()
        for d in map(int, input().split() ):
            a.append(Node(d))
        aa.append(a)

    data_set.append(aa)


search_vec = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,1), (1,-1), (-1,-1)]

iland_cnt = 0
def search_iland(iland_data):
    global iland_cnt
    for y in range(len(iland_data)):
        for x in range(len(iland_data[0])):
            if iland_data[y][x].f_search == True \
            or iland_data[y][x].data == 0:
                continue
            iland_cnt += 1
            iland_data[y][x].f_search = True
            for (dx,dy) in search_vec:
                if x+dx < 0 or y+dy < 0 \
                or x+dx >= len(iland_data[0]) \
                or y+dy >= len(iland_data): continue
                search_iland_area(iland_data, x+dx, y+dy)
            
            

def search_iland_area(iland_data, sx, sy):  
    if iland_data[sy][sx].f_search == True \
    or iland_data[sy][sx].data == 0:
        return 
    iland_data[sy][sx].f_search = True
    for (dx,dy) in search_vec:
        if sx+dx < 0 or sy+dy < 0 \
        or sx+dx >= len(iland_data[0]) \
        or sy+dy >= len(iland_data): continue
        search_iland_area(iland_data, sx+dx, sy+dy)
            
for iland in data_set:
    iland_cnt = 0
    search_iland(iland)
    print(iland_cnt)

