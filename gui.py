from PyQt5 import QtWidgets, uic
from spotify_api.spotify_api import SpotifyAPI
from alarm import Alarm

class AlarmApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(AlarmApp, self).__init__()
        uic.loadUi('alarm_app.ui', self)
        self.spotify_api = SpotifyAPI()
        self.alarm = Alarm()

        self.login_button.clicked.connect(self.login_to_spotify)
        self.set_alarm_button.clicked.connect(self.set_alarm)

    def login_to_spotify(self):
        self.spotify_api.authenticate()
        playlists = self.spotify_api.get_playlists()
        self.playlist_combo.addItems(playlists)

    def set_alarm(self):
        time = self.time_input.time().toString('HH:mm')
        playlist = self.playlist_combo.currentText()
        self.alarm.set_alarm(time, playlist, self.spotify_api)
