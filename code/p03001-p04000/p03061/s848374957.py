def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def kari():
    a = list(map(int, input().split()))
    b = map(int, input().split())


def start_process(num, data):
    kouyakusuu1, kouyakusuu2, kouyakusuu3 = gcd(data[0], data[1]), max(data[0], data[1]), min(data[0], data[1])
    # print(kouyakusuu2, kouyakusuu3)

    for i in range(2, num):
        if i == 2:
            a = gcd(data[i], kouyakusuu2)
            b = gcd(data[i], kouyakusuu3)
            kari1 = max(a, b)
            kari2 = kouyakusuu1

            kari3 = gcd(data[i], kouyakusuu1)
        else:
            kari1 = gcd(data[i], kouyakusuu2)
            kari2 = kouyakusuu1

            kari3 = gcd(data[i], kouyakusuu1)



        kouyakusuu1 = kari3
        kouyakusuu2 = max(kari1, kari2)



    print(max(kouyakusuu1, kouyakusuu2))

# def start_process(num, data):
#     for i in range(num)

def main():
    num = int(input())
    data = list(map(int, input().split()))
    start_process(num, data)



if __name__ == '__main__':
    main()
