hours = input('Enter Hours: ')
hours = float(hours)
rate = input('Enter Rate: ')
rate = float(rate)
if hours > 40:
    pay = (40*rate)+((hours-40)*(rate*1.5))
else:
    pay = hours*rate
print('Pay: ', pay)