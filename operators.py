#SECTION 2: BASIC OPERATIONS & MATHEMATICAL OPERATIONS
#1.Simple Calculator
print("SIMPLE CALCULATOR :")
num1= input("Enter first number :")
num2= input("Enter second number :")
print("The sum of the two numbers is : ", float(num1)+float(num2))
print("The difference  of the two numbers is : ", float(num1)-float(num2))
print("The product of the two numbers is : ", float(num1)*float(num2))  
print("The division of the two numbers is : ", float(num1)/float(num2))


#2. AREA OF SHAPES
print("AREA OF SHAPES :")
#CIRCLE
print("CIRCLE :")
radius = float(input("Enter the radius of the circle : "))  
area_circle = 3.14 * radius ** 2
print("The area of the circle is : ", area_circle)


#RECTANGLE
print("RECTANGLE :")
length = float(input("Enter the length of the rectangle : "))
width = float(input("Enter the width of the rectangle : "))
area_rectangle = length * width
print("The area of the rectangle is : ", area_rectangle)


#TRIANGLE
print("TRIANGLE :")
base = float(input("Enter the base of the triangle : "))
height = float(input("Enter the height of the triangle : "))
area_triangle = 0.5 * base * height
print("The area of the triangle is : ", area_triangle)


#3. EVEN OR ODD
print("EVEN OR ODD :")  
number = int(input("Enter a number : "))
if number % 2 == 0:
    print("The number is even.")    
else:    print("The number is odd.")

#4.STUDENT GRADE PERCENTAGE
print("STUDENT GRADE PERCENTAGE :")
marks_obtained = float(input("Enter marks obtained : "))
total_marks = float(input("Enter total marks : "))
percentage = (marks_obtained / total_marks) * 100
print("The percentage is : ", percentage, "%")


#5.BODY MASS INDEX (BMI)
print("BODY MASS INDEX (BMI) :")
weight = float(input("Enter weight in kilograms : "))
height = float(input("Enter height in meters : "))
bmi = weight / (height ** 2)
print("The BMI is : ", bmi)


#6.POWER & MODULUS
print("POWER & MODULUS :")
base = float(input("Enter the base number : ")) 
exponent = float(input("Enter the exponent : "))
power = base ** exponent
print("The result of ", base, " raised to the power of ", exponent, " is : ", power)
dividend = float(input("Enter the dividend : "))
divisor = float(input("Enter the divisor : "))  
modulus = dividend % divisor
print("The modulus of ", dividend, " divided by ", divisor, " is : ", modulus)


