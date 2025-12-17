class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def Push(self, val: int):
        if self.head:
            prev = self.head
            self.head = Node(val=val)
            self.head.next = prev
        else:
            self.head = Node(val=val)
    
    def Pop(self):
        if self.head:
            val = self.head.val
            self.head = self.head.next
            return val
    
    def peek(self):
        if self.head:
            return self.head.val

print("Create stack: my_stack = Stack()")
my_stack = Stack()
my_stack.Push(0)
print("my_stack.Push(0)", my_stack.peek())
my_stack.Push(5)
print("my_stack.Push(5)", my_stack.peek())
my_stack.Push(10)
print("my_stack.Push(10)", my_stack.peek())
my_stack.Push(15)
print("my_stack.Push(15)", my_stack.peek())
my_stack.Push(20)
print("my_stack.Push(20)", my_stack.peek())
my_stack.Push(25)
print("my_stack.Push(25)", my_stack.peek())

print("pop()")
val = my_stack.Pop()
print(f"return value: {val} peek: {my_stack.peek()}")

my_stack.Push(50)
print("my_stack.Push(50)", my_stack.peek())

print("pop()")
val = my_stack.Pop()
print(f"return value: {val} peek: {my_stack.peek()}")

print("pop()")
val = my_stack.Pop()
print(f"return value: {val} peek: {my_stack.peek()}")
print("pop()")
val = my_stack.Pop()
print(f"return value: {val} peek: {my_stack.peek()}")
print("pop()")
val = my_stack.Pop()
print(f"return value: {val} peek: {my_stack.peek()}")
print("pop()")
val = my_stack.Pop()
print(f"return value: {val} peek: {my_stack.peek()}")
print("pop()")
val = my_stack.Pop()
print(f"return value: {val} peek: {my_stack.peek()}")
