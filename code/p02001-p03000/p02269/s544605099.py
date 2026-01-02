# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_C&lang=jp
sample_input = list(range(4))
sample_input[0] = '''6
insert AAA
insert AAC
find AAA
find CCC
insert CCC
find CCC'''
sample_input[1] = '''13
insert AAA
insert AAC
insert AGA
insert AGG
insert TTT
find AAA
find CCC
find CCC
insert CCC
find CCC
insert T
find TTT
find T'''
sample_input[2] = '''20
find CTT
find TAG
insert AA
insert CTC
find G
insert TGT
find AAC
find TTG
insert AA
insert TTG
insert G
insert A
insert GG
insert C
insert TT
find T
insert C
find GG
find G
insert CG'''
sample_input[3]='''15
insert AAA
insert AAC
insert AGA
insert AGG
insert TTT
find AAA
find CCC
find CCC
insert CCC
find CCC
find CC
insert T
find TTT
find T
find A'''
give_sample_input = None
if give_sample_input is not None:
    sample_input_list = sample_input[give_sample_input].split('\n')
    def input():
        return sample_input_list.pop(0)
        
# main

class ACGTDictNode (object):
    
    def __init__(self):
        self.A = None    # None | ACGTDictNode
        self.C = None
        self.G = None
        self.T = None
        self.has_end = False
    
    
    def add_if_none(self, acgt):
        if acgt == 'A':
            if self.A is not None:
                return self.A
            else:
                self.A = ACGTDictNode()
                return self.A
        elif acgt == 'C':
            if self.C is not None:
                return self.C
            else:
                self.C = ACGTDictNode()
                return self.C
        elif acgt == 'G':
            if self.G is not None:
                return self.G
            else:
                self.G = ACGTDictNode()
                return self.G
        elif acgt == 'T':
            if self.T is not None:
                return self.T
            else:
                self.T = ACGTDictNode()
                return self.T
        else:
            assert False
            
            
    def get(self, acgt):
        if acgt == 'A':
            return self.A
        elif acgt == 'C':
            return self.C
        elif acgt == 'G':
            return self.G
        elif acgt == 'T':
            return self.T
        else:
            assert False
            
    
    def add_end(self):
        self.has_end = True

        

class ACGTDict (object):
    
    def __init__(self):
        self.tree = ACGTDictNode()
        
        
    def insert(self, string):
        node = self.tree
        for c in string:
            node = node.add_if_none(c)
        node.add_end()
            
    
    def find(self, string):
        node = self.tree
        for c in string:
            node = node.get(c)
            if node is None:
                return False
        return node.has_end
        
        

dict = ACGTDict()
num_of_commands = int(input())
for n in range(num_of_commands):
    input_str = input()
    command, data = input_str.split(' ')
    if command == 'insert':
        dict.insert(data)
    else:
        if dict.find(data):
            print('yes')
        else:
            print('no')
            