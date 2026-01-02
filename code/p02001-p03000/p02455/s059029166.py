BLACK = True
RED = False


class Vertex:
    def __init__(self, val, color, parent=None, left=None, right=None):
        self.val = val
        self.col = color
        self.p = parent
        self.l = left
        self.r = right


class RedBlcakTree:
    def __init__(self):
        self.nil = Vertex(None, BLACK, None, None, None)    # 番兵の設定。色は必ず黒、それ以外は適当 (フィールドが一時的に使われることはあるが意味はない)
        self.root = self.nil
        self.size = 0
    

    # =========
    # 巡回、出力
    # =========
    def inorder_traverse(self, node=None):
        buf = []
        node = self.root if node is None else node
        # print(node.val)
        if node != self.nil:
            buf += self.inorder_traverse(node.l)
            buf.append(node.val)
            buf += self.inorder_traverse(node.r)
        return buf
    
    def preorder_traverse(self, node=None):
        buf = []
        node = self.root if node is None else node
        if node != self.nil:
            buf.append(node.val)
            buf += self.preorder_traverse(node.l)
            buf += self.preorder_traverse(node.r)
        return buf

    def postorder_traverse(self, node=None):
        buf = []
        node = self.root if node is None else node
        if node != self.nil:
            buf += self.postorder_traverse(node.l)
            buf += self.postorder_traverse(node.r)
            buf.append(node.val)
        return buf
    
    def __str__(self):
        return '[' + ', '.join(map(str, self.inorder_traverse())) + ']'
    
    def __len__(self):
        return self.size

    
    # ===========
    # 基本的な探索
    # ===========
    def find(self, x, node=None, key=lambda x: x):
        '''
        ある部分木のなかで key(val) が x と一致するようなノードを探索する。
        発見したらそのノードを返し、発見できなったら -1 を返す。 (O(lgn))
        Args:
            x (object): 探索したい値
            node (Vertex): 探索を行う部分木の根。デフォルトでは探索木全体の根のノードを指す。
            key (function)
        '''
        node = self.root if node is None else node
        while node != self.nil and key(node.val) != x:
            node = node.l if x < node.val else node.r
        if node == self.nil:
            return -1
        else:
            return node
    
    def min_node(self, node=None):
        '''
        ある部分木のなかで最小のノードを探す (O(lgn))
        '''
        node = self.root if node is None else node
        while node.l != self.nil:
            node = node.l
        return node
    
    def max_node(self, node=None):
        '''
        ある部分木のなかで最大のノードを探す (O(lgn))
        '''
        node = self.root if node is None else node
        while node.r != self.nil:
            node = node.r
        return node
    
    def successor(self, node):
        '''
        中間順木巡回で定まる順序において、ある節点の次節点を決定する。(O(lgn))
        次節点が存在したらそのノードを、存在しなかったら ValueError を返す。
        '''
        arg = node
        if node.r != self.nil:
            return self.min_node(node.r)
        else:
            while node.p != self.nil and node.p.l != node:
                node = node.p
            if node.p == self.nil:
                raise ValueError(f'RedBlackTree.successor(): {arg} is the last node.')
            else:
                return node.p
    
    def predecessor(self, node):
        '''
        中間順木巡回で定まる順序において、ある節点の前節点を決定する。(O(lgn))
        前節点が存在したらそのノードを、存在しなかったら ValueError を返す。
        '''
        arg = node
        if node.l != self.nil:
            return self.max_node(node.l)
        else:
            while node.p != self.nil and node.p.r != node:
                node = node.p
            if node.p == self.nil:
                raise ValueError(f'RedBlackTree.predecessor(): {arg} is the first node.')
            else:
                return node.p


    # =========================
    # 単回転、重回転処理 (補助操作)
    # =========================
    def _left_rotate(self, node):
        # (O(1))
        # left_rotate ... node 自身を、node の右の子を回転中心として左回転させる。
        # right_rotate ...                左の子              右回転
        # 二分探索木条件を満たすよう適切に子供を付け替える。
        # なお回転中心である left_rotate の際の右の子、right_rotate の際の左の子は self.nil ではないとする。

        # アルファベットを節点、<ギリシャ文字>を木とする。節点 y 中心の回転は
                
        #         y          rRot           x
        #     x       <γ>    ->       <α>         y
        #  <α> <β>           <-                <β>  <γ>   
        #                    lRot

        # のようになる。
        '''
        Args:
            node (Vertex)
        Raises:
            RuntimeError: node ないし回転中心の node.r が self.nil であったとき
        '''
        if node == self.nil or node.r == self.nil:
            raise RuntimeError('RedBlackTree._left_rotate(): cannot rotate with NIL')
        pivot = node.r
        if node.p != self.nil:
            # 自身の親の設定
            if node.p.l == node:
                node.p.l = pivot
            else:
                node.p.r = pivot
        else:
            # root の設定
            self.root = pivot
        # 回転中心の左の子の設定
        pivot.l.p = node
        # 回転中心の設定、自身の設定 (ポインタが上書きされないように注意)
        pivot.p = node.p
        node.r = pivot.l
        pivot.l = node
        node.p = pivot
    
    def _right_rotate(self, node):
        if node == self.nil or node.l == self.nil:
            raise RuntimeError('RedBlackTree._right_rotate(): cannot rotate with NIL')
        pivot = node.l
        if node.p != self.nil:
            # 自身の親の設定
            if node.p.l == node:
                node.p.l = pivot
            else:
                node.p.r = pivot
        else:
            # root の設定
            self.root = pivot
        # 回転中心の右の子の設定
        pivot.r.p = node
        # 回転中心の設定、自身の設定 (ポインタが上書きされないように注意)
        pivot.p = node.p
        node.l = pivot.r
        pivot.r = node
        node.p = pivot
    
    def _LR_rotate(self, node):
        # (O(1))
        # LR_rotate ... 自身の左の子において left_rotate を行い、そのあと自身に right_rotate を行う。なお、左の子、左の子の右の子は self.nil でないものとする。
        # RL_rotate ...      右           right_rotate                    left_rotate             右の子、右の子の左の子

        # 以下の節点 u に対し LR_rotate() を施すと
        #             u                                      w 
        #     v              <t4>         LR          v             u
        # <t1>   w                        ->      <t1>  <t2>    <t3> <t4>
        #     <t2><t3>
        # となる。

        # 以下の節点 u に対し RL_rotate() を施すと
        #             u                                      w
        #   <t1>              v           RL          u             v
        #                 w      <t4>     ->     <t1>  <t2>     <t3> <t4>
        #              <t2><t3>
        # となる。
        self._left_rotate(node.l)
        self._right_rotate(node)
    
    def _RL_rotate(self, node):
        self._right_rotate(node.r)
        self._left_rotate(node)

    
    # ===================
    # 鉢植え処理 (補助操作)
    # ===================
    def _transplant(self, u_node, v_node):
        '''
        u_node の親の子供の位置に v_node 以下の部分木がくるように、v_node 部分木を機械的に移し替える。(O(1))
        (u の親が v の親になるわけではない。u 節点はかつての親や子供を参照し続けることに注意。オブジェクトは生き残るのでよしなに属性を書き換えて使用できる -> delete_node())
        なお、この関数では二分探索木条件が保持されるかどうかなどは考慮しない。        
        '''
        # u の親の子属性の設定
        if u_node.p == self.nil:
            self.root = v_node
        elif u_node.p.l == u_node:
            u_node.p.l = v_node
        else:
            u_node.p.r = v_node
        # v の親属性の設定
        v_node.p = u_node.p
    

    # ========
    # 節点の挿入
    # ========
    def insert(self, data):
        '''
        値が data であるようなノードを挿入する (O(lgn))
        z は挿入ノードを、y は適切な挿入位置の親ノードの位置を示すトレーラポインタである
        '''
        if self.find(data) == -1:
            self.size += 1
            x = self.root
            y = self.nil
            while x != self.nil:
                y = x
                x = x.l if data < x.val else x.r
            # 挿入ノードは赤色。親は y で子は共に番兵
            z = Vertex(data, RED, y, self.nil, self.nil)
            # z の親の子属性の設定 
            if y == self.nil:
                self.root = z
            elif data < y.val:
                y.l = z
            else:
                y.r = z
            # 二色木条件を復活
            self._insert_fixup(z)
    

    def _insert_fixup(self, z):
        '''
        insert により壊れた二色木条件を適切に復活させる。(O(1))
        最初は 2 4 の二色木条件が満たされていない可能性がある。
        ループ終了時には 4 の二色木条件は必ず満たされる。
        そして根が赤色の二色木を緩和二色木というが、この根を黒く彩色することで他の二色機条件が壊れることはない。ただ 2 が満たされるのみ。

        Args:
            z (Vertex): 挿入節点 (最初は赤色)。
        Raises:
            RuntimeError: なぜか二色木条件がすでに壊れている時
        '''
        while z.p.col == RED:
            parent = z.p
            if parent.p.col == RED:
                raise RuntimeError('RedBlackTree._insert_fixup(): color constraints broken')
            if parent.l == z:
                # 自分は親の左の子で、親も祖先の左の子 case 1-1
                if parent.p.l == parent:
                    self._right_rotate(parent.p)
                # 自分は親の左の子で、親は祖先の右の子 case 1-2
                else:
                    self._RL_rotate(parent.p)
                    z = z.r
            else:
                # 自分は親の右の子で、親は祖先の左の子 case 2-1
                if parent.p.l == parent:
                    self._LR_rotate(parent.p)
                    z = z.l
                # 自分は親の右の子で、親も祖先の右の子 case 2-2
                else:
                    self._left_rotate(parent.p)
            z.col = BLACK
            z = z.p
        self.root.col = BLACK
    

    # ========
    # 節点の削除
    # ========
    def delete(self, node):
        '''
        赤黒木内の指定された節点を削除する。(O(lgn))
        node 削除後に node がいた位置におさまる節点 x として、
        original_color_of_x は x のもとの色を、
        y は黒が足りていない木の根を表す。
        (以前 x がいた場所 (両方子供あり) or 以前 node がいた場所 (子供は高々片方のみ))
        '''
        self.size -= 1
        x = node
        original_color_of_x = x.col
        # 子供なし or 右のみ子供
        if node.l == self.nil:
            y = node.r    # y は transplant の結果 node が存在した位置に入る
            self._transplant(node, node.r)
        # 左のみ子供
        elif node.r == self.nil:
            y = node.l    # y は transplant の結果 node が存在した位置に入る
            self._transplant(node, node.l)
        # 両方子供
        # node の位置に node の次節点を鉢植えしポインタを調整
        else:
            x = self.successor(node)
            original_color_of_x = x.col
            y = x.r    # y は  transplant の結果 x が存在した位置に入る
            if x != node.r:
                self._transplant(x, x.r)
                x.r = node.r
                x.r.p = x
            else:
                y.p = x    # これがないと適切に親を辿れない。Algorithm Intro p.246 (c) でいうと x の親ポインタを y へむけている (x, y が逆なことに注意)
            self._transplant(node, x)
            node.l.p = x
            x.l = node.l
            x.col = node.col
        if original_color_of_x == BLACK:
            self._delete_fixup(y)
    
    def _delete_fixup(self, y):
        '''
        delete により壊れた二色木条件を適切に復活させる。(O(1))
        最初は 2 5 の二色木条件が満たされていない可能性がある。(要素数 3 で根が黒、両方の子供が赤であるような根を削除するようなケースで 2 が破られるよ)
        再帰関数処理後には 5 の二色木条件は必ず満たされる。
        そして根が赤色の二色木を緩和二色木というが、この根を黒く彩色することで他の二色機条件が壊れることはない。ただ 2 が満たされるのみ。

        Args:
            y (Vertex): 黒の足りない部分木の根
        '''
        if y != self.root:
            parent = y.p
            original_color_of_p = parent.col
            # 自身が左の子
            if parent.l == y:
                # 兄弟が赤 case 1-1
                if parent.r.col == RED:
                    # print('1-1')
                    self._left_rotate(parent)
                    parent.col = RED
                    parent.p.col = BLACK
                    self._delete_fixup(y)
                # 兄弟が黒、その兄弟の左の子は赤 case 1-2
                elif parent.r.l.col == RED:
                    # print('1-2')
                    self._RL_rotate(parent)
                    parent.col = BLACK
                    assert(parent.p.r.col == BLACK)
                    # parent.p.r.col = BLACK
                    parent.p.col = original_color_of_p
                # 兄弟が黒、その兄弟の右の子は赤 case 1-3
                elif parent.r.r.col == RED:
                    # print('1-3')
                    self._left_rotate(parent)
                    parent.col = BLACK
                    parent.p.r.col = BLACK
                    parent.p.col = original_color_of_p
                # 兄弟が黒、その両方の子が黒 case 1-4
                else:
                    # print('1-4')
                    parent.col = BLACK
                    parent.r.col = RED
                    if original_color_of_p == BLACK:
                        self._delete_fixup(parent)
            # 自身が右の子 (以下左右対象で同様)
            else:
                # 兄弟が赤 case 2-1
                if parent.l.col == RED:
                    # print('2-1')
                    self._right_rotate(parent)
                    parent.col = RED
                    parent.p.col = BLACK
                    self._delete_fixup(y)
                # 兄弟が黒、その兄弟の右の子は赤 case 2-2
                elif parent.l.r.col == RED:
                    # print('2-2')
                    self._LR_rotate(parent)
                    parent.col = BLACK
                    assert(parent.p.l.col == BLACK)
                    # parent.p.l.col = BLACK
                    parent.p.col = original_color_of_p
                # 兄弟が黒、その兄弟の左の子は赤 case 2-3
                elif parent.l.l.col == RED:
                    # print('2-3')
                    self._right_rotate(parent)
                    parent.col = BLACK
                    parent.p.l.col = BLACK
                    parent.p.col = original_color_of_p
                # 兄弟が黒、その両方の子が黒 case 2-4
                else:
                    # print('2-4')
                    parent.col = BLACK
                    parent.l.col = RED
                    if original_color_of_p == BLACK:
                        self._delete_fixup(parent)
        self.root.col = BLACK


if __name__ == "__main__":
    rb = RedBlcakTree()
    q = int(input())
    for _ in range(q):
        query, num = map(int, input().split())
        if query == 0:
            rb.insert(num)
            print(rb.size)
        else:
            res = rb.find(num)
            print(0) if res == -1 else print(1)


