import sys
from math import factorial
def main():
    packages, remainder = receiveInputData()

    packages.countOddAndEven()

    even_ways = packages.calculateEvenWays()
    odd_ways_remainder0, odd_ways_remainder1 = packages.calculateOddWays()

    if remainder.isZero():
        print(even_ways * odd_ways_remainder0)
        return

    print(even_ways * odd_ways_remainder1)






class Package():
    def __init__(self, packages_list, packages_num):
        if not isinstance(packages_list, list):
            print('Package Class argument error')
            sys.exit(1)

        # 問題の制約では、1以上50以下である
        if packages_num < 1 or packages_num > 50:
            print('Package Class Restriction error')
            print(packages_num)
            sys.exit(1)

        self.packages = packages_list
        self.packages_num = packages_num

    # 中に入っているビスケットの数が偶数の袋、奇数の袋それぞれ数える
    def countOddAndEven(self):
        self.packages_num_of_odd_biscuits  = 0
        self.packages_num_of_even_biscuits = 0
        for pack_i, biscuits_num in enumerate(self.packages):
            if biscuits_num % 2 == 0:
                self.packages_num_of_even_biscuits += 1
            else:
                self.packages_num_of_odd_biscuits += 1

    # 偶数個含まれる袋の選び方は何通りかを返す
    # 袋ごとに　食べる　食べない　の２通りなので
    # m袋あれば　2^m通り
    def calculateEvenWays(self):
        return 2 ** self.packages_num_of_even_biscuits

    def calculateOddWays(self):
        count_combination_list = self.calculateCombination(self.packages_num_of_odd_biscuits)

        # あまりPが0の場合
        # 奇数個含まれる袋は、偶数個選ばなければならない
        selected_even_odds = sum(count_combination_list[::2])

        # あまりPが1の場合
        # 奇数個含まれる袋は、奇数個選ばなければならない
        selected_odd_odds = sum(count_combination_list[1::2])

        return selected_even_odds, selected_odd_odds

    def calculateCombination(self,n):
        # i番目にはnCi
        select_ways_of_odd = [1]
        for select_num in range(1,n + 1):
            n_C_i = factorial(n) // (factorial(select_num) * factorial(n - select_num))
            select_ways_of_odd.append(n_C_i)
        return select_ways_of_odd











class Remainder():
    def __init__(self, remainder_0or1):
        if not isinstance(remainder_0or1, int):
            print('Remainder Class argument error')
            sys.exit(1)

        # 問題の制約では、0か1
        if remainder_0or1 != 0 and remainder_0or1 != 1:
            print('Remainder Class Restriction error')
            sys.exit(1)

        self.remainder = remainder_0or1


    def isZero(self):
        if self.remainder == 0:
            return True
        return False


def receiveInputData():

    N, P = map(int, input().split())
    A = list(map(int,input().split()))

    return Package(A, N), Remainder(P)

if __name__ == '__main__':
    main()
