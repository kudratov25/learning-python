# o'zgaruvchilar



num= 4
num_none= None  #we can also assign None to a variable
print(num)
print(num_none)

string = "Hello World"
print(string)

# we can also change the value of a variable
num = 10
print(num)

string = "Python is fun"
print(string)

# we can also change from one data type to another
num = 5
print(num)
num = 5.5
print(num)
num = "Five"
print(num)

# multiple variables in one line
x, y, z = 1, 2, 3
print(x, y, z)

# or 
a = b = c = 5
print(a, b, c)

# and also we can print string with 
string = "Hello"
print(string + " World")

str1= "Hello"
str2= " World"
print(str1 + str2)


var1= 1
var2= " World"
print(str(var1) + var2)#if we use without str() it will give an error because we can't concatenate int and str
# in order to user variables in strin we use f-string
print(f"{var1} {var2}")


# functions in python uses "def" keyword

def my_function():
    print("this is my function")

my_function()


# for passing arguments to a function we can use parameters
def my_func2(name="User"):
    print(f"Hello {name}")

my_func2()
my_func2("Bob")#we can also pass arguments to a function

# in order to make global variable we can use "global" keyword
def my_func3():
    global name 
    name= "John Doe"
    print(name)

my_func3()