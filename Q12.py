import math

# Take radius as input from the user
radius = float(input("Enter the radius of the circle: "))

# Calculate area and circumference
area = math.pi * (radius ** 2)
circumference = 2 * math.pi * radius

# Display the results rounded to 2 decimal places
print(f"Area of the circle: {area:.2f}")
print(f"Circumference of the circle: {circumference:.2f}")
