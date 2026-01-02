# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_3_B&lang=jp
sample_input = list(range(3))
sample_input[0] = '''5 100
p1 150
p2 80
p3 200
p4 350
p5 20'''
sample_input[1] = ''''''
sample_input[2] = ''''''
give_sample_input = None
if give_sample_input is not None:
    sample_input_list = sample_input[give_sample_input].split('\n')
    def input():
        return sample_input_list.pop(0)
        
# main
import copy

class Queue:
    queue = []
    def __init__(self, queue_list = []):
        self.queue = copy.copy(queue_list)
        pass
    def dequeue(self):
        if self.queue == []:
            return None
        return self.queue.pop(0)
        pass
    def enqueue(self, item):
        self.queue.append(item)

class Process:
    name = None
    time = -1
    def __init__(self, a_name, a_time):
        self.name = a_name
        self.time = a_time
    def execute(self, a_time):
        used_time = min(a_time, self.time)
        self.time -= a_time
        return used_time
    def is_ended(self):
        if self.time <= 0:
            return True
        else:
            return False
            
input_str = input()
num_of_process = int(input_str.split()[0])
quantum = int(input_str.split()[1])

input_process = []

for n in range(num_of_process):
    input_str = input()
    input_split = input_str.split()
    process = Process(input_split[0], int(input_split[1]))
    input_process.append(process)

process_queue = Queue(input_process)

time = 0
while True:
    process = process_queue.dequeue()
    if process is None:
        break
    used_time = process.execute(quantum)
    time += used_time
    if process.is_ended():
        timestamp = process.name + ' ' + str(time)
        print(timestamp)
    else:
        process_queue.enqueue(process)
        
        