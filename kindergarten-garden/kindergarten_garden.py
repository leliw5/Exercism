class Garden(object):
    def __init__(self, diagram, students):
        self.diagram = diagram
        self.students = students
        self.students = "Alice, Bob, Charlie, David, Eve, Fred, Ginny, Harriet, Ileana, Joseph, Kincaid, Larry".split()
        self.legend = {"G": "Grass", "C": "Clover", "R": "Radishes", "V": "Violets"}

    def plants(self, student):
        plots = self.diagram.split()
