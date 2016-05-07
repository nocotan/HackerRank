cost = float(input())
tip_per = int(input())
tax_per = int(input())

tip = cost * tip_per / 100
tax = cost * tax_per / 100

total = cost + tip + tax
print("The total meal cost is %d dollars." % round(total))
