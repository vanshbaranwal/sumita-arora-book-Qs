#write a program that reads two times in military format (0900, 1730)
#and prints the number of hours and minutes between two times.
#sample: enter first time : 0900
#        enter second time : 1730
#        8 hours 30 minutes

first_time=input("enter first time in military format : ")
second_time=input("enter second time in miltary format : ")

first_mins= int(first_time[:2])*60 + int(first_time[2:])
second_mins= int(second_time[:2])*60 + int(second_time[2:])

difference= second_mins - first_mins

hrs= difference//60
mins= difference%60

print(f"\nthe difference is :\t{hrs} hours {mins} minutes.")

