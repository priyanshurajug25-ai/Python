# We use different types of strings notations like (single and double quotes) becuase the use of 's like that

# Escape sequence characters
# (\n) --> for next line        (\t) --> for tab
st = "I am a new user. I want to enjoy my life" 
st1 = "I am a new user. \nI want to enjoy my life"
st2 = "I am a new user. \tI want to enjoy my life"
print(st)
print(st1)
print(st2)



# Operations on strings
# Concatenation --> "add" + "two strings" = addtwo strings
# length of the string --> len(str)         it also include spaces and other characters
n = "New User"
n1 = "Is here"
n2 = n+n1
print(n2)
print(len(n2))



# Indexing (As same as in Cpp)
# n2[5] = "k"       |   Index assigning is not allowed in python  
print(n2[5])

# Slicing 
# str[starting index : ending index]        | Starting index inclued whereas ending index is not included
print(n2[5:9])
print(n2[5:])  #Index 5 till the last index
print(n1[2:len(n1)])  #Index 5 till the last index
print(n2[:6])   #Index start form 0 till given index



# Negative index in Slicing 
# The last index is -1 and it keep on decresing till -n
print(n2[-8:-1])



# String functions 
# To check the last word is same in the string or not --> str.endswith("last_word")     |   boolen type
print(n2.endswith("here"))
print(n2.endswith("yere"))

# To capitalize the string --> str.capitalize()
k = "who are you ?"
print(k.capitalize())   # Don't change the original string
print(k)    # If you want to make changes in the original so you have to assign it and then print it

# To replace old to new value --> str.replace("old","new")
print(k.replace("o","a"))   # Also change full sentence 

# Find any word in the string --> str.find("word")
print(k.find("o"))  # Give me the first index where it find "o" in first time
print(k.find("z"))  # Gives me -1 because z is not there

# Count when it been occured --> str.count()
print(n2.count("e"))    # Count how many a is there we can use the different words/sentences also



# Conditional Statements
# if(condition): statement1       elid(condition): statement2         else: statement3          same as in Cpp
traffic_light = "yellow"
if(traffic_light == "green"):
    print("Go")
elif(traffic_light == "yellow"): 
    print("Ready")
else: 
    print("Stop")       # Indentation --> proper spacing



# Nesting 
# if(statement):
#     if(statement2):
#         print("This is nestiong if inside if or elif")

