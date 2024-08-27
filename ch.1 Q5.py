#write a program that asks the user the day number in the year in the range
#2 to 365 and ask the first day of the year - sunday, monday, tuesday
#then the program should display the day on the day number that has been input.
import calendar

day_names=["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

day_number=int(input("enter the day number (2-365) : "))
first_day=input("enter the first day of the year : ")

if(day_number<2 or day_number>365):
    print("invaild day number.")
else:
    startdayidx=day_names.index(str.lower(first_day))
    currentdayidx=day_number % 7 + startdayidx - 1
    
    if currentdayidx >=7:
        currentdayidx=currentdayidx-7
        
    print(f"day on day number {day_number} : {day_names[currentdayidx]}.")
    
    