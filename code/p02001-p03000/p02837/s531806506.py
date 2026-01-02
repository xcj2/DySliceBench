from queue import Queue

n = int(input())
shogens = []

for people_index in range(n):
    this_shogens = []
    shogen_num = int(input())
    for _ in range(shogen_num):
        this_shogens.append(tuple(map(int, input().split())))

    shogens.append(this_shogens)

def make_pattern(number):
    pattern = [0 for _ in range(n)]
    index = 0
    while True:
        if number == 0:
            break
        else:
            pattern[index] = number % 2
            number //= 2
            index += 1
    return pattern


def ok(pattern):
    hantei = [None for _ in range(n)]
    seen_list = []
    q = Queue()
    ret = True
    for people_index in range(len(pattern)):
        if pattern[people_index] == 1:
            q.put(people_index)
            hantei[people_index] = 1

    while True:
        if q.empty():
            break
        else:
            people_index = q.get()
            if people_index in seen_list:
                continue
            else:
                seen_list.append(people_index)

            this_shogens = shogens[people_index]

            for this_shogen in this_shogens:
                people_sareta_index = this_shogen[0]-1
                shogen = this_shogen[1]

                if shogen == 1 and (people_sareta_index not in seen_list):
                    q.put(people_sareta_index)

                if hantei[people_sareta_index] == None:
                    hantei[people_sareta_index] = shogen

                if shogen != hantei[people_sareta_index]:
                    ret = False
                    break

    return ret

def main():
    max_num = 0
    num_list = []
    for value in range(pow(2, n)-1, -1, -1):
        pattern = make_pattern(value)

        shojiki_count = 0
        for p in pattern:
            if p == 1:
                shojiki_count += 1

        if not shojiki_count in num_list:
            if ok(pattern):
                max_num = max(max_num, shojiki_count)
                num_list.append(shojiki_count)

    print(max_num)
main()