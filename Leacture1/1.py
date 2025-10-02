name = "New User"   # String datatype used for wring alphabets
age = 55            # Integer datatype from -ve to +ve including 0
money = 56.54       # Float datadype which have decimal points

# For numericals and numericals calculation ("") sign is not used

print("My name is : " , name, "My age is : " , age , "Money I have is : " , money)

print("My name is : " , name)
print("My age is : " , age)
print("I have money dept which is : " , money)

boolen = True       # Small f and t in False and True are not acceptable 
none = None
print(boolen , none)
print(type(name) , type(age) , type(money) , type(boolen), type(none)) # Used to print datatypes

# In the naming of the identifiers we can use special sign and can't start it with the numbers
# And there are also some reserved words which we can't use like (as,and,for,class etc...)

name1 = "sk"
name2 = 'sk'
name3 = '''sk'''
name4 = """sk"""
print(name1,name2,name3,name4)      # We can use different notations for the writing strings 
print(type(name1) , type(name2) , type(name3) , type(name4))

# Python is case sensitive language for example (Apple is not equal to apple)

# OPERATORS:-
# Arithmetic Operators:-
# (+) --> Add       (-) --> Substract       (*) --> Multiply        (/) --> divide gives in float       (%)  --> modulus gives remainder        (**) --> Power

# Relational Operators:-
# (==) --> Equals       (!=) --> Not equals     (>=) --> sign with equality     (>) --> sign

# Assignment Operators:-
# (=) --> Assign something      (+=) --> Add with asign and also we can do as in arthematic operators (-=),(%=),(/=) etc...

# Logic Operators:-
# (not) --> Opposite      (and) --> Both must be True       (or) --> Any one is True

print(age == money)     # Relational Operators gives us True False statement
print(age>money)
print(not (age>money))

v1 = True
v2 = True
v3 = False
v4 = False

print("answer is : " , v1 and v2) # Suppose v1 is fix then v3 --> False and v4 --> False
print("ans is : " , v3 or v4) # Suppose v3 fix then v2 --> True and v1 --> True
print("compare " , (money==age) or (money > age))

# Type conversion (Automatically by Python)
a = 5
b = 5.645

print(a+b)

# Type casting (Manually)
c = "55"
d = 65.87

print(int(c)+d)     # if we directly type print(c+d) so this will give error bcuz of string can't added to number like float & int
# We can't write the print(int("String")) bcuz it can't be converted into numbers
# But we can do vice versa
w = 55
w = str(w)
print(w, type(w))


# INPUTS:-
input("Enter your name : ")     # Dynamic we can type now in the terminal and can display based on that statements
age = input("Enter your age : ")
print ("Your age is : " , age , "Type of the value is : " , type(age))     # Input store the value in string even it is int,float etc...

money = int(input("How many money you got : "))     # Restrict to int values only as the int is typecast over the input type
print(money, type(money))


# Practice Problems are :-
# Sum of two numbers 
# Area of the square
# Average of the two numbers
# Which number is greater with equal operation also