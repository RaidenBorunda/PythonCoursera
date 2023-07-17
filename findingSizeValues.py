# Largest so far

from multiprocessing.sharedctypes import Value


largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15] :
    if the_num > largest_so_far :
        largest_so_far = the_num
    print(largest_so_far, the_num)

print('After', largest_so_far)

# Smallest so far

smallest_so_far = None # Use this first. Super helpful
print('Before', smallest_so_far)
for value in [9, 41, 12, 3, 74, 15] :
    if smallest_so_far is None :
        smallest_so_far = value
    elif value < smallest_so_far :
        smallest_so_far = value
    print(smallest_so_far, value)

print('After', smallest_so_far)