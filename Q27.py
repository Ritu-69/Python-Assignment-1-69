# Initial values of different data types
num_str = "25"
decimal_num = 18.75
whole_num = 100

# 1. Using int() to convert string and float to an integer
converted_int1 = int(num_str)        # Converts "25" to 25
converted_int2 = int(decimal_num)    # Truncates 18.75 to 18

# 2. Using float() to convert string and integer to a floating-point number
converted_float1 = float(num_str)    # Converts "25" to 25.0
converted_float2 = float(whole_num)  # Converts 100 to 100.0

# 3. Using str() to convert integer and float to a string
converted_str1 = str(whole_num)      # Converts 100 to "100"
converted_str2 = str(decimal_num)    # Converts 18.75 to "18.75"

# Displaying the converted values and their new data types
print("int() results:", converted_int1, type(converted_int1), "|", converted_int2, type(converted_int2))
print("float() results:", converted_float1, type(converted_float1), "|", converted_float2, type(converted_float2))
print("str() results:", converted_str1, type(converted_str1), "|", converted_str2, type(converted_str2))
