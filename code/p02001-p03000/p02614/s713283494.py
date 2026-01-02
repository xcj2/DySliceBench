def countRowColumn(color):
    blackr = []
    for i in range(row):
        blackr.append(color[i].count('#'))
    blackc = []
    for i in range(col):
        c = 0
        for j in range(row):
            if color[j][i]=='#':
                c+=1
        blackc.append(c)
    
def counting(color):
    t=0
    for c in color:
        t+=c.count('#')
    return t
def func(color,setr,setc,r,c):
    counts = counting(color)
    if counts<k:
        return 0
    if counts==k:
        dp.add((tuple(sorted(setr)),tuple(sorted(setc))))
    #if r==row or c==col:
    #    return 0
    for i in range(r,row):
        temp = []
        for j in range(col):
            temp+=[color[i][j]]
            color[i][j]='R'
        setr.add(i)
        func(color,setr,setc,i+1,c)
        setr.remove(i)
        for j in range(col):
            color[i][j]=temp[j]
    for j in range(c,col):
        temp = []
        for i in range(row):
            temp+=[color[i][j]]
            color[i][j]='R'
        setc.add(j)
        func(color,setr,setc,r,j+1)
        setc.remove(j)
        for i in range(row):
            color[i][j]=temp[i]
    return 0
    
dp = set()
row, col, k = map(int,input().split())
color = []
blackr = []
for _ in range(row):
    color.append(list(input()))
    blackr.append(color[-1].count('#'))
blackc = []
for i in range(col):
    c = 0
    for j in range(row):
        #print(j,i)
        if color[j][i]=='#':
            c+=1
    blackc.append(c)
total = sum(blackr)
#print(total)
if total<k:
    print(0)
else:
    func(color,set(),set(),0,0)
    print(len(dp))