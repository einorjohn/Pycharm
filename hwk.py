string = input("Input Word: ")
char = input("Input Character: ")

count=0
for i in range(len(string)):
    if(string[i] == char):
        count = count + 1

print("No. of times",char, "was present in", string, ":", count )
