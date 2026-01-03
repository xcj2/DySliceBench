def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(list(enumerate(a)), key=lambda x: -x[1])

    class unionfind():
        # size:要素数,tree：unionfind木
        def __init__(self, size):  # self,要素数
            self.size = size
            self.tree = [i for i in range(self.size)]  # root,depth

        # rootを探す
        def root(self, index):
            temp_list = []
            temp = self.tree[index]
            while index != temp:
                temp_list.append(index)
                index = temp
                temp = self.tree[index]
            for i in temp_list:
                self.tree[i] = index
            return index

        # 結合
        def unite_r(self, index1, index2):
            r1 = self.root(index1)
            r2 = self.root(index2)
            if r1 < r2:
                self.tree[r1] = r2
            else:
                self.tree[r2] = r1

        def unite_l(self, index1, index2):
            r1 = self.root(index1)
            r2 = self.root(index2)
            if r1 > r2:
                self.tree[r1] = r2
            else:
                self.tree[r2] = r1

        # 同じか判定
        def same(self, index1, index2):
            r1 = self.root(index1)
            r2 = self.root(index2)
            return r1 == r2

    ur = unionfind(n+2)
    ul = unionfind(n+2)
    vis = [False]*(n+2)
    ans = 0
    for i, j in a:
        vis[i+1] = True
        if vis[i+2]:
            ur.unite_r(i+1, i+2)
            ul.unite_l(i+1, i+2)
        if vis[i]:
            ur.unite_r(i, i+1)
            ul.unite_l(i, i+1)
        ans += j*(ur.root(i+1)-i)*(i+2-ul.root(i+1))
    print(ans)


main()
