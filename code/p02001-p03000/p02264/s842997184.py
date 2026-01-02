#http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_3_B&lang=jp
#?????\???
#??????????????¨????§?????????¨?????¨?????????????????????????????????????????????????????????
def rrs(quantum, process):
    finished_process = []
    queue = Queue()
    current_time = 0
    i = 0
    while len(finished_process) < len(process):
        if i < len(process):
            p_info = process[i]
            i += 1
        else:
            p_info = queue.dequeue()
        time = int(p_info[1])
        name = p_info[0]
        
        if time <= quantum:
            current_time += time
            finished_process.append((name, current_time))
        else:
            current_time += quantum
            queue.enqueue((name, time - quantum))
            
    return finished_process


class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, d):
        self.data.append(d)

    def dequeue(self):
        r = self.data[0]
        self.data = self.data[1:]
        return r
    
def main():
    info = input().split()
    n_list = int(info[0])
    quantum = int(info[1])
    target_list = [tuple(input().split()) for i in range(n_list)]
    print("\n".join([p + " " + str(t) for p,t in rrs(quantum, target_list)]))
    
if __name__ == "__main__":
    main()