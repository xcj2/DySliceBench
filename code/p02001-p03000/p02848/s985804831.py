def _rot13(c,N):
    if 'A' <= c and c <= 'Z':
        # 13 文字分ずらす
        return chr((ord(c) - ord('A') + N) % 26 + ord('A'))

    if 'a' <= c and c <= 'z':
        # 13 文字分ずらす
        return chr((ord(c) - ord('a') + N) % 26 + ord('a'))

    # その他の文字は対象外
    return c


def rot13(s,N):
    # ジェネレータ内包表記で文字列に ROT13 を適用する
    g = (_rot13(c,N) for c in s)
    # 文字列に直す
    return ''.join(g)


def main():
    N = int(input())
    s = input()
    print(rot13(s,N))


if __name__ == '__main__':
    main()