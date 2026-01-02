from collections import deque


def main():
    process_count, process_time, processes = get_input()
    result = run_roundrobin(processes=processes, time=process_time)
    for r in result:
        print(r.name, r.time)


def run_roundrobin(processes, time, total_time=0, result=[]):
    while processes:
        p = processes.popleft()
        if p.time <= time:
            total_time += p.time
            p.time = total_time
            result.append(p)
        else:
            total_time += time
            p.time -= time
            processes.append(p)

    return result


def get_input():
    count, time = list(map(lambda x: int(x), input().split(' ')))

    processes = deque([])
    for _ in range(count):
        im = input().split(' ')
        p = Process(im[0], int(im[1]))
        processes.append(p)

    return count, time, processes


class Process():

    def __init__(self, name, time):
        self.name = name
        self.time = time


main()