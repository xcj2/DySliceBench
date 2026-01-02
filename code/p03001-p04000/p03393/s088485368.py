import sys


def next_str() -> str:
    result = ""
    while True:
        tmp = sys.stdin.read(1)
        if tmp.strip() != "":
            result += tmp
        elif tmp != '\r':
            break
    return result


def next_permutation(l: list) -> bool:
    n = len(l)
    i = n - 2
    while i >= 0 and l[i] >= l[i + 1]:
        i -= 1

    if i == -1:
        return False

    j = i + 1
    while j < n and l[j] > l[i]:
        j += 1
    j -= 1

    l[i], l[j] = l[j], l[i]

    left = i + 1
    right = n - 1

    while left < right:
        l[left], l[right] = l[right], l[left]
        left += 1
        right -= 1

    return True


def main() -> None:
    s = next_str()
    t = [a for a in s]

    for v in range(ord('a'), ord('z') + 1):
        if chr(v) not in s:
            print(s + chr(v))
            return

    if not next_permutation(t):
        print(-1)
    else:
        i = 0
        while s[i] == t[i]:
            print(s[i], end="")
            i += 1
        print(t[i])


if __name__ == '__main__':
    main()