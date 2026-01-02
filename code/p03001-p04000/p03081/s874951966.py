def c_snuke_the_wizard(N, Q, S, Magic):
    # ゴーレムが隣のゴーレムを追い抜くことはありえない
    # (複数体重なれば、その後同じように動いていくため)。
    # よって、 左端で消滅する、最初に最も右にいるゴーレムleftと、
    # 右端で消滅する、最初に最も左にいるゴーレムrightが分かればいい。
    # (left >= right とはなりえない)
    # これを二分探索で求めれば O(Qlog(N)) で解を得られる。
    def is_vanished(x, direction):
        """
        x番のゴーレムがdirection(leftまたはrightのいずれか)で指定される端で
        消滅するかどうか判定する
        """
        for t, d in Magic:
            if t == S[x]:
                # 呪文で指定されたマスに注目したゴーレムがいた。
                # 呪文の内容に従ってゴーレムを移動させる
                if d == 'L':
                    x -= 1
                else:
                    x += 1
            if x in (-1, N):
                return True  # 左端/右端 で消滅することとなった
        return False

    def binary_search(accept, reject, direction):
        """
        direction が 'left' の場合は accept番とその左側のゴーレムが消滅する。
        direction が 'right' の場合は accept番とその右側のゴーレムが消滅する。
        direction によって accept と reject の位置関係が逆転することに注意。
        """
        while abs(accept - reject) > 1:
            mid = (accept + reject) // 2
            if is_vanished(mid, direction):
                accept = mid
            else:
                reject = mid
        return accept + 1 if direction == 'left' else N - accept
    return max(N - binary_search(-1, N, 'left') - binary_search(N, -1, 'right'), 0)

N, Q = [int(i) for i in input().split()]
S = input()
Magic = [input().split() for j in range(Q)]
print(c_snuke_the_wizard(N, Q, S, Magic))