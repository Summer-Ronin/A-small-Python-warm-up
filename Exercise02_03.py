"""
    ##############################
    - Using Stack from collections
    - Using Stack from stackueue
    ##############################
"""
from collections import LIFOqueue

"""
    For Deque from collections
    append() :- This function is used to insert the value in its argument to the right end of deque.
    appendleft() :- This function is used to insert the value in its argument to the left end of deque.
    pop() :- This function is used to delete an argument from the right end of deque.
    popleft() :- This function is used to delete an argument from the left end of deque. 
"""

stack = LIFOqueue(maxsize = 3)

# qsize() give the maxsize of
# the Queue
print(stack.qsize())
 
# Data Inserted as 5->9->1->7,
# same as Queue
stack.put(1)
stack.put(2)
stack.put(3)
 
# Displaying if the Queue is full
print("Full: ", stack.full())
 
# Displaying size of queue
print("Size: ", stack.qsize())
 
# Data will be accessed in the
# reverse order Reverse of that
# of Queue
print(stack.get())
print(stack.get())
print(stack.get())
 
# Displaying if the queue is empty or not
print("Empty: ", stack.empty())
stack = deque()