# satrlar
string = "Hello, World!"
string2= 'Python is fun.'
string3 = """hello world"""
string4 = '''hello world'''

print(string)
print(string2)
print(string3)
print(string4)



# massivlar 
set = ["apple", "banana", "cherry", 1, 2, 3]
print(set[0])

print(str(string2[0]).upper() + str(string2[1:]).upper())
# str(var).capitalize() makes the first letter of the string uppercase and the rest lowercase.


# slicing


string5  = "Munich is a beautiful city"
print(string5[0:6]) # prints "Munich"
print(string5[11:20]) # prints "beautiful"

string6 = "new string"
print(string6[-6:]) # prints "string"
print(string6[-6:-3]) # prints "str"





# string length
newstring= "    new string     "
print(len(newstring)) # prints the length of the string including empty spaces
print(len(newstring.strip())) #removes empty spaces from the beginning and end of the string


lowercased_string= "hello world"
print(lowercased_string.upper()) # converts the string to uppercase
print(lowercased_string.lower()) # converts the string to lowercase


# replacement
balance = "i have no money"
print(balance.replace("no", "lot of"))

its_not_me = "I am the good boy"
print(its_not_me.replace("I am", "You are"))


# splitting
new_sentence = "Ertadan men googleda ishlayman"
print(new_sentence.split(" ")) #splits each sentece using empty space and returns list of words! ""remember returns LIST"""
print(new_sentence.split(" ")[1]) #this returns one element from list and prints "men".    returns string


# listing

new_text = "here we go"
print(list(new_text)) #converts string to list of characters and returns it.  ['h', 'e', 'r', 'e', ' ', 'w', 'e', ' ', 'g', 'o']


# check existance of element in string or list
text = "assalomu alaykum dunyo"
in_text = "assalom" in text
print("here we checked list and ")
print(in_text) # prints True if "assalom" is found in text, otherwise False


# check not existance
not_in_text = "vaalaykum assalom" in text
print(not_in_text)



# we will check list to with this way
my_new_list = ["men", "sen", "ular"]
in_list = "men" in my_new_list
print("bu yerda men listda bormanmi?")
if in_list:
    print("sen bu listda borsan")
else:
    print("yo'q")


# satrlar

var1=1
var2=500
var3 = 15000

context = "{} apple is {} and total {}"

print(context.format(var1, 50000, var3))

# using index in format
context = "{1} apple is {0} and total 3kg {2}"
print(context.format(4000,1,12000))

