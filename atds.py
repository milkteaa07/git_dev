#!/usr/bin/env/python3

"""
atds.py
a compilation of useful classes...
"""

__author__ = "Ava Teng"
__version__ = "2023-02-17"


class Stack(object):
    def __init__(self):
        self.stack = []
    
    def get_stack(self):
        return self.stack
        
    def size(self):
        return len(self.stack)   
     
    def push(self, item):
        # Adds an item to the end of the list, ie. the top of the stack.
        self.stack.append(item)
        
    def pop(self):
        # removes the last item on the list, ie. the top of the stack
        if len(self.stack) > 0:
            return self.stack.pop()
        
    def peek(self):
        return self.stack[-1]
        
    def is_empty(self):
        return len(self.stack) == 0
    
    def __repr__(self):
        string = ''
        for i in range(len(self.stack)-1, -1, -1):
            string += self.stack[i] + '\n'
        return "STACK: \n" + string
    
    
class Deque(object):
    # front = start of list, rear = end of list
    def __init__(self):
        self.queue = []
        
    def get_queue(self):
        return self.queue
    
    def size(self):
        return len(self.queue)
    
    def add_front(self, item):
        self.queue.insert(0, item)
        
    def add_rear(self, item):
        self.queue.append(item)
        
    def remove_front(self):
        del self.queue[0]
        
    def remove_rear(self):
        del self.queue[-1]
        
    def is_empty(self):
        return len(self.queue) == 0
    
    def __repr__(self):
        string = ''
        for i in range(len(self.queue)):
            string += str(i+1) + " " + self.queue[i] + '\n'
        return "QUEUE: \n" + string
    
    
    
# for testing purposes...
def main():
    d = Deque()
    string = 'hacrar'
    for letter in string:
        d.add_rear(letter)
    print(d)
    d.remove_rear()
    print(d)
        

if __name__ == "__main__":
    main()

