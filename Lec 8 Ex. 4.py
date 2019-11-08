collect = []
while True:
    inp= input('Enter a number: ')
    if inp == 'done':
        break
    try:
        inp = float(inp)
    except:
        print('Please input a numerical value')
        continue
    collect.append(inp)
if len(collect) == 0:
    print('Please enter a numerical value first!')
else:
    print('Maximum is: ', max(collect))
    print('Minimum is: ', min(collect))


