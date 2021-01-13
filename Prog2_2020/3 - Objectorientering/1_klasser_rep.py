"""
Klasser

- Hur man definerar klasser
- Hur man använder dem
    - init
    - str

"""


class Profession():
    name = None
    salary = None
    location = None
    title = None

    def __init__(self, name=None, salary=None):
        self.name = name
        self.salary = salary
    
    def promotion(self):
        newsalary = salary *  2
        return newsalary
    
    def go_on_vacation(self, days:int):
        newsalary = salary * 0.8
        return newsalary


class Person():
    name = None
    age = None
    prof = None

    def grow(self):
        self.age+=1

    def __init__(self, name=None, age=None, profname=None, salary=None):
        self.name = name
        self.age = age
        self.prof = Profession(name=profname, salary=salary)

    def __str__(self):
        return self.name + " is " + str(self.age) + " years old. And works as a " + self.prof.name 




class JobListings():
    jobs = []

    def add_job(self, prof:Profession):
        self.jobs.append(prof)
    
    def get_next_job(self):
        return self.jobs.pop(0)




blocketjobb = JobListings()
blocketjobb.add_job(  Profession("Police", "2000000$")  )
blocketjobb.add_job(  Profession("Trafikpolis", "200$")  )

kalle = Person("Kalle", 29, "Teacher", "10000000000$")
print(kalle)
kalle.prof = blocketjobb.get_next_job()
print(kalle)


kalle.grow()
print(kalle)
kalle.grow()
print(kalle)

