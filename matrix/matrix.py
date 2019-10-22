class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.good_list = []
        self.column_list = []
        self.create_list()

    def create_list(self):
        for line in self.matrix_string.split("\n"):
            self.temp_list = []
            for elem in line.split():
                self.temp_list.append(int(elem))
            self.good_list.append(self.temp_list)

    def row(self, index):
        return self.good_list[index-1]

    def column(self, index):
        for i in self.good_list:
            self.column_list.append(i[index-1])
        return self.column_list