# Open the file romeo.txt and read it line by line. 
# For each line, split the line into a list of words using the 
# split() method. The program should build a list of words. 
# For each word on each line check to see if the word is already
# in the list and if not append it to the list. 
# When the program completes, sort and print the resulting 
# words in python sort() order as shown in the desired output.

#fname = input("Enter file name: ")
# words that start with a capital letter come before words that start with a lower case letter
fh = open('romeo.txt')
lst = []
for line in fh:
    nline = line.strip()
    stuff = nline.split()
    lst.append(stuff)
    lst.sort()
for x in lst[1] :
    if x not in lst[0] :
        lst[0].append(x)
for y in lst[2] :
    if y not in lst[0] :
        lst[0].append(y)
for z in lst[3] :
    if z not in lst[0] :
        lst[0].append(z)
lst[0].sort()
print(lst[0])


# print(lst[0:1])

