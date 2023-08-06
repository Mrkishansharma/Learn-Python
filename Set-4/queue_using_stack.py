class Queue :
    
    def __init__(self) :
        self.s1 = []
        self.s2 = []
    
    def enqueue(self, ele) :
        self.s1.append(ele)
    
    def dequeue(self) :
        if not self.s2 :
            while self.s1 :
                self.s2.append(self.s1.pop())
        if self.s2 :
            return self.s2.pop()
    
    def front(self) :
        if not self.s2 :
            while self.s1 :
                self.s2.append(self.s1.pop())
        if self.s2 :
            return len(self.s2)
        


q = Queue()
print(q.enqueue(1))
print(q.enqueue(2)) 

print(q.dequeue())

print(q.enqueue(3))

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())