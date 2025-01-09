#1- Write a Python program to read a file line by line and store each line into a list.
filename = 'C:/Users/Fatoom/Documents/text_files/numbers1.txt'
lines_list = []
try:
    with open(filename, 'r') as f:
        lines_list = f.readlines()
        lines_list = [line.strip() for line in lines_list]
        print(lines_list)
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")