def pay500():
    a_max = min(int(x / 500), a)

    return [x - 500 * i for i in range(a_max + 1)]


def pay100(pay: int):
    b_max = min(int(pay / 100), b)
    return [pay - i * 100 for i in range(b_max + 1)]


def pay50(pay_list: list):
    def canPay(pay: int):
        if 50 * c >= pay:
            return True
        else:
            return False

    return list(map(canPay, pay_list))


def judge():
    def countTrue(l: list, count: int, remain: int):
        count += l[remain].count(True)
        if remain > 0:
            countTrue(l, count, remain - 1)
        else:
            print(count)

    a_list = pay500()
    b_list = list(map(pay100, a_list))
    c_list = list(map(pay50, b_list))
    c_len = len(c_list)

    countTrue(c_list, 0, c_len - 1)


a = int(input())
b = int(input())
c = int(input())
x = int(input())

judge()
