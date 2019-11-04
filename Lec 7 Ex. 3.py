finput = input('Enter filename: ')
if finput == 'na na boo boo':
    print('NA NA BOO BOO TO YOU - You have been punk`d!')
    quit()
try:
    fhand = open(finput)
except:
    print('File cannot be opened: ', finput)
    quit()
for line in fhand:
    line = line.rstrip()
    line = line.upper()
    print(line)