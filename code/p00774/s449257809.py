from functools import lru_cache

digits = list(map(lambda x: str(x),range(1,10)))

@lru_cache(maxsize=None) 
def check(s,n):  
    return ' '.join([s]*n)

def down(x):
    x = list(x[::-1])   
    while '0' in x:
        x.remove('0')
        x.append('#')
    return x

def main(n):
    data = '\n'.join(map(lambda x: input(), range(n)))  
    score = 0
    while True:
        removed = False
        for d in digits:
            if check(d, 3) in data:
                for i in range(5, 2, -1):
                    if check(d, i) in data:
                        score += int(d) * (data.count(check(d, i))*i)
                        data = data.replace(check(d, i), check('0', i))
                        removed = True
        if removed == False:
            break
        data = zip(*map(lambda x: x.split(), data.split('\n')))
        data = map(lambda x: down(x), data)
        data = list(map(lambda x: ' '.join(x),zip(*data)))
        data = '\n'.join(data[::-1])
    print(score) 


while True:
    n = int(input())
    if n == 0: break
    main(n)

