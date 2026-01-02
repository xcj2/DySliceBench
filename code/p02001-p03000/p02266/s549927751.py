S = input()

# ■のマスは2, ▲のマスは1でカウントする

def scan_forward(F:list, S):

    depth = 0  # 深さ（開始点を基準）
    start = 0  # 「池」が始まった高さ
    is_pond = True  # 池が始まっているか？

    for s in S:
        if s == '\\':  # 下り
            if not is_pond:
                is_pond = True
                start = depth
            depth -= 1
            F.append(2*(start - depth) - 1)
            continue

        if s == "/":  # 上り
            depth += 1
            if start < depth:  # 池の開始位置より高くなった場合
                is_pond = False
                F.append(0)
                continue
            else:
                F.append(2*(start - depth) + 1)

        if s == "_":
            if is_pond:
                F.append(2*(start - depth))
            else:
                F.append(0)

def scan_backward(B:list, S):
    
    depth = 0  # 深さ（開始点を基準）
    start = 0  # 「池」が始まった高さ
    is_pond = True  # 池が始まっているか？

    for s in S:
        if s == '/':  # 下り
            if not is_pond:
                is_pond = True
                start = depth
            depth -= 1
            B.append(2*(start - depth) - 1)
            continue

        if s == "\\":  # 上り
            depth += 1
            if start < depth:  # 現在地が池の開始位置より高い場合
                is_pond = False # 「池」終了
                B.append(0)
                continue
            B.append(2*(start - depth) + 1)

        if s == "_":
            if is_pond:
                B.append(2*(start - depth))
            else:
                B.append(0)

def count_pond(FB):
    
    P = []

    is_pond = False
    count = 0
    amount = 0
    all_amount = 0
    for i in range(len(FB)):
        all_amount += FB[i]
        if is_pond:  # 池の途中
            amount += FB[i]
            if FB[i] == 1:
                is_pond = False  # ここで一旦終了
                P.append(amount//2)
        else:  # 池でなくなった場合
            if FB[i] == 0: continue
            count += 1
            is_pond = True
            amount = FB[i]
    
    return all_amount//2, count, P

F = []
scan_forward(F, S)

B = []
scan_backward(B, reversed(S))
B.reverse()
# print(F)  # 順方向にスキャンした結果
# print(B)  # 逆方向にスキャンした結果

FB = [0]*len(F)
# print(len(F), len(B))

for i in range(len(F)):
    FB[i] = min(F[i], B[i])


# print(FB)  # 水量

aa, k, P = count_pond(FB)
print(aa)
if k == 0:
    print(k)
else:
    print(k, " ".join(list(map(str, P))))
