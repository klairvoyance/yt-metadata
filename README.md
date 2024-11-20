# yt-metadata

A command-line tool to fetch metadata using the YouTube Data API.

## Current Features

- Fetches video details such as title, duration, and filename from multiple videos in a playlist.
- Saves metadata as a CSV file for easy analysis.
- [[Intended to expand functionalities]](https://github.com/youtube/api-samples/tree/master/python)

## Prerequisites

1. **Python 3.6 or higher**: Verify your Python version
   ```bash
   python --version
   ```
2. **YouTube Data API Credentials** (free service):
   - Create a `client_secret.json` file by following the [YouTube API Guide](https://developers.google.com/youtube/registering_an_application).
   - For a detailed setup guide, refer to the [Setup section](https://github.com/klairvoyance/yt-metadata/blob/master/README.md#Setup)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/klairvoyance/yt-metadata.git
   ```
2. Navigate to the project directory:
   ```bash
   cd yt-metadata
   ```
3. Install dependencies from the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

## Docker Usage (Optional)

You can also run this tool via Docker:

1. Build the Docker image:
   ```bash
   docker build -t yt-metadata .
   ```
2. Run the Docker container:
   ```bash
   docker run yt-metadata <playlist_id>
   ```

## Setup
- Go to the Google Developer [Console](https://console.developers.google.com).
- ... (TODO: trailing-'/')

## Usage

### 1. Authenticate
Ensure your `client_secret.json` is in the project directory. You will be prompted to authenticate each time you run the script!

### 2. Fetch Playlist Metadata
Run the script using:
```bash
python main.py <playlist_id>
```
Replace `<playlist_id>` with the ID of the YouTube playlist.

### Example:
```bash
python main.py PLbpi6ZahtOH41pTffYAcobNPYveptjT5K
```
This will generate a CSV file named after the playlist title containing metadata for each video.

## Notes

- Ensure the `client_secret.json` file is kept secure and is not uploaded to public repositories.
- The CSV file will be saved in the current working directory.

## License

This project is licensed under the [GNU General Public License v3.0](https://github.com/klairvoyance/yt-metadata/blob/master/LICENSE). Feel free to use, modify, and distribute the code for personal and commercial purposes.
