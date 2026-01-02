def bubble_sort(card_list):
    # フラグを使わないので、card_list がどの程度ソート済みかに
    # 関わらず、常に N ^ 2 のオーダーになる。
    for i in range(len(card_list)):
        for j in range(len(card_list)-1, i, -1):
            if int(card_list[j][1]) < int(card_list[j-1][1]):
                card_list[j-1], card_list[j] = card_list[j], card_list[j-1]

def selection_sort(card_list):
    for i in range(len(card_list)):
        minj = i
        for j in range(i+1, len(card_list)):
            if int(card_list[j][1]) < int(card_list[minj][1]):
                minj = j
        
        if minj != i:
            card_list[minj], card_list[i] = card_list[i], card_list[minj]


def is_stable(before, after):
    """ソートが安定だったかどうかを判定する。

    ソート前と後のリスト in, out をとる。リスト中に全く同じカードはないと仮定している。
    """
    for i in range(len(before)):
        for j in range(i+1, len(before)):
            for a in range(len(after)):
                for b in range(a+1, len(after)):
                    if before[i][1] == before[j][1] and before[i] == after[b] and before[j] == after[a]:
                        return False

    return True



N = int(input())
orig_card_list = input().split()

b_card_list = orig_card_list.copy()
s_card_list = orig_card_list.copy()

bubble_sort(b_card_list)
selection_sort(s_card_list)

print(*b_card_list)
if is_stable(orig_card_list, b_card_list):
    print('Stable')
else:
    print('Not stable')

print(*s_card_list)
if is_stable(orig_card_list, s_card_list):
    print('Stable')
else:
    print('Not stable')
