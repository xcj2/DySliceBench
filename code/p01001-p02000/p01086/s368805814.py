class CheckError(Exception):
    pass

def check(wclist, count):
    c = 0
    while True:
        c += wclist.pop(0)
        if c == count:
            return wclist
        elif c > count:
            raise CheckError

def tanku_check(wclist):
    for i in range(len(wclist)):
        try:
            wcl = wclist[:][i:]
            wcl = check(wcl, 5)
            wcl = check(wcl, 7)
            wcl = check(wcl, 5)
            wcl = check(wcl, 7)
            wcl = check(wcl, 7)
            return i+1
        except CheckError:
            pass

def main():
    while True:
        n = int(input().strip())
        if n == 0:
            break
        wclist = [len(input().strip()) for _ in range(n)]
        print(tanku_check(wclist))

if __name__ == '__main__':
    main()

