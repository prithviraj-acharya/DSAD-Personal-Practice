# Stack implementation using array

# Algorithm size()
# Algorithm isEmpty()
# Algorithm top()
# Algorithm push(o)
# Algorithm pop()


class Stack:
    def __init__(self, max_size=2):
        # initialize the stack
        self.arr = []
        self.idx = -1
        self.max_size = max_size

    def size(self):
        return self.idx + 1

    def is_empty(self):
        return self.top_index == -1

    def top(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        else:
            return self.arr[self.idx]

    def push(self, data):
        if self.size() >= self.max_size:
            print("Stack is full")
            return

        self.arr.append(data)
        self.idx = self.idx + 1
        return True

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        else:
            self.top_index -= 1
            return self.arr.pop()


arrImplementation = Stack()
try:
    len = arrImplementation.size()
    arrImplementation.push(2)
    arrImplementation.push(4)
    arrImplementation.push(5)
    arrImplementation.push(6)
    top = arrImplementation.top()
    print("Top: ", top)
    arrImplementation.pop()
    top = arrImplementation.top()
    print("Top: ", top)
    arrImplementation.pop()
    top = arrImplementation.top()
    print("Top: ", top)
    arrImplementation.pop()

except IndexError as e:
    print("Error: ", e)

except Exception as e:
    print("Error: ", e)
