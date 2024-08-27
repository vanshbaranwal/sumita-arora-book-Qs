#write a program that reads a date as an integer in the format MMDDYYYY.
#the porgram will call a function that prints print out the date in the format.
#<Month Name>, <Day>, <Year>.
#sample :   December 25, 2019

months=["january", "february", "march", "april", "may", "june", "july", "august",
        "september", "october", "november", "december"]

datestr=input("enter the date in ['MMDDYYYY'] format : ")

monthidx=int(datestr[:2])-1
month=months[monthidx]
month=month.title()

day=datestr[2:4]
year=datestr[4:]

print("\nthe date is : \n")
print(f"{month} {day}, {year}")