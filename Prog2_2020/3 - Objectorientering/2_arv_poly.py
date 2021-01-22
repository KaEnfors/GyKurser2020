


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


class Employee(Person):
    working_hours :int
    phone : str

    def go_on_vacation(self):
        pass

    def fire(self):
        print("Bye!")


class Teacher(Employee):
    cofefe : bool
    
    def teach(self):
        pass

class Student(Person):
    courses : list

    def bring_csn():
        pass


class Admin(Employee):
    keys : list

    def remove_csn(student : Student):
        pass


class Course():
    students : list
    teachers : list


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
