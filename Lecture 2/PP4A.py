a = int(input("First number : "))
b = int(input("Second number : "))
c = int(input("Third number : "))

if(a>b and a>c):
    print("The answer is : ",a)
elif(b>c and b>a):
    print("The answer is : ",b)
elif(c>a and c>b):
    print("The answer is : ",c)

# To use and 