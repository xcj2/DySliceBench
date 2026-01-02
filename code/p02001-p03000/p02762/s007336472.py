def init(n) :  #n要素で初期化
	for i in range(n) :
		par[i] = i;
		rank[i] = 0;
		siz[i] = 1;

def root(x) :  #木の根を求める
	if par[x] == x :  #根
		return x;
	else :
		par[x] = root(par[x]);  #経路圧縮
		return par[x];

def same(x,y) :  #xとyが同じ集合に属するか否か
	return root(x) == root(y);

def unite(x,y) :  #xとyの属する集合を併合
	x = root(x);
	y = root(y);
	if x == y :
		return;
	if siz[x] < siz[y] :
		x,y = y,x;
	siz[x] += siz[y];
	par[y] = x;

def size(x) :
	return siz[root(x)];


nmk = input().split(' ');
n = int(nmk[0]);
m = int(nmk[1]);
k = int(nmk[2]);

par = [0]*n
rank = [0]*n
siz = [0]*n
init(n);

fre = [[0]*2 for i in range(m)];
bro = [[0]*2 for i in range(k)];
fb = [0]*n;

for i in range(m) :
	ab = input().split(' ');
	unite(int(ab[0])-1,int(ab[1])-1);
	fb[int(ab[0])-1] += 1;
	fb[int(ab[1])-1] += 1;
	fre[i][0] = int(ab[0]);
	fre[i][1] = int(ab[1]);

for i in range(k) :
	ab = input().split(' ');
	bro[i][0] = int(ab[0]);
	bro[i][1] = int(ab[1]);

for i in range(k) :
	if root(bro[i][0]-1) == root(bro[i][1]-1) :
		fb[bro[i][0]-1] += 1;
		fb[bro[i][1]-1] += 1;

print(size(0)-fb[0]-1,end='');
for i in range(1,n) :
    print('',size(i)-fb[i]-1,end='');
print();
