class Daise:
    def __init__(self, info_list):
        self.T = info_list[0]
        self.S = info_list[1]
        self.E = info_list[2]
        self.W = info_list[3]
        self.N = info_list[4]
        self.B = info_list[5]
    
    def change(self, axis):
        if axis == 'S':
            self.T, self.B, self.S, self.N = self.N, self.S, self.T, self.B
        
        elif axis == 'E':
            self.T, self.B, self.E, self.W = self.W, self.E, self.T, self.B
        
        elif axis == 'W':
            self.T, self.B, self.W, self.E = self.E, self.W, self.T, self.B
        
        elif axis == 'N':
            self.T, self.B, self.N, self.S = self.S, self.N, self.T, self.B
        
        elif axis == 'Turn':
            self.S, self.E, self.N, self.W = self.E, self.N, self.W, self.S
    

    def output(self):
        return [self.T, self.S, self.E, self.W, self.N, self.B]
    

    def set_info(self, top, front):
        if front in (self.T, self.B):
            self.change("S")

        while self.S != front:
            self.change('Turn')
 
        while self.T != top:
            self.change('E')


def compair(A, B):
    for _ in range(4):
        for _ in range(4):
            if A.output() == B.output():
                return 'Yes'
            for _ in range(4):
                if A.output() == B.output():
                    return 'Yes'
                B.change('Turn')
            B.change('S')
        B.change('W')
    return 'No'


if __name__ == '__main__':
    inputs = int(input())
    
    all_daise = [Daise(list(map(str, input().split()))) for _ in range(inputs)]
    result = [compair(all_daise[0], i) for i in all_daise[1:]]

    if 'Yes' in result:
        print('No')
    else:
        print('Yes')
