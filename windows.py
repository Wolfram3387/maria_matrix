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
        self.table_is_filled = False

        self.pushButton_load.clicked.connect(self.btn_load_clicked)
        self.pushButton_find.clicked.connect(self.btn_find_clicked)
        self.pushButton_add.clicked.connect(self.btn_add_clicked)
        self.pushButton_delete.clicked.connect(self.btn_delete_clicked)
        self.pushButton_export.clicked.connect(self.btn_export_clicked)
        self.pushButton_author.clicked.connect(self.btn_author_clicked)
        self.tableWidget.cellChanged.connect(self.cell_changed)

    def resizeEvent(self, event):
        if matrix.packed_matrix:
            self.update_table(matrix)

    def cell_changed(self):
        if not self.table_is_filled:
            return
        row = int(self.tableWidget.currentRow()) + 1
        column = int(self.tableWidget.currentColumn()) + 1
        if row == 0 and column == 0:  # этот условие выхода необходимо для изменения окна без ошибок
            return
        element = self.tableWidget.item(row-1, column-1).text()
        try:
            element = int(element)
        except ValueError:
            self.tableWidget.setItem(row-1, column-1, QTableWidgetItem('0'))
            return
        if element:
            matrix.add_element_to_packed_matrix(row, column, element)

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
        for i in range(matrix.rank):
            for j in range(matrix.rank):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(array[i][j])))
        column_size = self.tableWidget.width() // self.tableWidget.columnCount() - 5
        row_size = self.tableWidget.height() // self.tableWidget.rowCount() - 5
        for i in range(matrix.rank):
            self.tableWidget.setColumnWidth(i, column_size)
            self.tableWidget.setRowHeight(i, row_size)
        self.table_is_filled = True

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
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, 'Open file', 'packed_matrix.txt', '.txt')
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
        try:
            row = int(self.lineEdit_row.text())
            column = int(self.lineEdit_column.text())
            assert 1 <= row <= matrix.rank and 1 <= column <= matrix.rank
        except ValueError:
            warning(text='Введите число', icon=QMessageBox.Warning)
            return
        except AssertionError:
            warning(text='Некорректный индекс для столбца или строки', icon=QMessageBox.Warning)
            return

        element = matrix.find_element_in_packed_matrix(row, column)
        warning(text=f'A[{row}][{column}] = {element}', title='Поиск элемента', icon=QMessageBox.Information)


class AddWindow(QtWidgets.QMainWindow, designs.AddWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_add.clicked.connect(self.btn_add_clicked)

    def btn_add_clicked(self):
        try:
            row = int(self.lineEdit_row.text())
            column = int(self.lineEdit_column.text())
            element = int(self.lineEdit_element.text())
            assert 1 <= row <= matrix.rank and 1 <= column <= matrix.rank
        except ValueError:
            warning(text='Введите число', icon=QMessageBox.Warning)
            return
        except AssertionError:
            warning(text='Некорректный индекс для столбца или строки', icon=QMessageBox.Warning)
            return

        matrix.add_element_to_packed_matrix(row, column, element)
        main_window.update_table(matrix)
        self.close()


class DeleteWindow(QtWidgets.QMainWindow, designs.DeleteWindow.Ui_DeleteWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_delete.clicked.connect(self.btn_delete_clicked)

    def btn_delete_clicked(self):
        try:
            row = int(self.lineEdit_row.text())
            column = int(self.lineEdit_column.text())
            assert 1 <= row <= matrix.rank and 1 <= column <= matrix.rank
        except ValueError:
            warning(text='Введите число', icon=QMessageBox.Warning)
            return
        except AssertionError:
            warning(text='Некорректный индекс для столбца или строки', icon=QMessageBox.Warning)
            return

        matrix.remove_element_from_packed_matrix(row, column)
        main_window.update_table(matrix)
        self.close()


main_window = MainWindow()
