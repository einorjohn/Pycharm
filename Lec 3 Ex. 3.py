grade = input('Enter Score: ')
try:
    grade = float(grade)
except:
    grade = 1
if grade >= 1:
    print('Error, input a numerical grade that is between 0.0 and 1.0')
elif grade >= 0.9:
    print('A')
elif grade >=0.8:
    print('B')
elif grade >=0.7:
    print('C')
elif grade >=0.6:
    print('D')
else:
    print('F')