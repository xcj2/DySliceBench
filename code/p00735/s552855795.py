def main():
    while True:
        data = int(input())
        if data == 1: break

        i = 1
        factlist = []
        while True:
            item = 7 * i - 1
            if item > int(data / 6) + 1: break

            if data % item == 0:
                quo = int(data / item)
                if isms(quo) and ismsp(quo):
                    factlist.append(quo)
            

            item = 7 * i + 1
            if item > int(data / 6) + 1:break

            if data % item == 0:
                quo = int(data / item)
                if isms(quo) and ismsp(quo):
                    factlist.append(quo)

            i += 1

        factlist.sort()
        if factlist == []: factlist.append(data)

        print(str(data) + ":", end = "")

        for item in factlist:
            print(" " + str(item), end = "")
        print("")
            

def isms(num):
    if num % 7 == 1 or num % 7 == 6: return True
    else: return False

def ismsp(num):
    i = 1
    while True:
        item = 7 * i - 1
        if item > int(num / 6) + 1: break

        if num % item == 0: return False

        item = 7 * i + 1
        if item > int(num / 6) + 1: break

        if num % item == 0: return False

        i += 1
    return True
main()

