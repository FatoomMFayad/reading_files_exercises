#2- Write a Python program to read first n lines of a file
i  = 0
f = open('C:/Users/Fatoom/Documents/names.txt')
lines = f.readlines()
names = []
for line in lines:
    if i <= 3:
        names.append(lines[i].strip())
        i+=1
print(names)