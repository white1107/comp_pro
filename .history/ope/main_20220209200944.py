import os
import shutil

file_names = os.listdir('Sand')

dic_name_list = ['ABC','ARC','AGC',"Others"]
for file_name in file_names:
    dic_name, name = file_name.split('-')
    abcNames = os.listdir('AtCoder/')
    if not dic_name in abcNames:
        os.mkdir('AtCoder/'+dic_name)
    for tmp in dic_name_list:
        if tmp in dic_name:break
    shutil.move('Sand/'+file_name,"AtCoder/"+dic_name+'/'+name)

    print(file_name,dic_name,name)