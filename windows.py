from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem

import designs
from Matrix import matrix, PackedMatrix


def warning(text, title='Предупреждение', icon=QMessageBox.Warning, button=QMessageBox.Ok):
    msg = QMessageBox()
    msg.setText(text)
    msg.setIcon(icon)
    msg.setWindowTitle(title)
    msg.setStandardButtons(button)
    msg.exec_()


class MainWindow(QtWidgets.QMainWindow, designs.MainWindow.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.delete_window = None
        self.add_window = None
        self.find_window = None

        self.pushButton_load.clicked.connect(self.btn_load_clicked)
        self.pushButton_find.clicked.connect(self.btn_find_clicked)
        self.pushButton_add.clicked.connect(self.btn_add_clicked)
        self.pushButton_delete.clicked.connect(self.btn_delete_clicked)
        self.pushButton_export.clicked.connect(self.btn_export_clicked)
        self.pushButton_author.clicked.connect(self.btn_author_clicked)

    def btn_load_clicked(self):
        file, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            'Open File',
            './',
            'txt Files (*.txt);;Text Files (*.txt)'
        )
        if file:
            try:
                matrix.read_matrix_from_file(file)
            except (FileNotFoundError, ValueError, NameError, NotImplementedError) as error:
                warning(text=error.args[0])
                return
            self.update_table(matrix)

    def update_table(self, matrix: PackedMatrix):
        array = matrix.unpack_matrix()
        self.tableWidget.setColumnCount(matrix.rank)
        self.tableWidget.setRowCount(matrix.rank)
        self.tableWidget.setHorizontalHeaderLabels(list(map(str, range(1, matrix.rank + 1))))
        self.tableWidget.setVerticalHeaderLabels(list(map(str, range(1, matrix.rank + 1))))
        cell_size = self.tableWidget.geometry().width() // matrix.rank
        self.tableWidget.setColumnWidth(cell_size, cell_size)
        self.tableWidget.setRowHeight(cell_size, cell_size)
        for i in range(matrix.rank):
            for j in range(matrix.rank):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(array[i][j])))

        self.tableWidget.resizeColumnsToContents()

    def btn_find_clicked(self):
        if not matrix.packed_matrix:
            warning(text='Матрица не загружена. Загрузите матрицу')
            return
        self.find_window = FindWindow()
        self.find_window.show()

    def btn_add_clicked(self):
        if not matrix.packed_matrix:
            warning(text='Матрица не загружена. Загрузите матрицу')
            return
        self.add_window = AddWindow()
        self.add_window.show()

    def btn_delete_clicked(self):
        if not matrix.packed_matrix:
            warning(text='Матрица не загружена. Загрузите матрицу')
            return
        self.delete_window = DeleteWindow()
        self.delete_window.show()

    def btn_export_clicked(self):
        if not matrix.packed_matrix:
            warning(text='Матрица не загружена. Загрузите матрицу')
            return

        # записываем данные упакованной матрицы в файл, выбранный пользователем
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, 'Open file', '/packed_matrix', '.txt')
        if file_path:
            matrix.export_packed_matrix_to_file(file_path=file_path)

    @staticmethod
    def btn_author_clicked():
        warning(text='Автор программы: Мария', title='Авторство', icon=QMessageBox.Information)


class FindWindow(QtWidgets.QMainWindow, designs.FindWindow.Ui_FindWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_find.clicked.connect(self.btn_find_clicked)

    def btn_find_clicked(self):
        row = self.lineEdit_row.text()
        column = self.lineEdit_column.text()

        # TODO валидация данных

        # TODO найти элемент a[row, column] в матрице
        element = matrix.find_element_in_packed_matrix(row, column)

        warning(text=f'A[{row}][{column}] = {element}', title='Поиск элемента', icon=QMessageBox.Information)


class AddWindow(QtWidgets.QMainWindow, designs.AddWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_add.clicked.connect(self.btn_add_clicked)

    def btn_add_clicked(self):
        row = self.lineEdit_row.text()
        column = self.lineEdit_column.text()
        element = self.lineEdit_element.text()

        # TODO валидация данных

        # добавить element в матрицу
        matrix.add_element_to_packed_matrix(row, column, element)

        # TODO обновить TableWidget


class DeleteWindow(QtWidgets.QMainWindow, designs.DeleteWindow.Ui_DeleteWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_delete.clicked.connect(self.btn_delete_clicked)

    def btn_delete_clicked(self):
        row = self.lineEdit_row.text()
        column = self.lineEdit_column.text()

        # TODO валидация данных

        matrix.remove_element_from_packed_matrix(row, column)

        # TODO обновить TableWidget
