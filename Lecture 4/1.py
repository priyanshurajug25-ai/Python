# Dictionary
# dict = {
#     "key1" : "value1",
#     "key2" : "value2",
# }

info = {
    "Name" : "NEW USER",
    ("New", "Class" , "Boards") : 12,
    12 : 50.4,
    "Adult" : True,
    15.26 : ["English , Maths, Physics, Chemistry"],
    True : ("Banana", "Apple", "Gauva")
}
# In value all datatypes are valid but in key dict and list are not acceptable but tuple can be because of non change able feature
# Dict are non order(no indexing) , it is changable , not duplicate key
print(info)
print(type(info))

print(info["Name"])

info["Name"] = "Kon hu meh"     # Overwrite value
info["Surname"] = "Pta nhi kya likhu"   # Making new key and value

print(info)

null_dict = {}
print(null_dict)



# Nested Dictionary

student = {
    "Name" : "Kumar",
    "Subject" : {
        "Physics" : 95 ,
        "Chemistry" : 88 ,
        "Maths" : 55.5,
    },
    "Percentage" : "92%",
    "DOB" : {
        "Date" : "15",
        "Day" : "Monday"
    }
}

print(student)
print(student["Subject"]["Chemistry"])



# Dictionary Methods
# dict.key() --> Return all keys
print(student.keys())