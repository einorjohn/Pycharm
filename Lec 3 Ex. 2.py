hours = input('Enter Hours: ')
try:
    hours = float(hours)
except:
    hours = 0
if hours == 0:
    print('Error, please enter numeric input')
else:
    print("")
rate = input('Enter Rate: ')
try:
    rate = float(rate)
except:
    rate = 0
if rate == 0:
    print('Error, please enter numeric input')
else:
    print("")
if hours > 40:
    pay = (40*rate)+((hours-40)*(rate*1.5))
else:
    pay = hours*rate
if pay <= 0:
    print('Error, please repeat and enter numeric inputs')
else:
    print('Pay: ', pay)