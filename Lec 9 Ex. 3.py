counts = dict()
largest = 0
max_email = None
fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()
for line in fhand:
    if line.startswith('From:'):
        line = line.split()
        email = line[1]
        counts[email] = counts.get(email,0)+1
for i in counts:
    email_val = counts.get(i)
    if largest < email_val:
        largest = email_val
for i in counts:
    if counts.get(i) == largest:
        max_email = i
print('{0} {1}'.format(max_email,largest))
