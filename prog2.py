# Simple Python program to calculate the area of a rectangle

# Function to calculate the area of a rectangle
def calculate_area(length, width):
    area = length * width
    return area

# Ask the user for the dimensions of the rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate the area
area = calculate_area(length, width)

# Display the area
print(f"The area of the rectangle with length {length} and width {width} is {area}.")
