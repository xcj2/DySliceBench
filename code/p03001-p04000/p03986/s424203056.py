def main():
    X = input()

    #ans = part(X)
    ans = editorial(X)
    print(ans)


def test_ans():
    X_ans = [
        ("TSTTSS", 4),
        ("SSTTST", 0),
        ("TSSTTTSS", 4),
    ]
    for X, ans in X_ans:
        assert part(X) == editorial(X) == ans


def editorial(X):
    stack = [X[0]]
    ans = len(X)
    for c in X[1:]:
        if stack and stack[-1] == "S" and c == "T":
            ans -= 2
            stack.pop()
        else:
            stack.append(c)

    return ans


def part(X):
    while True:
        n = len(X)
        for i in range(n-1):
            if X[i:i+2] == "ST":
                X = X[:i] + X[i+2:]
                break

        if n == len(X):
            break

    return len(X)


if __name__ == '__main__':
    main()
