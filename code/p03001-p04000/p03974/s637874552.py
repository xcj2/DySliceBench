import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

from collections import defaultdict

"""
・trie木
・各ノードから、アルファベットごとの子ノードの番号
・親ノードの番号
"""

N = int(readline())
data = tuple(read().split())
S = data[:N]
Q = int(data[N])
query_target = list(map(int,data[N+1::2]))
query_order = data[N+2::2]

class Node():
    def __init__(self,parent):
        self.parent=parent
        self.child = defaultdict(int)
        self.is_word_node = False
        self.Nword = 0 # 部分木にあるword_nodeの個数
        
    def __repr__(self):
        return 'parent:{}\nchild:{}\nNword:{}'.format(self.parent,self.child,self.Nword)

def add(word):
    n = 0
    next_idx = len(nodes)
    for x in word:
        nodes[n].Nword += 1
        c = nodes[n].child[x]
        if c == 0:
            c = next_idx
            nodes[n].child[x] = c
            nodes.append(Node(n))
            next_idx += 1
        n = c
    nodes[n].is_word_node = True
    nodes[n].Nword += 1

def solve(word):
    """
    ・wordに沿って進む。
    ・「char1<char2ならば自身より弱い文字列1個」という情報を調べる・
    ・自身のprefixの個数も調べる
    """
    data = defaultdict(int)
    prefix = 0
    n = 0
    for x in word:
        # 進む前に、他のルートの文字列数も確認する
        for k,v in nodes[n].child.items():
            if k == x:
                continue
            data[1000*k+x] += nodes[v].Nword # k<xのときの加算量
        # prefixを見つけたら加算
        if nodes[n].is_word_node:
            prefix += 1
        # 進む
        n = nodes[n].child[x]
    return data, prefix

root = Node(0)
nodes = [root]

for word in S:
    add(word)

# 同じ文字列に対するクエリを一括処理
word_to_query = [[] for _ in range(N)]
for i,x in enumerate(query_target):
    word_to_query[x-1].append(i)

answer = [0]*Q
for n,word in enumerate(S):
    if not word_to_query[n]:
        continue
    data,pref = solve(word)
    for q in word_to_query[n]:
        order = query_order[q]
        alphabet_rank = {x:i for i,x in enumerate(order)}
        rank = pref+1
        for x,v in data.items():
            a,b = divmod(x,1000)
            if alphabet_rank[a] < alphabet_rank[b]:
                rank += v
        answer[q] = rank

print('\n'.join(map(str,answer)))