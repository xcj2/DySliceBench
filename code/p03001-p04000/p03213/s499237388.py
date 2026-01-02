
from collections import defaultdict

def get_yakusuu(num):
    yakusuu_dic = defaultdict(int)
    seed_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for now_num in range(1, num + 1):
        for num_ele in seed_primes:
            if now_num < num_ele:
                break
            while now_num % num_ele == 0:
                yakusuu_dic[num_ele] += 1
                now_num = now_num // num_ele
    return list(yakusuu_dic.values())

def calc(yakusuu_dic, lim):
    count = 0
    for num in yakusuu_dic:
        if num >= lim:
            count += 1
        else:
            break
    return count

def main():
    num = int(input())
    yakusuu_dic = get_yakusuu(num)
    yakusuu_dic.sort(reverse=True)

    up_4 = calc(yakusuu_dic, 4)
    up_2 = calc(yakusuu_dic, 2)
    ans1 = max(up_4 * (up_4 - 1) * (up_2 - 2) // 2, 0)

    up_24 = calc(yakusuu_dic, 24)
    ans2 = max(up_24 * (up_2 - 1), 0)

    up_14 = calc(yakusuu_dic, 14)
    ans3 = max(up_14 * (up_4 - 1), 0)

    up_74 = calc(yakusuu_dic, 74)
    ans4 = up_74

    ans = ans1 + ans2 + ans3 + ans4

    print(ans)




if __name__ == '__main__':
    main()