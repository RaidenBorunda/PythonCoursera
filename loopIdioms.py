# Loopings
from ipaddress import summarize_address_range


zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + 1
    print(zork, thing)
print('After', zork)

# Summing Loops
zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + thing
    print(zork, thing)
print('After', zork)

# Finding the average in loops
count = 0
sum = 0
print('Before', count, sum)
for value in [9, 41, 12, 3, 74, 15] :
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, int(sum / count)) # An average combines the count and sum then divides.

# Filtering in a loop
print('Before')
for value in [9, 41, 12, 3, 74, 15] :
    if value > 20:
        print('Large Number', value)
print('After')

# Search using a boolean variable
found = False
print('Before', found)
for value in [9, 41, 12, 3, 74, 15] :
    if value == 3 :
        found = True
    print(found, value)
print('After', found)