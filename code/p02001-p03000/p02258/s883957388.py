import math

class MaxPrice(object):
    
    def __init__(self):
        self.min_price = math.inf
        self.max_price = -math.inf
        self.max_diff = -math.inf

    def set_price(self, p):
        if self.max_price < p:
            self.max_price = p
        else:
            if self.max_diff < p - self.max_price:
                self.max_diff = p - self.max_price

        if p < self.min_price:
            self.min_price = p
        else:
            if self.max_diff < p - self.min_price:
                self.max_diff = p - self.min_price

def run():
    n = int(input())
    mp = MaxPrice()
    for i in range(n):
        p = int(input())
        mp.set_price(p)
    print(mp.max_diff)

if __name__ == '__main__':
    run()
