
class restaurant:
    def __init__(self, name, point, num):
        self.name = name
        self.point = point
        self.num = num
    def __repr__(self):
        return "%d" % (self.num)



def main():
    N  = int(input())
    restaurants = []
    for i in range(N):
        S = input().split()   
        restaurants.append(restaurant(str(S[0]),int(S[1]),i+1))

    restaurants = sorted(restaurants, key=lambda x: x.point , reverse=True)
    restaurants = sorted(restaurants, key=lambda x: x.name)

    
    for i in range(N):
        print(restaurants[i])



if __name__ == '__main__':
    main()
