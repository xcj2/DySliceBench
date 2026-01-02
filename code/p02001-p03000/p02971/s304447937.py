SEQUENCE_LEN_MIN = 2
SEQUENCE_LEN_MAX = 200000
NUMERIC_MIN = 1
NUMERIC_MAX = 200000
 
 
class NumericInfo:
    def __init__(self):
        self.index = - 1
        self.value = NUMERIC_MIN - 1
 
    def update(self, idx, val):
        self.index = idx
        self.value = val
 
    def copy(self, info):
        self.update(info.index, info.value)
 
 
class SequenceProcessor:
    def __init__(self, sequence):
        self.sequence_length = len(sequence)
        self.first_largest_num_info = NumericInfo()
        self.second_largest_num_info = NumericInfo()
        self._process(sequence)
 
    def _process(self, sequence):
        for i, num in enumerate(sequence):
            if self.first_largest_num_info.value < num:
                self.second_largest_num_info.copy(self.first_largest_num_info)
                self.first_largest_num_info.update(i, num)
            elif self.second_largest_num_info.value < num:
                self.second_largest_num_info.update(i, num)
 
    def _max_value(self, idx):
        if idx == self.first_largest_num_info.index:
            return self.second_largest_num_info.value
        else:
            return self.first_largest_num_info.value
 
    def all_max_value(self):
        for i in range(self.sequence_length):
            yield self._max_value(i)
 
 
def _validate_sequence_length(s):
    r = int(s)
 
 
def get_sequence_length_from_stdin():
    s = input()
    s = s.strip()
    return int(s)
 
 
def _validate_numeric(s):
    r = int(s)
 
 
def get_sequence_from_stdin(length):
    result = []
    for i in range(1, length+1):
        while True:
            n = input()
            try:
                result.append(int(n))
                break
            except ValueError:
                continue
    return result
 
 
def main():
    seq_len = get_sequence_length_from_stdin()
    sequence = get_sequence_from_stdin(seq_len)
    seq_processor = SequenceProcessor(sequence)
    for num in seq_processor.all_max_value():
        print(num)
 
 
if __name__ == '__main__':
    main()