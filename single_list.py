class Node:
    def __init__(self, value: int):
        self.next = None
        self.val = value

class LinkedList:
    def __init__(self, value:int):
        self.head = Node(value=value)
    
    def insert_node(self, value: int):
        next_node = Node(value=value)
        
        tail = self.head
        while(tail.next):
            tail = tail.next
        
        tail.next = next_node

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.val, end=", ")
            curr = curr.next
        print() 

    
    def delete_node(self, value: int):
        if self.head is None:
            return # list is empty
        
        if self.head.val == value:
            self.head = self.head.next
            return
        
        prev = self.head
        curr = self.head.next

        while curr:
            if curr.val == value:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next
    
    def findMToLastElement(self, m: int):
        "Retuns m Node from the last"

        if self.head is None or m >= 0:
            return None
        
        current : Node= self.head
        mBehind : Node = self.head

        for _ in range(0, m):
            if current.next:
                current = current.next
            else:
                return None
        
        while(current.next):
            current = current.next
            mBehind = mBehind.next
        
        return mBehind




my_list = LinkedList(5)
my_list.insert_node(10)
my_list.insert_node(15)
my_list.insert_node(20)
my_list.insert_node(25)

my_list.print_list()

my_list.delete_node(10)
my_list.delete_node(15)

my_list.print_list()
