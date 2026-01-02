n = int(input())
length = 1000018
sosu = 500009
ht = [-1] * length


def convert(moji):
    l_moji = len(moji)
    num = 0
    for j in range(l_moji):
        keta = 10 ** (l_moji - j - 1)
        if moji[j] == 'A':
            num += keta * 1
        if moji[j] == 'C':
            num += keta * 2
        if moji[j] == 'G':
            num += keta * 3
        if moji[j] == 'T':
            num += keta * 4
    return num


def hash_in(nk, num, m):
    if m == 0:
        return False
    hash_num = nk + (num % m)
    if hash_num > length:
        hash_num -= length
    if ht[hash_num] == -1:
        ht[hash_num] = num
    elif ht[hash_num] != num:
        hash_in(hash_num, num, m-1)
    return


def find(nk, num, m):
    if m == 0:
        return 'no'
    hash_num = nk + (num % m)
    if hash_num > length:
        hash_num -= length
    if ht[hash_num] == -1:
        return 'no'
    elif ht[hash_num] != num:
        return find(hash_num, num, m-1)
    elif ht[hash_num] == num:
        return 'yes'


def main():
    output = list()
    for i in range(n):
        command = list(input().split())
        num = convert(command[1])
        if command[0] == 'insert':
            if hash_in(0, num, sosu) is not None:
                print('an error is occured')
                break
        if command[0] == 'find':
            output.append(find(0, num, sosu))

    for j in output:
        print(j)


if __name__ == '__main__':
    main()

