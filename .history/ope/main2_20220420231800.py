import os
import shutil

file_names = os.listdir('Sand')

dic_name_list = ['ABC','ARC','AGC',"Others"]
for file_name in file_names:
    print(file_name)
    dic_name, name = file_name.split('-')
    dic_big = ""
    for tmp in dic_name_list:
        dic_big = tmp
        if tmp in dic_name:break
    abcNames = os.listdir('AtCoder/'+dic_big)
    if not dic_name in abcNames:
        os.mkdir("AtCoder/"+dic_big+"/"+dic_name)
    shutil.move('Sand/'+file_name,"AtCoder/"+dic_big+"/"+dic_name+'/'+name)

    print(file_name,dic_name,name)