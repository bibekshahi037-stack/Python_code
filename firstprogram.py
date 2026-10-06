# for single line comment ctrl slash
""" 
for multi-line comment shift alt A

""" 
#python is dynamically typed language so we don't need to declare the type of variable
name = input("Enter the name")
age = int (input("Enter the age"))
location =input("Enter thr location")
#concate 
print("My name is " + name + " and my age is " + str(age)+" Location is "+location)
#f string
print(f"My name is {name} and my age is {age} and the location is {location}")
#format old version 
print("My name is %s and my age is %d and location is %s" % (name, age, location))
#format new version 
print("My name is {0} and my age is {1} and location is {2}".format(name, age, location))


num1 = input("Enter your num1")
num2 = input("Enter your num2")
sum1 = int(num1) + int(num2)
print("The sum is" + sum1 + "and the type is" + type(sum1))

num3 = int(input("Enter the num1"))
num4 = int(input("Enter the num2"))
sum2 = num3 + num4
print("The sum is" + sum2 + "and the type is" + type(sum2))
#print(5 and 6 or"success")

#Did any changes occur in the thing?
# print ("looking for changes")
#print ("apple"<"Apple")

""" print("apple"<"banana")

print(ord('😩'))

print(chr(128553))

print(chr(87))
print(chr(91))
 """
#Write a program that prints a short poem using \n.
""" print("My feelings for you still linger \n"
      "Its both a curse and a blessing \n"
      "The days when I am happy its a curse \n"
      "because it reminds me how happy I was with you \n"
      "And a blessing in those days when I am at my lowest \n"
      "because it reminds me how happy I can be \n"
      "I hope when I die and my ashes are poured in the same river as yours \n"
      "So that when my ashes meets yours \n"
      "I will be able to say you everything I couldnt") 
 """
#Write a short program to print something inside quotation.

""" print(f"Hello my name is Ken and I beileve in the quote \"nothing is free everything is permitted\"")

path1 = "C:\\Users\\User\\OneDrive\\Pictures"
print(path1)
 """

#AND -1 only where both bits are 1
print(5&3)

#bin shows the binary representation of any number
print(bin(4))

#OR -1 where either bit is 1
print(5|3)

#XOR -1 where bits are different
print(5^3) # for eg if there is same bits such as 1 and 1 then the result is 0 but if there is diff such as 0 and 1 then the result is 1

#Left shift  multiple by powers of 2
print(5 << 1) # 5 * 2 #binary digits move to left
print(5 << 2) # 5 * 4

#Right shift - divide by powers of 2
print(20 >> 1) #20 divied by 2
print(20 >> 2) #20 divied by 4

a = [1,2,3]
b = [1,2,3]
c = a

print (a is b)
print (a is c)
print (a == b)
print (a == c)
print (id (a))
print (id(b))
print (id(c))


# ============================================================
# PYTHON OPERATORS NOTES
# ============================================================

# Operators are symbols used to perform operations on values
# and variables.


# ============================================================
# 1. ARITHMETIC OPERATORS
# ============================================================

a = 10
b = 3

# Addition (+)
# Adds two values together.
print(a + b)       # Output: 13

# Subtraction (-)
# Subtracts the second value from the first value.
print(a - b)       # Output: 7

# Multiplication (*)
# Multiplies two values.
print(a * b)       # Output: 30

# Division (/)
# Divides the first value by the second value.
# The result is always a float.
print(a / b)       # Output: 3.3333333333333335

# Floor Division (//)
# Divides two values and returns only the whole-number part.
print(a // b)      # Output: 3

# Modulus (%)
# Returns the remainder after division.
print(a % b)       # Output: 1

# Exponentiation (**)
# Raises the first value to the power of the second value.
print(a ** b)      # Output: 1000


# ============================================================
# 2. ASSIGNMENT OPERATORS
# ============================================================

x = 10

# Assignment (=)
# Assigns the value 10 to the variable x.
x = 10
print(x)

# Addition Assignment (+=)
# Adds a value to the variable and assigns the result back.
x += 5
print(x)           # Output: 15

# Subtraction Assignment (-=)
# Subtracts a value from the variable and assigns the result back.
x -= 3
print(x)           # Output: 12

# Multiplication Assignment (*=)
# Multiplies the variable by a value and assigns the result back.
x *= 2
print(x)           # Output: 24

# Division Assignment (/=)
# Divides the variable by a value and assigns the result back.
x /= 4
print(x)           # Output: 6.0

# Floor Division Assignment (//=)
# Performs floor division and assigns the result back.
x //= 2
print(x)           # Output: 3.0

# Modulus Assignment (%=)
# Finds the remainder and assigns it back to the variable.
x %= 2
print(x)           # Output: 1.0

# Exponentiation Assignment (**=)
# Raises the variable to a power and assigns the result back.
x **= 3
print(x)           # Output: 1.0


# ============================================================
# 3. COMPARISON OPERATORS
# ============================================================

a = 10
b = 5

# Equal to (==)
# Checks whether two values are equal.
print(a == b)      # Output: False

# Not equal to (!=)
# Checks whether two values are different.
print(a != b)      # Output: True

# Greater than (>)
# Checks whether the first value is greater than the second.
print(a > b)       # Output: True

# Less than (<)
# Checks whether the first value is less than the second.
print(a < b)       # Output: False

# Greater than or equal to (>=)
# Checks whether the first value is greater than or equal to the second.
print(a >= b)      # Output: True

# Less than or equal to (<=)
# Checks whether the first value is less than or equal to the second.
print(a <= b)      # Output: False


# ============================================================
# 4. LOGICAL OPERATORS
# ============================================================

age = 20
has_id = True

# AND (and)
# Returns True only when both conditions are True.
print(age >= 18 and has_id)       # Output: True

# OR (or)
# Returns True when at least one condition is True.
print(age >= 18 or has_id)        # Output: True

# NOT (not)
# Reverses the Boolean result.
print(not has_id)                 # Output: False


# ============================================================
# 5. IDENTITY OPERATORS
# ============================================================

x = [1, 2, 3]
y = x
z = [1, 2, 3]

# is
# Checks whether two variables refer to the same object in memory.
print(x is y)                      # Output: True

# is not
# Checks whether two variables do not refer to the same object.
print(x is not z)                  # Output: True


# ============================================================
# 6. MEMBERSHIP OPERATORS
# ============================================================

numbers = [10, 20, 30, 40, 50]

# in
# Checks whether a value exists inside a sequence.
print(30 in numbers)               # Output: True

# not in
# Checks whether a value does not exist inside a sequence.
print(60 not in numbers)           # Output: True


# ============================================================
# 7. BITWISE OPERATORS
# ============================================================

a = 10       # Binary: 1010
b = 3        # Binary: 0011

# Bitwise AND (&)
# Compares each bit and returns 1 only when both bits are 1.
print(a & b)                         # Output: 2

# Bitwise OR (|)
# Compares each bit and returns 1 when at least one bit is 1.
print(a | b)                         # Output: 11

# Bitwise XOR (^)
# Returns 1 when the corresponding bits are different.
print(a ^ b)                         # Output: 9

# Bitwise NOT (~)
# Inverts all bits of the number.
print(~a)                            # Output: -11

# Left Shift (<<)
# Shifts the bits to the left.
print(a << 1)                        # Output: 20

# Right Shift (>>)
# Shifts the bits to the right.
print(a >> 1)                        # Output: 5


# END OF PYTHON OPERATORS NOTES
