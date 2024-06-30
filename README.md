# Alarmify

![Alarmify Logo](https://github.com/Lemniscate-SHA-256/Alarmify/blob/main/Logo%20First%20Draft.png)

**Alarmify** is an open-source Spotify Playlist Alarm GUI app for Linux that allows you to wake up to your favorite Spotify playlists.

## Features
- Spotify Authentication
- Select and play Spotify playlists as alarms
- User-friendly GUI built with PyQt5
- Schedule alarms to play at specific times

## Screenshots
![Screenshot1](https://your-screenshot-url.com/screenshot1.png)
![Screenshot2](https://your-screenshot-url.com/screenshot2.png)

## Installation

### Prerequisites
- Python 3.x
- Spotify Developer Account (for API credentials)

### Setup
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/alarmify.git
    cd alarmify
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up Spotify API credentials:
    - Create a `.env` file in the root directory and add your credentials:
      ```plaintext
      SPOTIPY_CLIENT_ID='your_client_id'
      SPOTIPY_CLIENT_SECRET='your_client_secret'
      SPOTIPY_REDIRECT_URI='your_redirect_uri'
      ```

4. Run the application:
    ```bash
    python main.py
    ```

## Usage
1. Launch the application.
2. Log in to Spotify.
3. Select the time and playlist for your alarm.
4. Set the alarm.

## Contributing
We welcome contributions! Please read our [Contributing Guidelines](CONTRIBUTING.md) for more details.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [Spotify API](https://developer.spotify.com/documentation/web-api/)
- [PyQt5](https://pypi.org/project/PyQt5/)
- [Spotipy](https://spotipy.readthedocs.io/en/2.16.1/)

---

**Author**: Lemniscate-SHA-256

[![GitHub followers](https://img.shields.io/github/followers/Lemniscate-SHA-256.svg?style=social&label=Follow)](https://github.com/Lemniscate-SHA-256)
