class Node(object):
    def __init__(self, num, prev = None, nxt = None):
        self.num = num;
        self.prev = prev;
        self.nxt = nxt;

class Double_Linked_List(object):
    def __init__(self):
        self.first = self.last = None;

    def insert(self, num):
        node = Node(num);
        if self.first is not None:
            self.first.prev = node;
            node.nxt = self.first;
            self.first = node;
        else:
            self.first = node;
            self.last = node;

    def delete(self, num):
        current = self.first;
        while current is not None:
            if current.num == num:
                prev = current.prev;
                nxt = current.nxt;
                if prev is not None:
                    current.prev = None;
                    prev.nxt = nxt;
                if nxt is not None:
                    current.nxt = None;
                    nxt.prev = prev;
                if nxt is None:
                    self.last = prev;
                if prev is None:
                    self.first = nxt;
                break;
            else:
                current = current.nxt;

    def delete_first(self):
        if self.first is not None:
            nxt = self.first.nxt;
            if nxt is not None:
                self.first.nxt = None;
                nxt.prev = None;
                self.first = nxt;
            else:
                self.first = None;
                self.last = None;

    def delete_last(self):
        if self.last is not None:
            prev = self.last.prev;
            if prev is not None:
                self.last.prev = None;
                prev.nxt = None;
                self.last = prev;
            else:
                self.first = None;
                self.last = None;

    def get_content(self):
        ret = [];
        append = ret.append;
        current = self.first;
        while current is not None:
            append(current.num);
            current = current.nxt;
        return " ".join(ret);

def main():
    from sys import stdin
    double_linked_list = Double_Linked_List();
    count = int(input());
    delete_first = double_linked_list.delete_first;
    delete_last = double_linked_list.delete_last;
    delete = double_linked_list.delete;
    insert = double_linked_list.insert;
    for i in range(count):
        command = stdin.readline().strip().split();
        if command[0] == "insert":
            insert(command[1]);
        if command[0] == "delete":
            delete(command[1]);
        elif command[0] == "deleteFirst":
            delete_first();
        elif command[0] == "deleteLast":
            delete_last();
    print(double_linked_list.get_content());

main();







