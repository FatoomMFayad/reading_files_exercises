import os
directory_path = 'C:/Users/Fatoom/Documents/text_files'
files_list = os.listdir(directory_path)
for file in files_list:
   f = open(os.path.join(directory_path , file))
   numbers = [int(number) for number in f]
   print(sum(numbers))
