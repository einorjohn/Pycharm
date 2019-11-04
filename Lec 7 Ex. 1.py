finput = input('Enter filename: ')
try:
    fhand = open(finput)
except:
    print('File cannot be opened: ', finput)
    quit()
for line in fhand:
    line = line.rstrip()
    line = line.upper()
    print(line)