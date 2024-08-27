#write a python program that accepts two integers from the user and prints a message saying if 
# first number is divisible by the second number or if it is not.

x=int(input("enter first number : "))
y=int(input("enter second number : ")) 

if(x%y==0):
    print(f"{x} is divisible by {y}.")

else:
    print(f"{x} is not divisible by {y}.")

