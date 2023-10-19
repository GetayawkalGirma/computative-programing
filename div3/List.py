class ListOperations:
    def __init__(self):
        self.my_list = []

    def insert(self, i, e):
        self.my_list.insert(i, e)

    def print_list(self):
        print(self.my_list)

    def remove(self, e):
        self.my_list.remove(e)

    def append(self, e):
        self.my_list.append(e)

    def sort(self):
        self.my_list.sort()

    def pop(self):
        self.my_list.pop()

    def reverse(self):
        self.my_list.reverse()

# Initialize the list operations object
list_ops = ListOperations()

# Read the number of commands
N = int(input())

# Process each command
for _ in range(N):
    command = input().split()
    cmd = command[0]

    if cmd == "insert":
        i = int(command[1])
        e = int(command[2])
        list_ops.insert(i, e)
    elif cmd == "print":
        list_ops.print_list()
    elif cmd == "remove":
        e = int(command[1])
        list_ops.remove(e)
    elif cmd == "append":
        e = int(command[1])
        list_ops.append(e)
    elif cmd == "sort":
        list_ops.sort()
    elif cmd == "pop":
        list_ops.pop()
    elif cmd == "reverse":
        list_ops.reverse()
