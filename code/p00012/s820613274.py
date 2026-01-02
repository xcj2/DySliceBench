
def cross_product(a,b):#a,bは複素数、だけどベクトル扱いしよう
    return (a.conjugate()*b).imag

def abs_area_vector(ax,ay,bx,by):#3点(0,0)(ax,ay)(bx,by)で構成される三角形の面積の絶対値
    return abs(0.5 * (cross_product(complex(ax,ay),complex(bx,by))))

def abs_area_3point(ax,ay,bx,by,cx,cy):#3点(ax,ay)(bx,by)(cx,cy)で構成される三角形の面積の絶対値
    return abs_area_vector(bx-ax,by-ay,cx-ax,cy-ay)

try:
    while True:
        x1,y1,x2,y2,x3,y3,xp,yp = map(float,input().split())
        abc = abs_area_3point(x1,y1,x2,y2,x3,y3)
        pab = abs_area_3point(x1,y1,x2,y2,xp,yp)
        pbc = abs_area_3point(x2,y2,x3,y3,xp,yp)
        pca = abs_area_3point(x1,y1,x3,y3,xp,yp)
        #ここらへんで結構ミスあったから今度からはもっと簡潔に書けるように何か関数でも用意すべき
        print("NO" if pab * pbc * pca == 0 or abc != pab + pbc + pca else "YES")
except  (EOFError,ValueError):
    pass



