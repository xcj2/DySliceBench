def scale(unit):
    if unit == "JPY":
        scale = 1.0
    else:
        scale = 380000.0

    return scale


def normalize_money(money):
    _price, unit = money.split()
    price = float(_price)

    return price * scale(unit)


def solve(str_in_arr):
    moneys = str_in_arr[1::]
    normalized_money = [normalize_money(money) for money in moneys]

    return sum(normalized_money)

  
def main():
    _num_relative = input()
    num_relative = int(_num_relative)

    std_in = [num_relative if idx == 0 else input() for idx in range(num_relative+1)]
    print(solve(std_in))


if __name__ == "__main__":
    main()
