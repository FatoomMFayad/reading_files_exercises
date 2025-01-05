#3- Write a Python program to write a list to a file
file = open('C:/Users/Fatoom/Documents/lists.txt', "w")
cities = ["Gaza", "Deir El-Balah", "Khanyounis", "Rafah"]
for city in cities:
    file.write(city + '\n')
file.close()
