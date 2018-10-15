class Student(object):
    def __init__(self,name,gender):
        self.__name=name
        self.__gender=gender
        #print('Hello')
    def Greet(self):
        print("Welcome! %s : %s" %(self.__gender,self.__name),)
    def get_grade(self):
        if self.__gender == 'Female':
            print( 'hentai')
        else :
            print('Normal')

Lisa = Student('Lisa','Female')
Jack = Student('Jack','Male')
Lisa.Greet()
Jack.Greet()
Lisa.get_grade()
Jack.get_grade()
Lisa.__name()