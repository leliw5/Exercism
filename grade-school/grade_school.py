class School(object):
    def __init__(self):
        self.students = {}

    def add_student(self, name: str, grade: int) -> None:
        self.students[name] = grade

    def roster(self) -> list:
        roster_list = []
        for name in sorted(self.students, key=lambda k: (self.students[k], k)):
            roster_list.append(name)
        return roster_list

    def grade(self, grade: int) -> list:
        grade_list = []
        for n, g in self.students.items():
            if g == grade:
                grade_list.append(n)
        return sorted(grade_list)
