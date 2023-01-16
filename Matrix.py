import os


class PackedMatrix:

    ...

    def __init__(self):
        """Initialize the packed matrix with an optional initial matrix."""
        self.packed_matrix = []
        self.rank = 0

    def pack_matrix(self, matrix):
        """Packs the matrix by storing only the non-zero elements and their positions."""
        for col in range(1, self.rank+1):
            self.packed_matrix.append((0, col))
            for row in range(1, self.rank+1):
                if matrix[row-1][col-1] != 0:
                    self.packed_matrix.append((row, matrix[row-1][col-1]))
        self.packed_matrix.append((0, 0))

    def add_element_to_packed_matrix(self, row, column, element):
        """Adds an element to the packed matrix at the specified position."""
        i_start = self.packed_matrix.index((0, column))
        i_end = len(self.packed_matrix) - 1 if column == self.rank else self.packed_matrix.index((0, column+1))
        while self.packed_matrix[i_start][0] < row:
            i_start += 1
            if i_start == i_end:
                break
        if self.packed_matrix[i_start][0] == row:
            del self.packed_matrix[i_start]
        self.packed_matrix.insert(i_start, (row, element))

    def remove_element_from_packed_matrix(self, row, column):
        """Removes an element from the packed matrix at the specified position."""
        delete_column = False
        for i, (r, c) in enumerate(self.packed_matrix):
            if r == 0 and c == column:
                delete_column = True
            if r == row and delete_column:
                del self.packed_matrix[i]
                break

    def find_element_in_packed_matrix(self, row, column):
        """Finds an element in the packed matrix and returns its position."""
        find_column = False
        for i, (r, c) in enumerate(self.packed_matrix):
            if r == 0 and c == column:
                find_column = True
            elif r == 0 and find_column:
                return 0
            if r == row and find_column:
                return self.packed_matrix[i][1]

    def export_packed_matrix_to_file(self, file_path):
        """Exports the packed matrix to a text file."""
        with open(file_path, 'w') as f:
            f.write(f'{self.packed_matrix}')

    def unpack_matrix(self):
        """Converts packed matrix back to a regular matrix"""

        matrix = [[0 for _ in range(self.rank)] for _ in range(self.rank)]
        for i, (r, c) in enumerate(self.packed_matrix):
            if r == 0 and c == 0:
                break
            elif r == 0:
                current_column = c
            else:
                matrix[r-1][current_column-1] = c
        return matrix

    def read_matrix_from_file(self, file_path):
        """Reads a square matrix from a text file"""
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"Файл не найден: {file_path}")

        if not file_path.endswith('.txt'):
            raise NameError(f'Файл должен быть с расширением .txt')

        with open(file_path) as file:
            array = file.readlines()
            if not array:
                raise NotImplementedError('Файл не должен быть пустой')

        matrix = self._read_matrix_from_array(array)
        self.pack_matrix(matrix)

    def _read_matrix_from_array(self, strings_array):

        self.rank = len(strings_array)
        matrix = [[0 for _ in range(self.rank)] for _ in range(self.rank)]
        for i in range(self.rank):
            line = strings_array[i].split(';')
            if len(line) != self.rank:
                raise ValueError("Матрица не квадратная, проверьте файл.")
            for j in range(self.rank):
                try:
                    int(line[j])
                except ValueError:
                    raise ValueError(f"Некоррекнтный символ '{line[j]}' найден в строке {i+1}, проверьте файл.")
                matrix[i][j] = int(line[j])
        return matrix


matrix = PackedMatrix()
