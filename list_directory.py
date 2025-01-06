import os
files_list = os.listdir('C:/Users/Fatoom/Documents/text_files')
for file in files_list:
   f = open('C:/Users/Fatoom/Documents/text_files/' + file)
   numbers = f.readlines()
   numbers2 = [int(number) for number in numbers]
   print(sum(numbers2))
