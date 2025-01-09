#3- Write a Python program to write a list to a file
my_list = [1, 2, 3, 100, 200, 300]
my_file = 'C:/Users/Fatoom/Documents/text_files/my_file.txt'
try:
    with open(my_file, 'w') as f:
        for item in my_list:
            f.write(str(item) + '\n')
except FileNotFoundError:
    print('File not found')
