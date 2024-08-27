#write a program that prints a table on 2 columns - table that helps
#converting miles into kilometres.
# 1 mile = 1.609 kilometres
#yes a mile is greter than a kilometre.

miles=float(input("enter a range in miles : "))

print()
print("\tmiles\t|\tkilometres")

kilometres=1.609*miles

print(f"\t{miles} \t\t {kilometres: .2f}")

