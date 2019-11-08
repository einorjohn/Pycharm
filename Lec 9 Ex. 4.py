counts = {}
fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()
for line in fhand:
    lineslist = line.split()
    if line.startswith('From '):
      email=lineslist[1]
      domain = email.split('@')[1]
      if domain not in counts:
        counts[domain] = 1
      else:
        counts[domain] = counts[domain] + 1
print(counts)