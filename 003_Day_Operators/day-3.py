#day 3
# Declare age as an integer variable
age = 25

# Declare height as a float variable
height = 5.9

# Declare a variable that stores a complex number
complex_num = 3 + 4j

# Calculate area of a triangle
base = float(input("Enter base: "))
height_triangle = float(input("Enter height: "))
area_triangle = 0.5 * base * height_triangle
print("The area of the triangle is", area_triangle)

# Calculate perimeter of a triangle
side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))
side_c = float(input("Enter side c: "))
perimeter_triangle = side_a + side_b + side_c
print("The perimeter of the triangle is", perimeter_triangle)

# Calculate area and perimeter of a rectangle
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
area_rectangle = length * width
perimeter_rectangle = 2 * (length + width)
print("The area of the rectangle is", area_rectangle)
print("The perimeter of the rectangle is", perimeter_rectangle)

# Calculate area and circumference of a circle
radius_circle = float(input("Enter radius of circle: "))
pi = 3.14
area_circle = pi * radius_circle * radius_circle
circumference_circle = 2 * pi * radius_circle
print("The area of the circle is", area_circle)
print("The circumference of the circle is", circumference_circle)

# Calculate slope, x-intercept, and y-intercept of y = 2x - 2
slope = 2
x_intercept = 1  # (0, -2)
y_intercept = -2

# Calculate slope and Euclidean distance between points (2, 2) and (6, 10)
x1, y1 = 2, 2
x2, y2 = 6, 10
slope_points = (y2 - y1) / (x2 - x1)
euclidean_distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print("Slope between points:", slope_points)
print("Euclidean distance between points:", euclidean_distance)

# Calculate x value for y = 0 in y = x^2 + 6x + 9
# Solving the equation y = x^2 + 6x + 9 = 0
# (x + 3)(x + 3) = 0
# x = -3
# Therefore, y = 0 when x = -3

# Find the length of 'python' and 'dragon' and make a falsy comparison statement
length_python = len('python')
length_dragon = len('dragon')
print(length_python == length_dragon)

# Use 'and' operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon')

# Use 'in' operator to check if 'jargon' is in the sentence
sentence = "There is no 'on' in both dragon and python"
print('jargon' in sentence)

# Find the length of the text 'python' and convert the value to float and then to string
length_python = len('python')
float_length = float(length_python)
str_length = str(float_length)
print(str_length)

# Check if a number is even or not using Python
num = 10
is_even = num % 2 == 0
print(is_even)

# Check if floor division of 7 by 3 is equal to the integer value of 2.7
print(7 // 3 == int(2.7))

# Check if type of '10' is equal to type of 10
print(type('10') == type(10))

# Check if int('9.8') is equal to 10
try:
    print(int('9.8') == 10)
except ValueError:
    print("Conversion to int failed")

# Calculate pay based on hours and rate per hour
hours = int(input("Enter hours: "))
rate_per_hour = int(input("Enter rate per hour: "))
weekly_earning = hours * rate_per_hour
print("Your weekly earning is", weekly_earning)

# Calculate the number of seconds a person can live
years_lived = int(input("Enter number of years you have lived: "))
seconds_lived = years_lived * 365 * 24 * 60 * 60
print("You have lived for", seconds_lived, "seconds")

# Display a table
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)
