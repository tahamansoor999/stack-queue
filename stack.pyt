# Node class for the linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Stack implementation using Linked List
class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.top.value

# Queue implementation using Linked List
class Queue:
    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.front.value

# Example usage
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    print("Top of stack:", stack.peek())  # Output: 20
    stack.pop()
    print("Top of stack after pop:", stack.peek())  # Output: 10

    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    print("Front of queue:", queue.peek())  # Output: 1
    queue.dequeue()
    print("Front of queue after dequeue:", queue.peek())  # Output: 2