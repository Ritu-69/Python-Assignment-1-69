# 1. Assigning Boolean values directly
is_raining = True
has_umbrella = False

print("Is it raining?", is_raining)
print("Do you have an umbrella?", has_umbrella)

# 2. Assigning Boolean values using comparisons
age = 20
is_adult = age >= 18  # Evaluates to True
print("Is the person an adult?", is_adult)

# 3. Using Boolean variables in if-else conditions
if is_raining and not has_umbrella:
    print("Stay inside, you will get wet!")
else:
    print("You are good to go outside.")
