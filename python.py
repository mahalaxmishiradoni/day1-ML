# ==========================================
# Python Basic Programs
# Author: Mahi
# Description: Collection of basic Python programs for beginners.
# ==========================================

# Program 1: Print a String
name = "mahi"
print(name)

# Program 2: List Creation and Assignment
Subjects = ["Python", "Java", "C"]
Fav = Subjects
print(Fav)

# Program 3: Traverse a List Using a Loop
Cities = ["Athani", "Vijaypur", "Bagalkot"]
for city in Cities:
    print(city)

# Program 4: Print Numbers Using range()
for i in range(1, 10):
    print(i)

# Program 5: Function to Add Three Numbers
def add(a, b, c):
    return a + b + c

print(add(1, 2, 4))

# Program 6: Print a Message
print("HELLO WORLD!")

# Program 7: Check Whether a Number is Even or Odd
number = int(input("Enter any number: "))
if number % 2 == 0:
    print("EVEN")
else:
    print("ODD")

# Program 8: Find the Largest of Two Numbers
a = float(input("Enter number for a: "))
b = float(input("Enter number for b: "))

if b > a:
    print("b is greater than a")
else:
    print("a is greater than or equal to b")

# Program 9: Print Multiplication Table
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# Program 10: Find the Sum of First n Natural Numbers
n = int(input("Enter n: "))
s = 0

for i in range(1, n + 1):
    s += i

print("Sum =", s)

# Program 11: Find the Factorial of a Number
number2 = int(input("Enter a number: "))
f = 1

for i in range(1, number2 + 1):
    f *= i

print("Factorial =", f)

# Program 12: Generate Fibonacci Series
n = int(input("Enter the number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

print()

# Program 13: Reverse a Number
num = int(input("Enter a number: "))
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

print("Reverse =", rev)

# Program 14: Check Whether a Number is Prime
num = int(input("Enter a number: "))
count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count += 1

if count == 2:
    print("Prime")
else:
    print("Not Prime")

# Program 15: Check Whether a Number is Palindrome
num = int(input("Enter a number: "))
temp = num
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

if num == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

# Program 16: Swap Two Numbers
a = 10
b = 20

print("Before Swapping:", a, b)

a, b = b, a

print("After Swapping:", a, b)
