import bisect
import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF = 10**20
def main():
    A,B,Q=mi()
    X,Y= [], []
    for i in range(A):
        X.append(ii())
    for i in range(B):
        Y.append(ii())
    
    def search_min_dist(Z,z):
        insert_i = bisect.bisect_left(Z,z)
        res = []
        m = INF
        for di in [-2,-1,0,1,2]:
            i = insert_i + di
           
            if 0<= i < len(Z):
                res.append(Z[i])

        return res


    for q in range(Q):
        x=ii()
        minX = search_min_dist(X,x)
        minY = search_min_dist(Y,x)

        ans = INF
        for mx in minX:
            for my in minY:
                min_dist_x,min_dist_y = mx,my
                if not min_dist_x < min_dist_y:
                    min_dist_x,min_dist_y = min_dist_y,min_dist_x

                _ans = 0
                if min_dist_x <= x <= min_dist_y:
                    _ans = min(min_dist_y-x,x-min_dist_x) + min_dist_y - min_dist_x
                elif x <= min_dist_x <= min_dist_y:
                    _ans = min_dist_y - x
                else:
                    _ans = -min_dist_x + x
                
    
                ans = min(ans,_ans)
        print(ans)

        

if __name__ == "__main__":
    main()