finput = input('Enter filename: ')
count = 0
collect = []
try:
    fhand = open(finput)
except:
    print('File cannot be opened: ', finput)
    quit()
for line in fhand:
    if line.startswith('From '):
        #line.rstrip()
        #first = line.find(' ')
        #number = line[first+1:]
        words = line.split()
        email = words[1]
        collect.append(email)
        count = count + 1
for word in collect:
    print(word)
#    if word in collect:
 #       continue
#print(collect[:])
print('There were', count, 'lines with From as the first word')