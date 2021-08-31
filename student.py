class Student:
    def __init__(self,id,name,testscore):
        self.name=name
        self.id=id
        self.testscore=testscore
    def display(self):
        print(self.name,self.id,self.testscore)