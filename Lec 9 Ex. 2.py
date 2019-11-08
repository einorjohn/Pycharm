fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()
counts = dict()
for line in fhand:
    if line.startswith('From:'):
        line = line.split()
        email = line[1]
        counts[email] = counts.get(email,0) + 1
print(counts)