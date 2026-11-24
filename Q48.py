# Defining multiple variables of different data types
student_name = "Aarav"
age = 16
percentage = 92.456

# 1. Printing multiple variables separated by commas (default space separator)
print("Student:", student_name, "Age:", age, "Percentage:", percentage)

# 2. Using f-strings (Formatted String Literals - Recommended)
print(f"Name: {student_name} | Age: {age} | Score: {percentage:.2f}%")

# 3. Using the .format() method
print("Student {} is {} years old and scored {:.1f}%.".format(student_name, age, percentage))

# 4. Using custom 'sep' and 'end' parameters in print()
print(student_name, age, round(percentage, 2), sep=" - ", end=" [End of Record]\n")
