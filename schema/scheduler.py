

class Schedule():
    available_schedule: dict

    def __init__(self):
        TIME = {
            'mån' = []
            'tis' = []
            'ons' = []
            'tor' = []
            'fre' = []
        }
        
        for i in range(12):
            TIME['mån'].append(True)
            TIME['tis'].append(True)
            TIME['ons'].append(True)
            TIME['tor'].append(True)
            TIME['fre'].append(True)
        self.available_schedule = TIME

    def is_available(self, day:str, start:int, end:int):
        for i in range(start:end):
            if not self.available_schedule[day][i]:
                return False
        return True
    
    def place(self, day:str, start:int, end:int):
        for i in range(start:end):
            self.available_schedule[day][i] = True
        return True

class Block():
    name : str
    day : str
    start : int
    end : int


    def __init__(self, courseName:str, teach, group, halftime=False, big=False):
        self.teacher = teach
        self.group = group
        self.halftime = halftime
        self.big = big

    def build(self):
        # Find available times
        # Assign to teacher and group
        # Save block, or fail
        pass

class Teacher(Schedule):
    pass

class Group(Schedule):
    pass

class Course(Schedule):
    pass
