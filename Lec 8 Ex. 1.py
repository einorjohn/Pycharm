numlist = list()
numlist2 = list()
def chop(list):
    del list[0]
    del list[-1]
def middle(list):
    return list[1:-1]
while True:
    str = input('Enter a sentence: ')
    if str =='done':
        break
    numlist.append(str)
print(numlist)
numlist2 = middle(numlist)
print(numlist2)
print(numlist)

    #chopped = chop.split()
    #print(chopped)
    #chop(list)