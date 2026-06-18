print("----- Student Grade Calculator -----")
sub1 = int(input("Enter marks of Subject 1: "))
sub2 = int(input("Enter marks of Subject 2: "))
sub3 = int(input("Enter marks of Subject 3: "))
sub4 = int(input("Enter marks of Subject 4: "))
sub5 = int(input("Enter marks of Subject 5: "))
total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = total / 5
print("\nTotal Marks =", total)
print("Percentage =", percentage, "%")
if sub1 < 35 or sub2 < 35 or sub3 < 35 or sub4 < 35 or sub5 < 35:
    print("Failed in Subject")
else:
    # Grade Calculation
    if percentage >= 75:
        print("Result: Distinction")
    elif percentage >= 60:
        print("Result: First Class")
    elif percentage >= 50:
        print("Result: Second Class")
    elif percentage >= 35:
        print("Result: Pass")
    else:
        print("Result: Fail")