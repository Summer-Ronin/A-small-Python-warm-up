from Exercise04 import Stack

string_stack = Stack()

string = input()

# convert string to list
string_list = [x for x in string]

for i in string_list:
    string_stack.push(i)

string_stack_list = []
while string_stack.size() != 0:
    string_stack_list.extend(string_stack.pop())

if(string_list == string_stack_list):
    print(string + " is Palindrome")
else:
    print(string + " is Not Palindrome")