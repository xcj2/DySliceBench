'''
いちばん簡単なのは建物とフロアごとにリスト作って、足し引き
'''


#部屋、フロア、建物をクラスで定義。まあ、クラスにしなくてもいいんだけど

a = int(input())

n = 10
m = 3
o = 4
h = [
        [
            [0 for i in range(n)] 
         for j in range(m)] 
    for k in range(o)]


#w, x, y, z = 3, 1, 8, 4
for i in range(a):
    w,x,y,z = map(int, input().split())
    h[w-1][x-1][y-1] += z

#print(h[1][1])
#建物と建物仕切り
def makeFence():
    fence = '#' * 20
    print(fence)

#部屋を表示する関数
def showRoom(f):
    for k in range(len(f)-1):
        print(' ' + str(f[k]), end='')
    print(' ' + str(f[len(f)-1]))

#フロアを表示する関数
def showFloor(b):
    j = 0
    while j < len(b):
        f = b[j]
        showRoom(f)
        j += 1

def statusShow(h):
    for i in range(len(h)-1):
        b = h[i]
        showFloor(b)
        makeFence()
    showFloor(h[len(h)-1])

statusShow(h) 

   
#b = statusShow(h)
#makeFence()
#print(b)



