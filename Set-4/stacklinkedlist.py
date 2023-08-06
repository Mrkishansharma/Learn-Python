class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def pop(self):
        if self.head is None:
            return None
        popped_data = self.head.data
        self.head = self.head.next
        return popped_data

stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop())
stack.push(3)
print(stack.pop())
print(stack.pop())
print(stack.pop())
