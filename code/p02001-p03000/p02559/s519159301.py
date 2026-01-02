def main():
    N, Q = map( int, input().split())
    A = list( map( int, input().split()))
    bit = [0]*N
    def add(bit,a,w):#リストに値を追加する関数
        x = a
        while x <= N:
            bit[x-1] += w
            x += x&(-x)

    def sums(bit,a):#k番目までの和
        x = a
        S = 0
        while x > 0:
            S += bit[x-1]
            x -= x&(-x)
        return S

    for i, a in enumerate(A):
        add(bit,i+1,a)
    Q = [ tuple( map( int, input().split())) for _ in range(Q)]
    ANS = []
    for q,p,x in Q:
        if q == 0:
            add(bit,p+1,x)
        else:
            ANS.append( sums(bit,x)-sums(bit,p))
    print( "\n".join( map( str, ANS)))
if __name__ == '__main__':
    main()
