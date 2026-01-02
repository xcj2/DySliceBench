def num_4x_list():
    # 100以下の4の倍数をつくる
    return [4 * i for i in range(1, (100 // 4) + 1)]


def num_list_comb_4_7():
    # 4 と 7 の和の組み合わせで表現できる数を列挙する(最大は100)
    diff = 7 - 4  # ドーナツとケーキの差分が公差になる

    x = set()

    for i, num_4x in enumerate(num_4x_list(), start=1):
        for j in range(i + 1):
            element = num_4x + diff * j
            x |= {element}

    return {y for y in x if y <= 100}


def actual(N):
    if N in num_list_comb_4_7():
        return 'Yes'

    return 'No'

  
  
N = int(input())

print(actual(N))