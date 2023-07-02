import os
from pprint import pprint
folder_path = r'C:\Users\liss2\OneDrive\Рабочий стол\R.W.A files_homework\HW_task_3_files'
my_files = os.listdir(folder_path)
#print(my_files) #['1.txt', '2.txt', '3.txt']
common_txt_file_list = []
for file_name in my_files:
    with open(f'{folder_path}\{file_name}', 'r', encoding="utf8") as f:
        file_lines = f.readlines()
        #print(file_lines)
        common_txt_file_list.append([str(len(file_lines)), file_name, file_lines])
common_txt_file_list.sort()
pprint(common_txt_file_list)
with open('finish.txt','a',encoding="utf8") as f:
    for list_ in common_txt_file_list:
        for el in list_:
            f.writelines(el)
            f.write('\n')
        f.write('\n')
