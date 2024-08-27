#write a program printing a table with two columns that helps converting
#pounds in kilograms
#1 pound is equal to 0.4535 kilograms

pounds=float(input("enter the weight in pounds : "))
print("\n\tPounds\t|\tKilograms")

kilograms=0.4535*pounds

print(f"\t{pounds} \t\t\t {kilograms: .2f}")

