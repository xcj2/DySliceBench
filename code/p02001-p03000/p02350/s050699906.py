import sys
input = sys.stdin.readline
class LazySegTree:
    """
    遅延評価セグメント木
    デフォルト引数は RMQ and RUQ
    値の更新・取得は半開区間
    内部実装は 1-indexed
    参考: https://yukicoder.me/submissions/295288

    """
    def __init__(self,
                 a,
                 op=lambda a,b: a if a<b else b,
                 op_e=(1<<31)-1,
                 ap=lambda a,b,length: a if a!=-1 else b,
                 cp=lambda a,b: a if a!=-1 else b,
                 ap_identity=-1):
        """
        :param a: 初期状態
        :param op: 区間取得のための関数
        :param op_e: 単位元
        :param ap: 区間更新のための関数　第1引数は作用させる値　第2引数はもとの値
        :param cp: ap を結合するための関数
        :param ap_identity: 恒等変換
        """
        self.n = n = len(a)
        self.op, self.op_e, self.ap, self.cp, self.ap_identity = op, op_e, ap, cp, ap_identity
        self.val = val = [op_e] * n + a
        self.act = [ap_identity] * n
        self.length = length = [1] * (2*n)
        l = 2*n-2
        for i in range(n-1, 0, -1):
            r = l+1
            length[i] = length[l] + length[r]
            val[i] = op(val[l], val[r])
            l -= 2

    def get(self, l, r):
        self._push(l, r)
        res_l = res_r = self.op_e
        l += self.n
        r += self.n
        val, op = self.val, self.op
        while l < r:
            if l & 1:
                res_l = op(res_l, val[l])
            if r & 1:
                res_r = op(val[r-1], res_r)
            l = l+1 >> 1
            r >>= 1
        return op(res_l, res_r)

    def push(self):
        for i in range(1, self.n):
            self._push_one(i)

    def set(self, l, r, value):
        # 区間更新
        if l >= r:
            return
        n, ap, val, op, act, cp, length = self.n, self.ap, self.val, self.op, self.act, self.cp, self.length
        self._push(l, r)
        l = i = l + n
        r = j = r + n
        if i & 1: val[i] = ap(value, val[i], length[i])
        if j & 1: j-=1; val[j] = ap(value, val[j], length[j])
        i = i+1 >> 1
        j >>= 1
        while i < j:
            if i & 1:
                val[i] = ap(value, val[i], length[i])
                act[i] = cp(value, act[i])
            if j & 1:
                j -= 1
                val[j] = ap(value, val[j], length[j])
                act[j] = cp(value, act[j])
            i = i+1 >> 1
            j >>= 1
        l = l // (l & -l) >> 1
        while l>0:
            val[l] = op(val[2*l], val[2*l+1])
            l >>= 1
        r = r // (r & -r) >> 1
        while r>0:
            val[r] = op(val[2*r], val[2*r+1])
            r >>= 1

    def set_one(self, i, value):
        # 値の代入のみ行う
        val, op = self.val, self.op
        self._push(i, i+1)
        i += self.n
        val[i] = value
        i >>= 1
        while i>0:
            val[i] = op(val[2*i], val[2*i+1])
            i >>= 1

    def _ap(self, value, i):
        # 内部インデックス i の要素に値 value で作用させる
        self.val[i] = self.ap(value, self.val[i], self.length[i])
        if i < self.n:
            self.act[i] = self.cp(value, self.act[i])

    def _push_one(self, i):
        act = self.act
        self._ap(act[i], 2*i)
        self._ap(act[i], 2*i+1)
        act[i] = self.ap_identity

    def _push(self, l, r):
        n, act, ap_identity, ap, cp, val, length = self.n, self.act, self.ap_identity, self.ap, self.cp, self.val, self.length
        ln = l + n
        rnm1 = r + n - 1
        hl = ln.bit_length()-1
        hr = rnm1.bit_length()-1
        for hr in range(hr, 0, -1):
            al = ln >> hl
            ar = rnm1 >> hr
            if al < n:
                #_push_one(al)
                al_l = 2 * al
                al_r = al_l + 1
                act_al = act[al]
                val[al_l] = ap(act_al, val[al_l], length[al_l])
                if al_l < n:
                    act[al_l] = cp(act_al, act[al_l])
                val[al_r] = ap(act_al, val[al_r], length[al_r])
                if al_r < n:
                    act[al_r] = cp(act_al, act[al_r])
                act[al] = ap_identity
            if ar != al:
                #_push_one(ar)
                ar_l = 2 * ar
                ar_r = ar_l + 1
                act_ar = act[ar]
                val[ar_l] = ap(act_ar, val[ar_l], length[ar_l])
                if ar_l < n:
                    act[ar_l] = cp(act_ar, act[ar_l])
                val[ar_r] = ap(act_ar, val[ar_r], length[ar_r])
                if ar_r < n:
                    act[ar_r] = cp(act_ar, act[ar_r])
                act[ar] = ap_identity
            hl -= 1


N, Q = map(int, input().split())
tree = LazySegTree([(1<<31)-1]*N)
ans = []
for i in range(Q):
    q, *A = map(int, input().split())
    if q==0:
        s, t, x = A
        tree.set(s, t+1, x)
    else:
        s, t = A
        ans.append(tree.get(s, t+1))
print("\n".join(map(str, ans)))

