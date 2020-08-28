
from scheduler import Block, Teacher, Course, Group

JOBB_QUEUE = []
TEACHERS = {}
GROUPS = {}

def run():
    pass

def setup():
    global JOBB_QUEUE, TEACHERS, GROUPS
    TEACHERS['Karl Enfors'] = Teacher()
    GROUPS['TEK19'] = Group()
    JOBB_QUEUE.append(Block('Prog1', TEACHERS['Karl Enfors'], GROUPS['TEK19']))
    JOBB_QUEUE.append(Block('Pebb1', TEACHERS['Karl Enfors'], GROUPS['TEK19']))


def save():
    pass

def load():
    pass

if __name__ == "__main__":
    print("Scheduler...")


