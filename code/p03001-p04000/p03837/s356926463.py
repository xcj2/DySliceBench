#設定
import sys
input = sys.stdin.buffer.readline

#ライブラリインポート

#入力受け取り
def getlist():
	return list(map(int, input().split()))

def warshall_floyd(d, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

#処理内容
def main():
	n,w = map(int,input().split())
	d = [[float("inf") for i in range(n)] for i in range(n)]
	a = []
	b = []
	weight = []
	for i in range(w):
		x,y,z = map(int,input().split())
		a.append(x - 1)
		b.append(y - 1)
		weight.append(z)
		d[x - 1][y - 1] = z
		d[y - 1][x - 1] = z
		for i in range(n):
			d[i][i] = 0
	d = warshall_floyd(d, n)
	ans = 0
	for i in range(w):
		if d[a[i]][b[i]] < weight[i] :
			ans += 1
	print(ans)

if __name__ == '__main__':
	main()