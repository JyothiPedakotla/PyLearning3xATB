# Identity Operators (is, is not)

# These are used to check if two variables are located on the same part of the memory. Two variables that are equal does not imply that they are identical

a = 5
b = 5
print(a is b)  # Prints: True

list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 is list2)  # Prints: False

print(a is not b)  # Prints: False
print(list1 is not list2)  # Prints: True