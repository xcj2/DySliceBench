isPrime = []
prime = []
count = []

def init():
    for i in range(50000 + 1):
        isPrime.append(True)
        count.append(0)

def eratos():
    isPrime[0] = False
    isPrime[1] = False
    for i in range(2, int((50000 ** (1 / 2))) + 1):
        if (isPrime[i]):
            for j in range(i * 2, 50000 + 1, i):
                isPrime[j] = False
    
    for i in range(2, 50001):
        if isPrime[i]:
            prime.append(i)


def table():
    for i in prime:
        for j in prime:
            if i < j:
                continue
            if i + j > 50000:
                continue
            count[i + j] += 1

init()
eratos()
table()

while True:
    n = int(input())
    if n == 0:
        break
    print(count[n])