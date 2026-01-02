class WeightBalancedTree:
    def __init__(self, q):
        self.left = [0] * (q + 1)
        self.right = [0] * (q + 1)
        self.weight = [1] * (q + 1)
        self.key = [None] * (q + 1)
        self.last_index = 0
        self.root = 0

# key 未満の最大値
    def search_lower(self, key):
        if key == None:
            return None
        ret = None
        idx = self.root
        while idx != 0:
            if self.key[idx] < key:
                ret = self.key[idx]
                idx = self.right[idx]
            else:
                idx = self.left[idx]
        return ret

# key 超過の最小値
    def search_higher(self, key):
        if key == None:
            return None
        ret = None
        idx = self.root
        while idx != 0:
            if self.key[idx] > key:
                ret = self.key[idx]
                idx = self.left[idx]
            else:
                idx = self.right[idx]
        return ret

# 要素の挿入
# 重複を考慮しない
# ToDo: 考慮するものも実装する
    def insert(self, key):
        self.last_index += 1
        self.key[self.last_index] = key
        self.weight[self.last_index] = 2
        self.root = self.__recursive_insert(self.root)
        NotImplemented

# insert の再帰実装に用いる
    def __recursive_insert(self, idx):
        if idx == 0:
            return self.last_index
        elif self.key[self.last_index] < self.key[idx]:
            self.left[idx] = self.__recursive_insert(self.left[idx])
            self.__fix(idx)
            return self.__fix_left_bias(idx)
        else:
            self.right[idx] = self.__recursive_insert(self.right[idx])
            self.__fix(idx)
            return self.__fix_right_bias(idx)

# ノードの weight を補正する
    def __fix(self, idx):
        self.weight[idx] = self.weight[self.left[idx]] + \
            self.weight[self.right[idx]]

# 左回転
    def __rotate_left(self, idx):
        right = self.right[idx]
        self.right[idx] = self.left[right]
        self.__fix(idx)
        self.left[right] = idx
        self.__fix(right)
        return right

# 右回転
    def __rotate_right(self, idx):
        left = self.left[idx]
        self.left[idx] = self.right[left]
        self.__fix(idx)
        self.right[left] = idx
        self.__fix(left)
        return left

# 左偏状態の補正
    def __fix_left_bias(self, idx):
        if self.weight[self.right[idx]] * 4 < self.weight[idx]:
            left = self.left[idx]
            if self.weight[self.left[left]] * 4 < self.weight[left]:
                self.left[idx] = self.__rotate_left(left)
            idx = self.__rotate_right(idx)
        return idx

# 右偏状態の補正
    def __fix_right_bias(self, idx):
        if self.weight[self.left[idx]] * 4 < self.weight[idx]:
            right = self.right[idx]
            if self.weight[self.right[right]] * 4 < self.weight[right]:
                self.right[idx] = self.__rotate_right(right)
            idx = self.__rotate_left(idx)
        return idx

# 要素数
    def size(self):
        return self.weight[self.root] - 1

# デバッグ用
    def dump(self):
        self.__dump(self.root, 0)

    def __dump(self, idx, dep):
        if idx != 0:
            self.__dump(self.right[idx], dep + 1)
            for _ in range(0, dep):
                print("   ", end="")
            print('i:{0},k:{1},l:{2},r:{3},w:{4}'.format(
                idx, self.key[idx], self.left[idx], self.right[idx], self.weight[idx]))
            self.__dump(self.left[idx], dep + 1)


def main():
    n = int(input())
    p = list(map(int, input().split()))
    idx = [0] * n
    for i in range(0, n):
        idx[i] = i
    idx.sort(key=lambda i: - p[i])
    t = WeightBalancedTree(n+2)
    t.insert(-1)
    t.insert(n)
    ans = 0
    for i in idx:
        nex = t.search_higher(i)
        nexnex = t.search_higher(nex)
        pre = t.search_lower(i)
        prepre = t.search_lower(pre)
        if prepre != None:
            ans += p[i] * (pre - prepre) * (nex - i)
        if nexnex != None:
            ans += p[i] * (i - pre) * (nexnex - nex)
        t.insert(i)
    print(ans)


main()
