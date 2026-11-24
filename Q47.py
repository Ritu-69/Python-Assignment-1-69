# 1. Demonstrating the list() constructor
empty_list = list()
string_to_list = list("Python")
tuple_to_list = list((10, 20, 30))

print("--- list() Constructor ---")
print("Empty list:", empty_list)
print("From string:", string_to_list)
print("From tuple:", tuple_to_list)


# 2. Demonstrating the tuple() constructor
empty_tuple = tuple()
list_to_tuple = tuple([1, 2, 3, 4])
string_to_tuple = tuple("Code")

print("\n--- tuple() Constructor ---")
print("Empty tuple:", empty_tuple)
print("From list:", list_to_tuple)
print("From string:", string_to_tuple)


# 3. Demonstrating the dict() constructor
empty_dict = dict()
keyword_dict = dict(name="Alice", age=25, city="Delhi")
pairs_to_dict = dict([("a", 1), ("b", 2), ("c", 3)])

print("\n--- dict() Constructor ---")
print("Empty dictionary:", empty_dict)
print("From keyword arguments:", keyword_dict)
print("From list of tuples:", pairs_to_dict)
