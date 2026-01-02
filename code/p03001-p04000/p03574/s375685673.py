def myAnswer(H:int,W:int,S:list) -> None:
   XY = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
   index = []
   ans = [[0]*W for _ in range(H)]
   for i in range(H):
      for j in range(W):
         if(S[i][j] == "#"):
            ans[i][j] = "#"
            index.append([i,j])
   for i,j in index:
      for x,y in XY:
         if(0 > (j + x) or (j + x) >= W or 0 > (i + y) or (i + y) >= H):
            continue
         elif(ans[y+i][x+j]== "#"):
            continue
         else:
            ans[y + i][x + j] += 1
   for a in ans:
      string = ""
      for s in a:
         string += str(s)
      print(string)

def modelAnswer(H:int,W:int,S:list) -> int:
   dx = [1,0,-1,0,1,-1,-1,1]
   dy = [0,1,0,-1,1,1,-1,-1]
   for i in range(H):
      for j in range(W):
         if(S[i][j] == "#"):continue

         num = 0
         for d in range(8):
            ni = i + dy[d]
            nj = j + dx[d]
            if(ni < 0 or H <= ni):continue
            if(nj < 0 or W <= nj):continue
            if(S[ni][nj] == "#"): num+=1
         
         S[i][j] = str(num )
   for s in S:
      ans = ""
      for a in s:
         ans += a
      print(ans)
def main():
   H,W = map(int,input().split())
   S = [list(input()) for _ in range(H)]
   myAnswer(H,W,S[:])
if __name__ == '__main__':
   main()