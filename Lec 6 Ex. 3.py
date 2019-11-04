str = 'X-DSPAM-Confidence:0.8475’'
first = str.find(':')
second = str.find("’", first)
number = str[first+1:second]
number = float(number)
print(number)