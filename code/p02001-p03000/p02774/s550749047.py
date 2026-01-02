import sys

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

def nC2(n):
    return n * (n-1) // 2

n,k = get_nums_l()
aaa = get_nums_l()

negatives = []
zeros = 0
positives = []

for a in aaa:
    if a == 0:
        zeros += 1
    elif a > 0:
        positives.append(a)
    else:
        negatives.append(a)

# 絶対値小さい順
positives.sort()
negatives.sort(reverse=True)

len_positives = len(positives)
len_negatives = len(negatives)

# 要素の個数から、ペアの積を負,0,正に分けた場合の個数を数える
p_zeros = zeros*(len_negatives+len_positives) + nC2(zeros)
p_positives = nC2(len_positives) + nC2(len_negatives)
p_negatives = len_positives * len_negatives

if p_negatives < k <= (p_negatives+p_zeros):
    # ゼロの場合
    print(0)
    exit()

if k <= p_negatives:
    # 負の場合
    nokori = k

    left = -1 * ((10**9)**2 + 1)
    right = -1

    # 積がcenter未満になるペアがnokori個未満になる最大のcenterを探す
    while left < right:
        center = (left+right+1) // 2

        left2 = len_positives-1
        right2 = len_negatives-1

        count = 0

        # 正の数と負の数を掛けてcenter未満になる個数を数える
        while right2 > 0 and positives[left2] * negatives[right2] < center:
            right2 -= 1

        while 0<=left2<len_positives and 0<=right2<len_negatives:
            if positives[left2] * negatives[right2] < center:
                count += len_negatives - right2
                left2 -= 1
            else:
                right2 += 1

        if count < nokori:
            left = center
        else:
            right = center - 1
    print(left)
    exit()

# 正の場合
nokori = k - p_negatives - p_zeros

left = 1
right = (10**9)**2 + 1

# 積がcenter未満になるペアがnokori個未満になる最大のcenterを探す
while left < right:
    center = (left+right+1) // 2

    left2 = 0
    right2 = len_positives-1

    count = 0

    # 正の数同士で掛けてcenter未満になる個数を数える
    while left2 < right2:
        if positives[left2] * positives[right2] < center:
            count += right2 - left2
            left2 += 1
        else:
            right2 -= 1

    left2 = 0
    right2 = len_negatives-1

    # 負の数同士で掛けてcenter未満になる個数を数える
    while left2 < right2:
        if negatives[left2] * negatives[right2] < center:
            count += right2 - left2
            left2 += 1
        else:
            right2 -= 1

    if count < nokori:
        left = center
    else:
        right = center-1
print(left)