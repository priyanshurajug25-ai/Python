# palindrome --> it is a word or something which have same word if read from the start or end 

new1 = [1,2,2,1,3]
new2 = new1.copy()
new2.reverse()
if(new1==new2):
    print("This is Palindrome")
else:
    print("This is NOT Palindrome")