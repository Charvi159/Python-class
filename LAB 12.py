#1
'''class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)
    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)
    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_part, imag_part)
    def __truediv__(self, other):
        denominator = other.real**2 + other.imag**2
        real_part = (self.real * other.real + self.imag * other.imag) / denominator
        imag_part = (self.imag * other.real - self.real * other.imag) / denominator
        return ComplexNumber(real_part, imag_part)
    def __str__(self):
        return f"{self.real} + {self.imag}i"
c1 = ComplexNumber(3, 4)
c2 = ComplexNumber(1, 2)
print("Addition:", c1 + c2)
print("Subtraction:", c1 - c2)
print("Multiplication:", c1 * c2)
print("Division:", c1 / c2)'''

#2
'''class Matrix:
    def __init__(self, data):
        self.data = data
    def __add__(self, other):
        return Matrix([[self.data[i][j] + other.data[i][j] for j in range(3)] for i in range(3)])
    def __mul__(self, other):
        result = [[sum(self.data[i][k] * other.data[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
        return Matrix(result)
    def transpose(self):
        return Matrix([[self.data[j][i] for j in range(3)] for i in range(3)])
    def display(self):
        for row in self.data:
            print(row)
        print()
matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print("Matrix 1:")
matrix1.display()
print("Matrix 2:")
matrix2.display()
print("Addition:")
(matrix1 + matrix2).display()
print("Multiplication:")
(matrix1 * matrix2).display()
print("Transpose of Matrix 1:")
matrix1.transpose().display()'''

#4
'''import math
class Shape:
    def __init__(self, shape_type, *dimensions):
        self.shape_type = shape_type.lower()
        self.dimensions = dimensions
    def perimeter(self):
        if self.shape_type == "square":
            return 4 * self.dimensions[0]
        elif self.shape_type == "rectangle":
            return 2 * (self.dimensions[0] + self.dimensions[1])
        elif self.shape_type == "circle":
            return 2 * math.pi * self.dimensions[0]
        else:
            return "Invalid shape"
    def area(self):
        if self.shape_type == "square":
            return self.dimensions[0] ** 2
        elif self.shape_type == "rectangle":
            return self.dimensions[0] * self.dimensions[1]
        elif self.shape_type == "circle":
            return math.pi * (self.dimensions[0] ** 2)
        else:
            return "Invalid shape"
    def display(self):
        print(f"Shape: {self.shape_type.capitalize()}")
        print(f"Perimeter/Circumference: {self.perimeter()}")
        print(f"Area: {self.area()}")
shape1 = Shape("square", 5)
shape2 = Shape("rectangle", 4, 6)
shape3 = Shape("circle", 3)

shape1.display()
shape2.display()
shape3.display()'''

#5
'''class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.normalize()
    def normalize(self):
        """Adjusts minutes and seconds properly."""
        self.minutes += self.seconds // 60
        self.seconds %= 60
        self.hours += self.minutes // 60
        self.minutes %= 60
    def add_time(self, other):
        """Adds two Time objects."""
        return Time(self.hours + other.hours, self.minutes + other.minutes, self.seconds + other.seconds)
    def subtract_time(self, other):
        """Subtracts two Time objects."""
        total_sec1 = self.hours * 3600 + self.minutes * 60 + self.seconds
        total_sec2 = other.hours * 3600 + other.minutes * 60 + other.seconds
        total_sec = abs(total_sec1 - total_sec2)
        return Time(total_sec // 3600, (total_sec % 3600) // 60, total_sec % 60)
    def display(self):
        """Prints time in HH:MM:SS format."""
        print(f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}")
# Example usage
t1 = Time(2, 45, 50)
t2 = Time(1, 30, 20)
print("Time 1:", end=" ")
t1.display()
print("Time 2:", end=" ")
t2.display()
print("Added Time:", end=" ")
t1.add_time(t2).display()
print("Subtracted Time:", end=" ")
t1.subtract_time(t2).display()'''

#6
'''class Date:
    def __init__(self, day, month, year):
        self.date = [day, month, year]  # Store as a list

    def __eq__(self, other):
        return self.date == other.date  # Compare lists directly

    def display(self):
        print(f"{self.date[0]:02}/{self.date[1]:02}/{self.date[2]}")

# Example usage
date1 = Date(10, 5, 2024)
date2 = Date(10, 5, 2024)
date3 = Date(11, 6, 2025)

# Display dates
print("Date 1:", end=" ")
date1.display()

print("Date 2:", end=" ")
date2.display()

print("Date 3:", end=" ")
date3.display()

# Compare dates
print("Are Date 1 and Date 2 equal?", date1 == date2)  # True
print("Are Date 1 and Date 3 equal?", date1 == date3)  # False'''


#7
'''class Weather:
    def __init__(self, parameters):
        self.parameters = parameters  # Store weather parameters in a list

    def __contains__(self, item):
        return item in self.parameters  # Check if the item exists in the list

    def display(self):
        print("Weather parameters:", self.parameters)


# Example usage
weather = Weather(["Temperature", "Humidity", "Wind Speed", "Pressure", "Rainfall"])

weather.display()

# Checking if a parameter exists
print("Is 'Humidity' in the weather parameters?", "Humidity" in weather)
print("Is 'Snowfall' in the weather parameters?", "Snowfall" in weather)'''

#8
class String:
    def __init__(self, text):
        self.text = text

    def __iadd__(self, other):
        """Overloaded += operator for string concatenation"""
        self.text += other.text
        return self

    def toLower(self):
        """Converts the string to lowercase"""
        return self.text.lower()

    def toUpper(self):
        """Converts the string to uppercase"""
        return self.text.upper()

    def display(self):
        """Displays the current string"""
        print(self.text)

str1 = String("Hello")
str2 = String(" World")

print("Original String 1:", end=" ")
str1.display()

print("Original String 2:", end=" ")
str2.display()

str1 += str2
print("After Concatenation:", end=" ")
str1.display()

print("Lowercase:", str1.toLower())

print("Uppercase:", str1.toUpper())
