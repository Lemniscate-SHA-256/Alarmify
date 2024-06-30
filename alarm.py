import schedule
import time
import threading

class Alarm:
    def set_alarm(self, time_str, playlist, spotify_api):
        schedule.every().day.at(time_str).do(self.play_playlist, playlist, spotify_api)

        def run_scheduler():
            while True:
                schedule.run_pending()
                time.sleep(1)

        thread = threading.Thread(target=run_scheduler)
        thread.start()

    def play_playlist(self, playlist, spotify_api):
        spotify_api.play_playlist(playlist)
