"""
    Building a custom Stack
"""


class Stack:
    def __init__(self):
        self.st = []

    def push(self, el):
        self.st.append(el)

    def pop(self):
        if(self.isEmpty() == False):
            return self.st.pop(len(self.st) - 1)
        else:
            return 'Stack is Empty'

    def isEmpty(self):
        if(len(self.st) == 0):
            return True
        else:
            return False

    def size(self):
        return(len(self.st))

    def top(self):
        if(self.isEmpty() == False):
            return self.st[0]
        else:
            return 'Stack is Empty'


if __name__ == '__main__':
    st = Stack()
    st.push(5)
    st.push(7)
    st.push(9)
    st.size()
    print(st.pop())
    print(st.top())

    st.size()
