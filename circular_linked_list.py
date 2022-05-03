class Node:
    def __init__(self, data, next, prev):
        self.data = data
        self.next = next
        self.prev = prev

class circular_list:

    def __init__(self):
        self.head = None

    def insert_front(self, data):
        # If list is empty
        if self.head == None:
            node = Node(data, None, None)
            self.head = node
            self.head.next = self.head.prev = self.head
            return

        # If atleast one node is present
        last = self.head.prev
        node = Node(data, self.head, last)
        last.next = self.head.prev = node
        self.head = node

    def insert_end(self, data):
        last = self.head.prev
        node = Node(data, self.head, self.head.prev)
        last.next = self.head.prev = node

    def insert_any(self, data):
        next_node = self.head
        while next_node.data <= data:
            previous_node = next_node
            next_node = next_node.next
        node = Node(data, next_node, previous_node)
        next_node.prev = previous_node.next = node

    def delete_front(self):
        if self.head == None:
            print("Error: List is empty.")
            return
        
        self.head.next.prev = self.head.prev
        self.head.prev.next = self.head.next
        self.head = self.head.next

    def delete_end(self):
        if self.head == None:
            print("Error: List is empty.")
            return
        
        last = self.head.prev
        last.prev.next = self.head
        self.head.prev = last.prev

    def delete_any(self, data):
        if self.head == None:
            print("Error: List is empty.")
            return

        next_node = self.head
        while next_node.data < data:
            if next_node.next == self.head:
                break

            previous_node = next_node
            next_node = next_node.next

        if next_node.data != data:
            print("Error: Element {} not found.".format(data))
            return

        previous_node.next = next_node.next
        next_node.next.prev = next_node.prev

    def print_list(self):
        print("Traversing right to left:\n")
        temp = self.head
        out = ""
        while temp.next != self.head:
            out += str(temp.data) + "-->"
            temp = temp.next
        out += str(temp.data)
        print(out)

        print("Traversing left to right:\n")
        last = self.head.prev
        out = ""
        while last.prev != self.head.prev:
            out += str(last.data) + "-->"
            last = last.prev
        out += str(last.data)
        print(out)


cl = circular_list()
cl.delete_end()
cl.insert_front(3)
cl.insert_front(2)
cl.insert_front(1)
cl.insert_end(4)
cl.insert_end(6)
cl.insert_any(5)
cl.delete_front()
cl.delete_end()
cl.delete_any(4)
cl.delete_any(100)
cl.print_list()