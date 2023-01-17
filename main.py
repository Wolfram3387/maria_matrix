import sys
from PyQt5 import QtWidgets


def main():
    app = QtWidgets.QApplication(sys.argv)
    from windows import main_window
    main_window.show()
    app.exec_()


if __name__ == '__main__':
    main()
