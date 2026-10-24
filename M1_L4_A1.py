#Farm Harvest Calculator

#assignment operator

field1 = 10
field2 = 100
field3 = 111
field4 = 998
field5 = 7

total = field1 + field2 + field3 + field4 + field5
print("Total Harvest:", total)

average = total / 5
print("Average Harvest:", average)

#Arithmetic operators

price_per_kg = 7
earnings = total * price_per_kg
print("Earnings:", earnings)

bags = total // 25
print("Number of bags:", bags)
leftover_bags = total % 25
print("Leftover bags:", leftover_bags)

#Comparison operators

Last_year_harvest = 498
is_it_better = total > Last_year_harvest
print("Is this year's harvest better than last year's?", is_it_better)
is_it_same = total == Last_year_harvest
print("Is this year's harvest the same as last year's?", is_it_same)
is_it_greater = total >= Last_year_harvest
print("Is this year's harvest greater than or equal to last year's?", is_it_greater)

#Assignment operator - short hand

total += 10
print("Total Harvest (after adding 10):", total)
total -= 20
print("Total Harvest (after subtracting 20):", total)