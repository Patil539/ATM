# def prime(n):
#     for i in range(2,n):
#         if n%i==0:
#             return "Not Prime..."
#     return "Prime..."
# print(prime(100))
# print(prime(45))
# print(prime(22))
# print(prime(98))
# print(prime(11))

# def fib(n):
#     a, b = 0, 1
#     for i in range(n):
#         print(a, end=" ")
#         a, b = b, a+b
#
# fib(8)

# def palindrome(x):
#     if str(x) == str(x)[::-1]:
#         print("Palindrome")
#     else:
#         print("Not Palindrome")
#
# palindrome(121)
# palindrome("madam")

# def armstrong(n):
#     s = 0
#     for i in str(n):
#         s += int(i)**3
#     print("Armstrong" if s == n else "Not Armstrong")
#
# armstrong(153)
# armstrong(370)
# armstrong(123)

square = lambda x: x*x
cube = lambda x: x*x*x
maxi = lambda a,b: a if a>b else b
eo = lambda x: "Even" if x%2==0 else "Odd"
cf = lambda c: c*9/5+32

print(square(5))
print(cube(3))
print(maxi(10,20))
print(eo(7))
print(cf(25))