def splitString(target, start, end):
    first = target[:start]
    middle = target[start:end + 1]
    last = target[end + 1:]
    return (first, middle, last)

def doReplace(target, args):
    start = int(args[0])
    end = int(args[1])
    replace_str = args[2]

    first, _, last = splitString(target, start, end)

    return first + replace_str + last


def doReverse(target, args):
    start = int(args[0])
    end = int(args[1])

    first, middle, last = splitString(target, start, end)

    return first + middle[::-1] + last


def makeMessage(target, args):
    start = int(args[0])
    end = int(args[1])

    _, middle, _ = splitString(target, start, end)

    return middle


def transform():
    messages = []  # プリント用文字を格納するリスト
    target = input()
    q = int(input())

    for _ in range(q):
        line = input()
        cmd = line.split(' ')[0]
        args = line.split(' ')[1:]

        # 各命令を実行
        if cmd == 'print':
            messages.append(makeMessage(target, args))
        elif cmd == 'replace':
            target = doReplace(target, args)
        elif cmd == 'reverse':
            target = doReverse(target, args)
    # 各メッセージの表示
    [print(message) for message in messages]


def kantanna_test(expected, actual):
    if expected == actual:
        print('OK')
    else:
        print('NG')


if __name__ == '__main__':

    transform()
