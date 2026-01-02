import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

ans = 0
def main():
    H, W, K = map(int, readline().split())
    grid = []
    for _ in range(H):
        grid.append(list(input()))

    #再帰関数で二組の全bit探索を組む 
    #リストをコピーしない方法
    bitr = [0 for _ in range(H)]
    bitc = [0 for _ in range(W)]
    
    def dfsr(i): 
        if i == H:
            dfsc(0)
            return
        dfsr(i+1)
        bitr[i] = 1
        dfsr(i+1)        
        bitr[i] = 0
    
    def dfsc(i):
        global ans
        cnt = 0
        if i == W:
            #ここで処理をおこなう
            for j in range(H):
                #1が立っているならその行は全て赤とするので飛ばす
                if bitr[j] == 1: 
                    continue
                for k in range(W):
                    #1が立っているならその列は全て赤とするので飛ばす
                    if bitc[k] == 1:
                        continue
                    #飛ばされなかったマスのうち黒の数を数える
                    if grid[j][k] == '#':
                        cnt += 1
            if cnt == K:
                ans += 1
            return
        dfsc(i+1) 
        bitc[i] = 1
        dfsc(i+1)
        bitc[i] = 0
    
    dfsr(0)
    print(ans)
if __name__ == '__main__':
    main()
