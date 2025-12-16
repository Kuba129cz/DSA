class Node:
    def __init__(self, value: int):
        self.next = None
        self.val = value

class LinkedList:
    def __init__(self, value:int):
        self.head = Node(value=value)
    
    def insert_node(self, value: int):
        next_node = Node(value=value)
        
        # najdu posledni uzel
        tail = self.head
        while(tail.next):
            tail = tail.next
        
        tail.next = next_node

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.val, end=", ")
            curr = curr.next

my_list = LinkedList(5)
my_list.insert_node(10)
my_list.insert_node(15)
my_list.insert_node(20)
my_list.insert_node(25)

my_list.print_list()
