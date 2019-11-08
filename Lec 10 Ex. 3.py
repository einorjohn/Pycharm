import string
fname = input('Enter file name: ')
try:
	fhandle = open(fname)
except:
	print('File cannot be opened:', fname)
	exit()
letters = dict()
for line in fhandle:
	line = line.translate(string.punctuation)
	line = line.translate(string.digits)
	line = line.lower()
	words = line.split() #Sir nagtry na po ako magsearch sa marami, lahat sila ginagamit ang code na 'to remove punctutation pero ayaw pa rin sa'kin gumana
	for t in words:
		word = list(t)
		for letter in word:
			letters[letter] = letters.get(letter,0) + 1
letterlist = []
for letter, count in letters.items():
	letterlist.append( (count, letter) )
letterlist.sort(reverse=True)
for count, letter in letterlist:
	print(letter, count)