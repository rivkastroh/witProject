import os
import shutil
import filecmp
import json

    #לשים לב שיש מימוש למקרי קצה כשמפעילים מטודטות אלו
def is_exist(name_folder_or_file, path):
    return  os.path.exists(os.path.join(path,name_folder_or_file))

def current_path():
    return os.getcwd()

def join_path(path1,path2):
    return os.path.join(path1,path2)

def create_folder(name_folder, path):
    os.mkdir(os.path.join(path,name_folder))

def is_wit_folder(names):
    return [name for name in names if name == ".wit"]
#without ignore
def add_files(path1,path2):
    shutil.copytree(path1, path2, ignore=is_wit_folder, dirs_exist_ok=True)

def copy_file(source_path, destination_path):
    shutil.copy(source_path,destination_path)

def is_equals(file1, file2):
    return filecmp.cmp(file1,file2)

def is_empty(path):
    return  len(os.listdir(path))==0

def save_to_json(obj, filename):
    #מוחק את הקודם וכותב מחדש
    with open(filename, 'w') as json_file:
        json_file.truncate(0)
    with open(filename, 'w') as json_file:
        json.dump(obj.to_dict(), json_file)

def load_from_json(filename):
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
        return data
