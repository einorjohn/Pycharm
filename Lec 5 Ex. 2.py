smallest = None
biggest = 0
          value = input('Enter a number: ')
    if value == 'done':
        break
    try:
        value = float(value)
    except:
        print('Error. Invalid Input')
        continue
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    elif value > biggest:
        biggest = value
print('Minimum: ', smallest)
print('Maximum: ', biggest)