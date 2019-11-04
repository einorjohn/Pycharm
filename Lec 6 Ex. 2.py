count = 0
word = input('Input Word: ')
ichar = input('Input Character: ')
for char in word:
    if ichar == char:
        count = count + 1
print('No of letters: ', count)