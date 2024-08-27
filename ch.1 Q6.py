#one foot equals to 12 inches. write a function that accepts a length written in
#feet as an argument and returns this length written in inches.
#write a second function that asks the user for a number of feets and returns 
#this value.
#write a third function that accepts a number of inches and displays this to the screen.
#use these three functions to write a program that asks the user for a number of feet
#and tells them the corresponding number of inches.

def feet_to_inches(feet):
    inches=12
    one_foot=inches    
    result=one_foot*feet
    print(f"\n{feet} feet is equal to {result} inches.")
    return
    
def num_feets():
    feets=int(input("enter the number of feets : "))
    print(f"\nthe number of feets is {feets}")
    return

def etr_inches():
    num_inches=int(input("enter the number of inches : "))
    print(f"the number of inches is {num_inches}")
    return


feet=int(input("enter number of feet to get it in inches : "))   
feet_to_inches(feet)


