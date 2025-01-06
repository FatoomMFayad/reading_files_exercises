import os
files_list = os.listdir('C:/Users/Fatoom/Documents/text_files')
for file in files_list:
   f = open('C:/Users/Fatoom/Documents/text_files/' + file)
   numbers = [int(number) for number in f]
   print(sum(numbers))
