total = 0
count = 0
while True:
    value = input('Enter a number: ')
    if value == 'done':
        break
    try:
        value = float(value)
    except:
        print('Error. Invalid Input')
        continue
    count = count + 1
    total = value + total
print('Sum: ', total, 'Count: ', count, 'Average: ', total/count)

