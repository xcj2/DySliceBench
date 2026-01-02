def main():
    h,w=map(int,input().split())
    s=[]
    for i in range(h):
        ss=input()
        s.extend(ss)
    mat = [[float("INF")] * (h*w) for i in range(h*w)]
    for i,a in enumerate(s):
        if a == '.':
            mat[i][i] = 0
            makemat(i,mat,h,w,s)
    # mtemp = mat
    # for i , a in enumerate(mat):
    #     print(a)
    for i,a in enumerate(s):
        if a == '.':

            caldist(mat,w*h)
            break
    ans = 0
    # print(mat)
    # for i, a in enumerate(mat):
    #     print(a)
    #     ans = max(ans, max(a))
    print(calans(mat))
def calans(m):
    temp = 0
    for i,w in enumerate(m):
        for j, s in enumerate(w):
            if s != float("INF"):
                temp = max(temp,s)
    return temp
# 隣接行列m作成
def makemat(i,m,h,w,s):

    if (i % w) + 1 != w:
        if s[i+1] == '.':
            j = i+1
            m[i][j] = 1
            m[j][i] = 1
        # else:
        #     j = i+1
        #     m[i][j] = float('INF')
        #     m[j][i] = float('INF')
    if (i % w)  != 0:
        if s[i-1] == '.':
            j = i-1
            m[i][j] = 1
            m[j][i] = 1
        # else:
        #     j = i-1
        #     m[i][j] = float('INF')
        #     m[j][i] = float('INF')
    if i > w:
        if s[i-w] == '.':
            j=i-w
            m[i][j] = 1
            m[j][i] = 1
        # else:
        #     j = i-w
        #     m[i][j] = float('INF')
        #     m[j][i] = float('INF')
    if i < h*w - w:
        if s[i+w] == '.':
            j=i+w
            m[i][j] = 1
            m[j][i] = 1
        # else:
        #     j = i+w
        #     m[i][j] = float('INF')
        #     m[j][i] = float('INF')

def caldist(m,l):
    for i in range(l):
        for j in range(l):
            for k in range(l):
                m[j][k] = min(m[j][k],m[j][i]+m[i][k])


if __name__=='__main__':
    main()
