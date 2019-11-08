days = dict()
fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    else:
        if words[2] not in days:
            days[words[2]] = 1
        else:
            days[words[2]] = days[words[2]] + 1

print(days)