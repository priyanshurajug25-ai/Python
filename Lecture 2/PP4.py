a = int(input("First number : "))
b = int(input("Second number : "))
c = int(input("Third number : "))

if(a>b):
    if(a>c):
        print("The answer is",a)
    else:
        print("The answer is",c)
elif(b>c):
    if(b>a):
        print("The answer is",b)
    else:
        print("The answer is",a)
elif(c>a):
    if(c>b):
        print("The answer is",c)
    else:
        print("The answer is",b)

# I can use max function but not have been learned in this lecture so use basic logic