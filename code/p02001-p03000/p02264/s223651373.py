class Queue:
    def __init__(self) -> None:
        self.queue = list()

    def _is_empty(self):
        if len(self.queue) == 0:
            return True
        return False

    def enqueue(self, obj):
        self.queue.append(obj)

    def dequeue(self):
        if self._is_empty():
            return None
        else:
            return self.queue.pop(0)

    def __len__(self):
        return len(self.queue)


def main():
    n, q = map(int, input().split(' '))
    queue = Queue()
    for i in range(n):
        name, num = input().split(' ')
        queue.enqueue({'name': name, 'num': int(num)})
    time = 0
    while True:
        if len(queue) == 0:
            break
        task = queue.dequeue()
        task['num'] -= q
        if task['num'] > 0:
            queue.enqueue(task)
            time += q
        else:
            time += q+task['num']
            print(task['name'], time)


if __name__ == "__main__":
    main()

