finput = input("Enter file name: ")
fhandle = open(finput)
words = fhandle.read()
wordlist = [] #or list()

for word in words.split():
    value = word
    value = value.lower()
    if value in wordlist:
        continue
    wordlist.append(value)

wordlist.sort()
print(wordlist)