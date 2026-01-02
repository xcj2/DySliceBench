class Check():
    def __init__(self, N, number_of_truck,baggage):
        self.N = N
        self.number_of_truck = number_of_truck
        self.baggage = baggage

    def check(self, mid):
        baggage_num = 0
        for j in range(self.number_of_truck):
            baggage_sum = 0
            while(baggage_sum + self.baggage[baggage_num] <= mid):
                baggage_sum += self.baggage[baggage_num]
                baggage_num += 1
                if baggage_num == self.N:
                    return baggage_num
        return baggage_num

    def binary_search(self):
        left = 0
        right = 1000000000
        while(left + 1 < right):
            mid = int((left + right) / 2)
            ok = self.check(mid)
            if ok == self.N:
                right = mid
            else :
                left = mid
        return right

def main():
    N,number_of_truck = [int(i) for i in input().split()]
    baggage = list()
    for i in range(N):
        i = int(input())
        baggage.append(i)
    ok = Check(N,number_of_truck,baggage)
    print(ok.binary_search())

if __name__ == "__main__":
    main()
