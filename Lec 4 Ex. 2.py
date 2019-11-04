def computegrade(grade):
    grade = float(grade)
    if grade >= 1:
        return 'Error, input a numerical grade that is between 0.0 and 1.0'
    elif grade >= 0.9:
        return 'A'
    elif grade >=0.8:
        return 'B'
    elif grade >=0.7:
        return 'C'
    elif grade >=0.6:
        return 'D'
    else:
        return 'F'
x = computegrade(input('Enter Score: '))
print('Grade: ', x)