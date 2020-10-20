### Class Stack of integers ###


# Stack that only holds integers
class intStack(object):
    def __init__(self):
        self.state = []
    def push(self, element):
        '''Adds an element to the top of a stack'''
        assert type(element) == self.elemType
        self.state.append(element)
    def empty(self):
        '''True iff stack is empty'''
        return len(self.state) == 0
    def pop(self):
        '''Removes the top of a nonempty stack'''
        if not self.empty():
            self.state.pop()
    def top(self):
        '''Returns the top of a nonempty stack'''
        if self.empty():
            raise ValueError("Reuested top of an empty Stack!!")
        else:
            return self.state[-1]

# Most of the time, we are doing this:
# Parameterized Stack:
class Stack(object):
    def __init__(self,type):
        self.elemenType = type
        self.state = []
    def push(self, element):
        '''Adds an element to the top of a stack'''
        self.state.append(element)
    def empty(self):
        '''True iff stack is empty'''
        return len(self.state) == 0
    def pop(self):
        '''Removes the top of a nonempty stack'''
        if not self.empty():
            self.state.pop()
    def top(self):
        '''Returns the top of a nonempty stack'''
        if self.empty():
            raise ValueError("Reuested top of an empty Stack!!")
        else:
            return self.state[-1]
