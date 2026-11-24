a = 5
b = 10

# Method 1: Pythonic way (Tuple Unpacking)
a, b = b, a

# Method 2: Using Arithmetic (+ and -)
# a = a + b  # a becomes 15
# b = a - b  # b becomes 5 (15 - 10)
# a = a - b  # a becomes 10 (15 - 5)

print("After swapping: a =", a, "b =", b)
