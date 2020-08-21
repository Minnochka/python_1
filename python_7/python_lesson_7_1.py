class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(' '.join([str(j) for j in i]) for i in self.matrix)

    def __add__(self, other):
        sum_m = [] 
        if len(self.matrix) == len(other.matrix) and len(sel.matrix[0]) == len(other.matrix[0]):
            for i_1, i_2 in zip(self.matrix, other.matrix):
                l = []
                for j_1, j_2 in zip(i_1, i_2):
                    l.append(j_1 + j_2)
                sum_m.append(l)
            return Matrix(sum_m)
        else:
            return "Размерности матриц не совпадают"

                
m_1 = Matrix([[2, 3], [4, 5], [30, 40]])
print('----------\n')
print(m_1)
m_2 = Matrix([[10, 20], [30, 40]])
print('----------\n')
print(m_2)
s_m = m_1 + m_2
print('----------\n')
print(s_m)
