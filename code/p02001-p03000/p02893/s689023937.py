n = int(input())
X = input()
int_x = int(X, 2)
mod = 998244353


def divisors(num):
    array = []
    limit = int(num ** 0.5) + 1
    for i in range(1, limit):
        if num % i == 0:
            div1 = i
            div2 = num//i
            array.append(div1)
            if div1 != div2:
                array.append(div2)
    array.sort()
    return array


def is_repeatable(block):
    """
    分割したブロックの個数から、繰り返し可能か判定
    ブロック数は１以外の奇数の時に繰り返し可能
    :param block: 全体の長さnを等間隔に分割した時の、ブロック数
    :return: 繰り返し可能ならTrue そうでないならFalse
    """
    if block == 1:
        return False
    else:
        if block % 2 == 1:
            return True
        else:
            return False


def get_small_repeatable_list(length):
    """
    ブロックの長さを引数として受け取り、
    この長さを元にして、さらに小さい繰り返し配列が作成可能かどうかを確認し、
    小さく繰り返し配列のブロック長さをリストで返す
    （ダブルカウントのチェック）
    例　長さ6のブロックを繋いだ　6_6^_6　の配列の場合
    　　(2_2^_2)_(2^_2_2^)_(2_2^_2)の繰り返し配列が作成できる
    :param length: ブロックの長さ
    :return: ダブルカウントしてしまっているもののリスト
    """
    small_blocks = divisors(length)
    small_length_list = []
    for small_block in small_blocks:
        if is_repeatable(small_block):
            small_length = length//small_block
            small_length_list.append(small_length)

    return small_length_list


ans = (2 * n * (int_x+1)) % mod
div_list = divisors(n)

blocks = []
for div in div_list:
    block = div
    if is_repeatable(block):
        blocks.append(block)

blocks.sort(reverse=True)
done = {}
for block in blocks:
    length = n // block
    forward = X[:length]
    reverse = 2**length-1 - int(forward, 2)
    reverse = format(reverse, '0'+str(length)+'b')
    count = int(forward, 2) + 1
    for i in range(1, block):
        if i % 2 == 1:
            compare = reverse
        else:
            compare = forward

        check = X[length*i:length*(i+1)]
        if compare == check:
            continue
        elif compare > check:
            count -= 1
            break
        elif compare < check:
            break

    small_repeatable_list = get_small_repeatable_list(length)
    for small_length in small_repeatable_list:
        double_count = done[small_length]
        count -= double_count

    done[length] = count
    ans -= 2*n*count
    ans += 2*length*count
    ans %= mod

print(ans)
