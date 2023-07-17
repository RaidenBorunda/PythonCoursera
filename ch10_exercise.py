fhand = open('romeo.txt')
counts = dict()
for line in fhand :
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
        #print(counts)
lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
    #print(key, val)
lst = sorted(lst, reverse=True)

for val, key in lst[:10] :
    print(key,val)