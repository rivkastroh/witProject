
class Commit:
    def __init__(self,creation_date,description,hashcode):
        self.creation_date =creation_date
        self.description = description
        self.hashcode = hashcode
    def __str__(self):
        return "hashcode: "+str(self.hashcode)+"  description: "+str(self.creation_date)+" creation_date: "+str(self.creation_date)
    #ממירה את האוביקט למילון
    def to_dict(self):
        return{
            'creation_date':self.creation_date,
            'description':self.description,
            'hashcode':self.hashcode
        }
    #ממירה את המילון לאוביקט
    @classmethod
    def to_commit(cls,data):
        return cls(creation_date=data['creation_date'],description=data['description'],hashcode=data['hashcode'])
