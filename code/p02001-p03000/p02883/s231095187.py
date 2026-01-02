class Contest:
    def __init__(self, member_cost,food_cost,k):
        self.member_cost = member_cost
        self.food_cost   = food_cost
        self.max_training_times = k
        
    def canAchieve(self,target):
        sum_training_times = 0
        for i in range(len(self.member_cost)):
            sum_training_times += max(0,self.member_cost[i] - target//self.food_cost[i])

        return  sum_training_times <= self.max_training_times
        


    def bisect(self,begin,end):
        if (end - begin <= 1 ):
            return end
        target = (begin + end)//2
        if self.canAchieve(target):
            return self.bisect(begin,target)

        else:
            return self.bisect(target,end)




def resolve():
    n,k  = map(int,input().split())
    
    member_cost = list(map(int,input().split()))

    food_cost = list(map(int,input().split()))
    member_cost.sort()
    food_cost.sort(reverse=True)
    total_cost = []
    for i in range(len(member_cost)):
        total_cost.append(member_cost[i]*food_cost[i])

    max_total_cost = max(total_cost)
    contest = Contest(member_cost,food_cost,k)
    print(contest.bisect(-1,max_total_cost))
    
resolve()