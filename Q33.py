# Creating a list with different data types
mixed_list = [42, 3.14, "Hello", True, [1, 2, 3]]

# Printing the entire list
print("List:", mixed_list)

# Printing each element along with its data type
for item in mixed_list:
    print(f"Value: {item}  -->  Type: {type(item).__name__}")
