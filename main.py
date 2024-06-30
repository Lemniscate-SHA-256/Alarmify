from PyQt5 import QtWidgets
from gui import AlarmApp
import sys

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = AlarmApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
