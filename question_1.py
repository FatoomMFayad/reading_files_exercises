#1- Write a Python program to read a file line by line and store each line into a list.
f = open('C:/Users/Fatoom/Documents/names.txt')
lines = [line.strip() for line in f.readlines()]
print(lines)