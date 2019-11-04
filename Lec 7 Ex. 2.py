finput = input('Enter filename: ')
count = 0
digit = 0
try:
    fhand = open(finput)
except:
    print('File cannot be opened: ', finput)
    quit()
for line in fhand:
    if line.startswith('X-DSPAM-Confidence: '):
        line.rstrip()
        first = line.find(' ')
        number = line[first+1:]
        count = count + 1
        digit = digit + float(number)
average = digit/count
print('Average: ', average)


    #number = line[first + 1:]
    #number = float(number)
    #count = count + 1
#ave = number/count
#print('Average spam confidence: ', ave)
