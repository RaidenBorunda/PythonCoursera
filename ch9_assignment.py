# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
emails = dict()
bigemail = None
bigcount = None
for words in handle:
    if not words.startswith("From ") : continue
    # Split each line into individual items
    word = words.split()
    # Pull the second item in the list which is the email address
    word = word[1]
    # Incremental counter
    emails[word] = emails.get(word,0) + 1
for email,count in emails.items() :
    if bigcount is None or count > bigcount:
            bigemail = email
            bigcount = count
print(bigemail,bigcount)