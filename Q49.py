# Create an original tuple
original_tuple = (10, 20, 30, 40)
print("Original tuple:", original_tuple)

# 1. Demonstrate tuple immutability
try:
    original_tuple[1] = 25  # Attempting to modify an element directly
except TypeError as e:
    print("Immutability error:", e)

# 2. Create a modified tuple using slicing and concatenation
# Replacing index 1 (20) with 25
modified_tuple = original_tuple[:1] + (25,) + original_tuple[2:]

print("Modified tuple:", modified_tuple)
