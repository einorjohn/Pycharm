collect = []
while True:
    inp = input('Enter a number: ')
    if inp =='done':
        break
    value = float(inp)
    collect.append(value)
print('Maximum is: ', max(collect))
print('Minimum is: ', min(collect))


