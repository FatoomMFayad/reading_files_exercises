import os

file_path = 'C:/Users/Fatoom/Documents/text_files/numbers15.txt'
if os.path.exists(file_path):
    f = open(file_path, 'r')
    print(f.read())
    f.close()
else:
    print('File does not exist')