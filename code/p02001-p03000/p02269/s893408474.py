import sys 


class Tree:
    def __init__(self):
        self.children = {}
        self.end = False

    def __contains__(self, key):
        if len(key) == 0:
            return self.end

        k, *rest = key 
        if k not in self.children:
            return False

        return rest in self.children[k]

    def add(self, key):
        if len(key) > 0:
            k, *rest = key 
            if k not in self.children:
                self.children[k] = self.__class__()

            self.children[k].add(rest)
        else:
            self.end = True


class Dictionary:
    def __init__(self):
        self.tree = Tree()

    def insert(self, word):
        self.tree.add(word)

    def find(self, word):
        return word in self.tree


def run():
    _ = int(input())  # flake8: noqa
    words = Dictionary()

    for command in sys.stdin:

        if command.startswith('insert'):
            words.insert(command[7:])
        elif command.startswith('find'):
            if words.find(command[5:]):
                print('yes')
            else:
                print('no')
        else:
            raise ValueError()


if __name__ == '__main__':
    run()

