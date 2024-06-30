from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QTimeEdit, QComboBox
from PyQt5.uic import loadUi
import sys

class AlarmApp(QMainWindow):
    def __init__(self):
        super(AlarmApp, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Spotify Playlist Alarm')

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.login_button = QPushButton('Login to Spotify', self)
        self.layout.addWidget(self.login_button)

        self.time_input = QTimeEdit(self)
        self.time_input.setDisplayFormat('HH:mm')
        self.layout.addWidget(self.time_input)

        self.playlist_combo = QComboBox(self)
        self.layout.addWidget(self.playlist_combo)

        self.set_alarm_button = QPushButton('Set Alarm', self)
        self.layout.addWidget(self.set_alarm_button)

        self.setLayout(self.layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AlarmApp()
    window.show()
    sys.exit(app.exec_())
