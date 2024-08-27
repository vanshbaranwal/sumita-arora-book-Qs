#write a program to print one of the words negative, zero, or positive, according to whether variable x is less than
#zero, zero, or greater than zero, respectively.

x=int(input("enter a number : "))

if(x==0):
    print("the number entered by the user is zero.")
elif(x<0):
    print("the number entered is a negative number.")
else:
    print("the number entered is a positive number.")

