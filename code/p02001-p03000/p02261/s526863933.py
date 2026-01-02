n = int(input())
cards = list(map(str, input().split()))


def bubble(a):
    num = [int(i[1]) for i in a]
    char = [i[0] for i in a]
    for i in range(n):
        for j in range(n-1, i, -1):
            if num[j] < num[j-1]:
                num[j], num[j-1] = num[j-1], num[j]
                char[j], char[j-1] = char[j-1], char[j]
    else:
        a_new = [char[i] + str(num[i]) for i in range(n)]
        return a_new


def selection(a):
    num = [int(i[1]) for i in a]
    char = [i[0] for i in a]
    minj = 0
    stay = True
    same_exi = False
    for i in range(n):
        minj = i
        for j in range(i, n):
            if num[minj] > num[j]:
                minj = j
                if same_exi:
                    stay = False
            if num[i] == num[j]:
                same_exi = True
        else:
            num[i], num[minj] = num[minj], num[i]
            char[i], char[minj] = char[minj], char[i]
    else:
        a_new = [char[i] + str(num[i]) for i in range(n)]
        return a_new, stay


def print_space(li):
    for i in range(len(li)-1):
        print(li[i], end=' ')
    else:
        print(li[-1])



cards_bu = bubble(cards)
cards_sl = selection(cards)

sl_list = cards_sl[0]
sl_stay = cards_sl[1]

print_space(cards_bu)
print('Stable')

print_space(sl_list)
if sl_list == cards_bu:
    print('Stable')
else:
    print('Not stable')
    



