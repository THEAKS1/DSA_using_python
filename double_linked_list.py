class Node:

    def __init__(self, data, next, previous):
        self.data = data
        self.next = next
        self.previous = previous

class double_linked_list:

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head, None)

        if self.head == None:
            self.head = node
            return
            self.head.previous = node
            self.head = node

    def insert_at_end(self, data):
        itr = self.head
        while itr.next:
            itr = itr.next
        node = Node(data, itr.next, itr)
        itr.next = node


    def print_list(self):
        out = ""
        itr = self.head
        while itr:
            out += str(itr.data) + "-->"
            itr = itr.next
        print(out[:-3])

dl = double_linked_list()
dl.insert_at_beginning(1)
dl.insert_at_beginning(2)
dl.insert_at_end(3)
dl.print_list()