#hours = input('Enter Hours: ')
#rate = input('Enter Rate: ')
def computepay(hours, rate):
    hours = float(hours)
    rate = float(rate)
    if hours > 40:
        pay = (40 * rate) + ((hours - 40) * (rate * 1.5))
        return pay
    elif hours <= 40:
        pay = hours * rate
        return pay
x = computepay(input('Enter Hours: '), input('Enter Rate: '))
print('Pay:', x)