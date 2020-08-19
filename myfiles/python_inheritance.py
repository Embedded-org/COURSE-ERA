print("Person classs with constructor*_______")
class Person:
  def __init__(self, fname, lname):
    print("parent class called")
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

print("Student classs with no constructor*_______")
class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()

print("Student classs with constructor*_______")
class Student(Person):
    def __init__(self, fname, lname,myindex):
        #Person.__init__(self, fname, lname)
        #Person.__init__(self, fname, lname)
        super().__init__(fname, lname)
        super().__init__(fname, lname)
        self.mynumber=myindex
        print("myindex is",self.mynumber)

x = Student("bhai", "jee",4)
x.printname()

print("Student_child with no constructor*_______")

class Student_child(Student):
    pass


x = Student_child("raja", "sahab",4)
x.printname()


print("my simple class*_______")

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is ",abc.name)

p1 = Person("John", 36)
p1.myfunc()
