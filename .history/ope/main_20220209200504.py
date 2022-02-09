import os
file_names = os.listdir('Sand')


for file_name in file_names:
    dic_name, name = file_name.split('-')
    print(file_name,dic_name,name)