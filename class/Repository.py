from datetime import  date

import Files
from Commit import Commit


class Repository:
    def __init__(self,flag=True,hashcode=0):
        self.project_path = Files.current_path()
        self.commits_dict = {}
        self.hashcode = hashcode
        if flag:#בדיקה האם מאגר משוחזר או חדש
            if Files.is_exist('.wit',Files.current_path()):
                raise Exception('This database already exists')
            Files.create_folder('.wit',self.project_path)
            Files.create_folder('staging',Files.join_path(self.project_path,'.wit'))
            Files.create_folder('commits',Files.join_path(self.project_path,'.wit'))

    def add_commit(self, commit_description):
        self.commits_dict[self.hashcode] = Commit(date.today(), commit_description, self.hashcode)
        self.hashcode+=1

    def to_dict(self):
        return{
            'project_path':self.project_path,
            'commits_dict':{hashcode:commit.to_dict() for hashcode,commit in self.commits_dict.items()},
            'hashcode':self.hashcode
        }
    @classmethod
    def to_repository(cls,data):
        rep= cls(False,data['hashcode'])
        for hashcode,commit_data in data['commits_dict'].items():
            commit = Commit.to_commit(commit_data)
            rep.commits_dict[hashcode]=commit

    def wit_add(self):
        Files.add_files(self.project_path,Files.join_path(self.project_path,'.wit\staging'))

    def wit_add(self,file):
        Files.copy_file(Files.join_path(self.project_path,file),Files.join_path(self.project_path,'.wit\staging'))

    def wit_commit(self,message):
        self.add_commit(message)
        Files.create_folder(self.hashcode-1,Files.join_path(self.project_path,'.wit\commits'))
        Files.add_files(Files.join_path(self.project_path,'.wit\staging'),Files.join_path(Files.join_path(self.project_path,'.wit\commits'),str(self.hashcode-1)))

#לשנות שידפיס לcli ולא לקונסול
    def wit_log(self):
        for c in self.commits_dict:
            print(c)

    def wit_status(self):
        if Files.is_empty(Files.join_path(self.project_path,'.wit\staging')):
            print('No changes')
        pass
        #המשך אחרי שנקבל תשובה מהמורה

    def wit_checkout(self,commit_id):
        pass



#מסעעמים בממשק משתמש
    # def wit_init(self):
    #     if Files.is_exist('.wit',Files.current_path()):
    #         raise Exception('This database already exists')


#https://realpython.com/python-click/