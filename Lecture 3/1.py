marks = [99.4, 95.2, 33.4, 45.1]        # List in python like array can be modefied and no need of same type of dataset
print(marks)        # Same indexing as in normal cases 
print(type(marks)) 
print(len(marks))   # Length of the list as there are only 4 marks
student = ["User", 857.44, "Maths", 99, "Physics", 85]
print(student[0])
student[0] = "New"
print(student)

# Here slicing as well as negative slicing can be done as same as in previous lectures


# List Methods
# list.append(write_something) --> adds one element to the end 
student.append("Kon ho tum")
print(student.append("Kon ho tum"))     # Make changes in the original 
print(student)

# list.sort() --> sort in asceding order
marks.sort()
print(marks.sort())     # Make changes in the original 
print(marks)

# list.sort(reverse=True)
marks.sort(reverse=True)
print(marks)
string1 = ["a", "b", "apple", "banana"]
string1.sort()      # Sorted by the rank of the string 
print(string1)

# list.reverse() --> It reverse the list
string1.reverse()
print(string1)

# list.insert(index,element) --> It is same as append but it specifically denoted at which index 
string1.insert(3,5555)
print(string1)

# list.remove(element) --> remove first occurance of element
rev = [1, 5 ,4 , 1 , 9 , 1]
rev.remove(1)
print(rev)

# list.pop(index) --> remove element for particular index
rev.pop(3)
print(rev)



# Tuples

new = (2,1,2,5,3,4,5,3)
print(new)
print(type(new))
# new[3] = 5        can't do that. Tuples can't be changes in that index 
# for single value tuple 
# tup = (element ,)     is correct          not like    tup = (element)     this is an integer 
# for multiple values in tuples the last comma is optional
# Slicing is there also
tup = (1)
tup1 = (1,)
print(type(tup), type(tup1))



# Tuple Methods
# tup.index(element) --> returns index of fifrst occurance
print(new.index(3))

# tup.count(element) --> count the total number of occurance
print(new.count(5))