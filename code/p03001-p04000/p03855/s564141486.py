from collections import Counter

N,K,L = map(int, input().split())
pq_list = []
for _ in range(K):
    pq_list.append(list(map(int, input().split())))

rs_list = []
for _ in range(L):
    rs_list.append(list(map(int, input().split())))

class UnionFind():
    def __init__(self):
        self.roots = {}
        self.ranks = {}

    def connect(self,x,y):
        root_x = self.pick_root(x)
        root_y = self.pick_root(y)
        
#         # 経路圧縮（のつもり）
#         self.roots[x] = root_x
#         self.roots[y] = root_y
        
        if not root_x == root_y:
            if self.ranks[root_x] >= self.ranks[root_y]:
                # 短い方の根を長い方の根にする
                # 等しいときはxにくっつける
                self.roots[root_y] = root_x
            else:
                self.roots[root_x] = root_y

            if self.ranks[root_x]==self.ranks[root_y]:
                # 等しいときxにくっつけると、xのランクが1増える
                self.ranks[x] += 1

    def pick_root(self,k):
        if not k in self.roots:
            self.roots[k] = k
            self.ranks[k] = 1
            return k

        k_root = self.roots[k]
        if k_root == k:
            return k
        else:
            # pick_rootで毎回見に行くのが無駄にも思えるが、いつ根ノードがくっつくかわからないので必要な気がしている
            self.roots[k] = self.pick_root(self.roots[k_root])
            return self.roots[k]
#             return self.pick_root(k_root)

UF_pq = UnionFind()
for p,q in pq_list:
    UF_pq.connect(p, q)

UF_rs = UnionFind()
for r,s in rs_list:
    UF_rs.connect(r, s)

root_tuples = []
for i in range(1,N+1):
    # rootsにないということは、一度もconnectしてないということ
    # それであれば最終的な解答ではその街は1（自分のみ）でよいので
    # (None, None)で保存しcounterを１に変更する
    if not i in UF_pq.roots:
        root_tuples.append((None,None))
        continue
    if not i in UF_rs.roots:
        root_tuples.append((None,None))
        continue
    pq_root = UF_pq.pick_root(i)
    rs_root = UF_rs.pick_root(i)
    
    # ある都市のpqのroot,rsのrootを保存。
    # これが両方共一致する都市は、「どちらでも連結している」といえる
    root_tuples.append((pq_root,rs_root))

counter = Counter(root_tuples)
counter[(None,None)] = 1

kotae_list = []
for i in range(N):
    kotae_list.append(counter[root_tuples[i]])

print(" ".join(map(str,kotae_list)))