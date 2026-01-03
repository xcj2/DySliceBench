class Number:
    value = ''
    plus = False
    
    def __init__(self, value, plus = False):
      self.value = value
      self.plus = plus

    def __str__(self) -> str:
        return '+' + str(self.value) if self.plus else str(self.value)


count = 0


def solve(numbers, k):
    global count
    if k >= len(numbers):
        x = ''.join([str(n) for n in numbers])
        count += sum(int(x) for x in x.split('+'))
        return

    b = []

    for i, n in enumerate(numbers):
        if i == k:
            b.append(Number(n.value, True))
        else:
            b.append(n)

    solve(numbers, k + 1)
    solve(b, k + 1)


s = input()

numbers = [Number(x) for x in s]

solve(numbers, 1)

print(count)
