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
