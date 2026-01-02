def s(generator, splitter, mapper):
    return [ mapper(s) for s in generator().split(splitter) ]

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行区切りの入力をn行読み込んで数値リストにして返します。
def get_nums_n(n):
    return [ int(input()) for _ in range(n)]

n = int(input())

strs = [ input() for _ in range(n) ]

ab = sum(map(lambda s:s.count("AB"), strs))
# print(ab)

last_a = sum(map(lambda s:1 if s.endswith("A") else 0, strs))

first_b = sum(map(lambda s:1 if s.startswith("B") else 0, strs))

both = sum(map(lambda s:1 if s.endswith("A") and s.startswith("B") else 0, strs))

if both > 0 and last_a == first_b and first_b == both:
    print(ab + min(last_a, first_b) - 1)
else:
    print(ab + min(last_a, first_b))