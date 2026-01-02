# ALDS_1_B.

def intinput():
    a = input().split()
    for i in range(len(a)):
        a[i] = int(a[i])
    return a

def get_gcd(x, y):
    if x < y: return get_gcd(y, x)
    # x >= yのときはx % yを計算してyとx % yの話にする。
    # ここでx % yのところが0ならばyが求める答えとなる。
    if y == 0: return x
    return get_gcd(y, x % y)

def main():
    a = intinput()
    x = a[0]; y = a[1]
    # Pythonではa, bのswapはa, b = b, aとか書く。
    print(get_gcd(x, y))

if __name__ == "__main__":
    main()
