x = [1, 2, 3]
y = [1, 2, 3]
z = x

# Case 1: x and y
if x is y:
    print("x and y are the same object")
else:
    print("x and y are not the same object")

# Case 2: x and z
if x is z:
    print("x and z are the same object")
else:
    print("x and z are not the same object")
'''output:
x and y are not the same object
x and z are the same object
'''
