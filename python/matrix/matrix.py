class Matrix(object):
    def __init__(self, matrix_string):
        self.a=matrix_string.split('\n')

    def row(self, index):
        return([int(i) for i in self.a[index-1].split()])

    def column(self, index):
        rows=len(self.a)
        column_matrix=[]
        for r in range(rows):
            int_row=self.row(r+1)
            column_matrix.append(int_row[index-1])
        return(column_matrix)

