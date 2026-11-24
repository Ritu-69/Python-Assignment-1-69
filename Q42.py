# Assigning variables with different and identical values
a = 10
b = 10
c = 25
name = "Python"

# Printing the memory addresses (IDs) of the variables
print("Value of a:", a, "| ID of a:", id(a))
print("Value of b:", b, "| ID of b:", id(b))
print("Value of c:", c, "| ID of c:", id(c))
print("Value of name:", name, "| ID of name:", id(name))

# Modifying variable 'a' and checking its new ID
a = 50
print("\nAfter changing 'a' to 50:")
print("New value of a:", a, "| New ID of a:", id(a))
