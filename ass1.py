'''id = input("Enter employee id :")
name = input("Enter employee name :")
email = input("Enter employee email :")
contact = input("Enter employee contact :")
add = input("Enter employee address :")
dept = input("Enter employee department :")
print("---Employee Details---")
print("Employee id :",id)
print("Employee name :",name)
print("Employee email :",email)
print("Employee contact :",contact)
print("Employee address :",add)
print("Employee department :",dept)

num1= int(input("Enter first number :"))
num2= int(input("Enter second number :"))
print("Addition of two numbers :",num1+num2)
print("Subtraction of two numbers :",num1-num2)
print("Multiplication of two numbers :",num1*num2)
print("Division of two numbers :",num1/num2)
print("Remainder of two numbers :",num1%num2)'''

# List of 10 student names
students = [
    "Avi", "Diya", "Ritika", "Priya", "Vijay",
    "Nisha", "Rahul", "Darshan", "Rudra", "Maithu"
]

# Add a new student
students.append("Janhavi")

# Remove a student
students.remove("Rahul")

# Display all students
print("Student List:")
for student in students:
    print(student)