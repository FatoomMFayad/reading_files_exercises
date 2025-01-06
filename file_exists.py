import os

file_path = 'C:/Users/Fatoom/Documents/text_files/numbers1.txt'
file_size = os.path.getsize(file_path)

if os.path.exists(file_path) and file_size > 0:
    f = open(file_path, 'r')
    print(f.read())
    f.close()
else:
    print('File does not exist')