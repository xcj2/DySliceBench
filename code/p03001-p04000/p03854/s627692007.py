import queue


def check_dream(s):
    return s.startswith('dream')


def check_dreamer(s):
    return s.startswith('dreamer')


def check_erase(s):
    return s.startswith('erase')


def check_eraser(s):
    return s.startswith('eraser')


def check_sentence(s, q):
    if check_dream(s):
        q.put(s[5:])

    if check_dreamer(s):
        q.put(s[7:])

    if check_erase(s):
        q.put(s[5:])

    if check_eraser(s):
        q.put(s[6:])

    return q


def search():
    sentence_q = queue.Queue()
    initial_s = input()

    s = initial_s
    while(1):
        if s == '':
            return True

        sentence_q = check_sentence(s, sentence_q)
        if sentence_q.empty():
            return False

        s = sentence_q.get()


if search():
    print('YES')
else:
    print('NO')