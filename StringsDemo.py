str = "RahulShettyAcademy.com"
str1 = "Consulting firm"
str3 = "RahulShetty"

print(str[1])  #a

print(str[0:5]) #if you want substring in python

print(str+str1) #concatenation

print (str3 in str) #substring check

var = str.split(".")
print(var)
print(var[0])

str4 = "great"
print(str4.strip())
print(str4.lstrip())
print(str4.rstrip())

str4 = "   great   "

print("Original string:", "[" + str4 + "]")

print("Using strip():", "[" + str4.strip() + "]") #removes both sides

print("Using lstrip():", "[" + str4.lstrip() + "]")  #removes left side


print("Using rstrip():", "[" + str4.rstrip() + "]") #removes right side