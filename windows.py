from typing import Type

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QWidget, QGridLayout

import designs
from Matrix import matrix, PackedMatrix


class MainWindow(QtWidgets.QMainWindow, designs.MainWindow.Ui_MatrixPacking):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.adjustSize()

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
            matrix.read_matrix_from_file(file)
            # TODO обновить TableWidget
            self.update_table(matrix)
    def update_table(self, matrix: Type[PackedMatrix]):
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
        self.find_window = FindWindow()
        self.find_window.show()

    def btn_add_clicked(self):
        self.add_window = AddWindow()
        self.add_window.show()

    def btn_delete_clicked(self):
        self.delete_window = DeleteWindow()
        self.delete_window.show()

    def btn_export_clicked(self):
        # записываем данные упакованной матрицы в файл, выбранный пользователем
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, 'Open file', '/packed_matrix', '.txt')
        if file_path:
            matrix.export_packed_matrix_to_file(file_path=file_path)


    @staticmethod
    def btn_author_clicked():
        about_window = QMessageBox()
        about_window.setText('Автор программы: Мария')
        about_window.setIcon(QMessageBox.Information)
        about_window.setWindowTitle('Авторство')
        about_window.setStandardButtons(QMessageBox.Ok)
        about_window.exec_()


class FindWindow(QtWidgets.QMainWindow, designs.FindWindow.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_find.clicked.connect(self.btn_find_clicked)

    def btn_find_clicked(self):
        row = self.lineEdit_row.text()
        column = self.lineEdit_2.text()

        # TODO валидация данных

        # TODO найти элемент a[row, column] в матрице
        element = matrix.find_element_in_packed_matrix(row, column)

        # показать окно с этим элементом
        element_window = QMessageBox()
        element_window.setText(f'A[{row}][{column}] = {element}')
        element_window.setIcon(QMessageBox.Information)
        element_window.setWindowTitle('Найти элемент')
        element_window.setStandardButtons(QMessageBox.Ok)
        element_window.exec_()


class AddWindow(QtWidgets.QMainWindow, designs.AddWindow.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_add.clicked.connect(self.btn_add_clicked)

    def btn_add_clicked(self):
        row = self.lineEdit_row.toPlainText()
        column = self.lineEdit_column.toPlainText()
        element = self.lineEdit_element.toPlainText()

        # TODO валидация данных

        # добавить element в матрицу
        matrix.add_element_to_packed_matrix(row, column, element)

        # TODO обновить TableView


class DeleteWindow(QtWidgets.QMainWindow, designs.DeleteWindow.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_delete.clicked.connect(self.btn_delete_clicked)

    def btn_delete_clicked(self):
        row = self.lineEdit_row.toPlainText()
        column = self.lineEdit.toPlainText()

        # TODO валидация данных

        # TODO удалить элемент a[row, column] из матрицы
        matrix.remove_element_from_packed_matrix(row, column)

        # TODO обновить TableView
