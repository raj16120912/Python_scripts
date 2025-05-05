import os

given_str = input("Enter Your string: ")
length = os.get_terminal_size().columns
print (given_str.center(length))
