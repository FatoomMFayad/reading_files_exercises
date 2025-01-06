import os
directory_path = 'C:/Users/Fatoom/Documents/text_files'
files_list = os.listdir(directory_path)
files_sum_dic = {}
for file in files_list:
   f = open(os.path.join(directory_path , file))
   numbers = [int(number) for number in f]
   files_sum_dic.update({file: sum(numbers)})
print(files_sum_dic)
