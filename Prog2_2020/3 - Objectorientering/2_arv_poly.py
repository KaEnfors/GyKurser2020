


class ScheduleBlock():
    pass

class Schedule():
    mon : list

    pass


class Person():
    name : str
    schedule : Schedule

    def say_hi(self):
        print("Hi!")


class Employee():
    working_hours :int
    phone : str

    def go_on_vacation(self):
        pass

    def fire(self):
        print("Bye!")

        unregister()
        taxes()
        akassa()
        




class Teacher(Person, Employee):
    cofefe : bool
    
    def teach(self):
        pass

    def go_on_vacation(self):

        print("NO!")


class Student(Person):
    courses : list

    def bring_csn():
        pass


class Admin(Employee):
    keys : list

    def remove_csn(student : Student):
        pass

    def fire(self):
        super().fire()
        self.keys = None



class Course():
    students : list
    teacher : Teacher
    


class Organization():
    employees = list

    def print_employees(self):
        for e in self.employees:
            print(e.go_on_vacation())


    

employees = []
employees.append(Admin())
employees.append(Teacher())
employees.append(Admin())

people = []
for i in range(100):
    people.append(Student())

for employee in employees:
    employee.fire()

for p in people:
    p.say_hi()    
