#import collections
#aa = collections.Counter(a) # list to list
#from itertools import combinations # (string,3) 3回

mod = 10**9 + 7

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def readInts():
  return list(map(int,input().split()))
def search(S,y,x,h,w):
    #全探索で間に合うべ
    cnt = 0
    #print(y,x)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        #print('nya',ny,nx)
        if 0 <= nx < w and 0 <= ny < h:
            #print('here',nx,ny)
            if S[ny][nx] == '#':
                cnt += 1
    #print(cnt)
    if cnt == 0:#隣接する#が一つもない
        return False
    else:
        return True

def main():
    h,w = readInts()
    S = [input() for _ in range(h)]
    #print(S)
    for i in range(h):
        for j in range(w):
            if S[i][j] == '#':
                #print(i,j)
                if search(S,i,j,h,w):
                    pass
                else:
                    print('No')
                    exit()
    print('Yes')


if __name__ == '__main__':
  main()
