#Given a .txt file that has a list of a bunch of names,
# count how many of each name there are in the file,
# and print out the results to the screen.
# The result should be a dictionary where keys are the names, and values are the counts.

file_name = 'C:/Users/Fatoom/Documents/names.txt'
names = []

try:
    with open(file_name, 'r') as file:
        names = file.readlines()
        names_count = {}
        for name in names:
            name = name.strip()
            if name in names_count:
                names_count[name] += 1
            else:
                names_count[name] = 1
        print(names_count)

except FileNotFoundError:
    print(f"{file_name} does not found" )