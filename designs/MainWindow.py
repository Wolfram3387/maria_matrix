# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\wolfr\PycharmProjects\Maria\designs\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MatrixPacking(object):
    def setupUi(self, MatrixPacking):
        MatrixPacking.setObjectName("MatrixPacking")
        MatrixPacking.resize(492, 318)
        MatrixPacking.setMinimumSize(QtCore.QSize(479, 318))
        MatrixPacking.setMaximumSize(QtCore.QSize(958, 636))
        MatrixPacking.setStyleSheet("")
        self.verticalLayoutWidget = QtWidgets.QWidget(MatrixPacking)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(320, 10, 171, 301))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(10, 0, 10, 0)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_load = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_load.setObjectName("pushButton_load")
        self.verticalLayout.addWidget(self.pushButton_load)
        self.pushButton_find = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_find.setObjectName("pushButton_find")
        self.verticalLayout.addWidget(self.pushButton_find)
        self.pushButton_add = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_add.setObjectName("pushButton_add")
        self.verticalLayout.addWidget(self.pushButton_add)
        self.pushButton_delete = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.verticalLayout.addWidget(self.pushButton_delete)
        self.pushButton_export = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_export.setObjectName("pushButton_export")
        self.verticalLayout.addWidget(self.pushButton_export)
        self.pushButton_author = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_author.setObjectName("pushButton_author")
        self.verticalLayout.addWidget(self.pushButton_author)
        self.tableWidget = QtWidgets.QTableWidget(MatrixPacking)
        self.tableWidget.setGeometry(QtCore.QRect(9, 9, 300, 300))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.retranslateUi(MatrixPacking)
        QtCore.QMetaObject.connectSlotsByName(MatrixPacking)

    def retranslateUi(self, MatrixPacking):
        _translate = QtCore.QCoreApplication.translate
        MatrixPacking.setWindowTitle(_translate("MatrixPacking", "Dialog"))
        self.pushButton_load.setText(_translate("MatrixPacking", "Загрузить матрицу"))
        self.pushButton_find.setText(_translate("MatrixPacking", "Поиск элемента"))
        self.pushButton_add.setText(_translate("MatrixPacking", "Добавление элемента"))
        self.pushButton_delete.setText(_translate("MatrixPacking", "Удаление элемента"))
        self.pushButton_export.setText(_translate("MatrixPacking", "Экспортировать матрицу"))
        self.pushButton_author.setText(_translate("MatrixPacking", "Автор программы"))