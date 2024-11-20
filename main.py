#!/usr/bin/env python
#
# Fetch metadata from a YouTube playlist using the YouTube Data API.
#
# Author: klairvoyage
# Repository: https://github.com/klairvoyance/yt-metadata
#
"""
Fetch and save metadata of all videos in a YouTube playlist.

Usage:
    $ python main.py <playlist_id>

Example:
    $ python main.py PLbpi6ZahtOH41pTffYAcobNPYveptjT5K

Output:
    A CSV file named after the playlist title containing the following metadata:
        - Duration
        - Filename (if available)
        - Description
        - video-ID
        - Published Date (see https://developers.google.com/youtube/v3/docs/videos#snippet.publishedAt for details)
        - Title
        - Comment count
"""

import re
import argparse
import pandas as pd
from auth import authenticate_youtube
from fetch import fetch_playlist_videos, fetch_video_details, fetch_playlist_title

def main():
    # Sets up argument parser
    parser = argparse.ArgumentParser(description="Allows to fetch YouTube playlist.")
    parser.add_argument("playlist_id", help="The ID of the YouTube playlist (everything after '?list=' in the URL)")
    args = parser.parse_args()

    # Extract playlist-ID from arguments
    playlist_id = args.playlist_id

    # Authenticates & builds the YouTube API service
    youtube = authenticate_youtube()

    # Fetches videos from provided playlist
    videos = fetch_playlist_videos(youtube, playlist_id)
    print("Fetching videos, please wait...")

    # Collects detailed metadata for each video upload in provided playlist
    video_data = []
    for video in videos:
        details = fetch_video_details(youtube, video["video_id"])
        if details:
            video_data.append(details)

    # Saves data to CSV
    playlist_title = re.sub(r'[\\/:*?"<>|]', "_", fetch_playlist_title(youtube, playlist_id))
    output_file = f"{playlist_title}.csv"
    df = pd.DataFrame(video_data)
    df.to_csv(output_file, index=False)

    print(f"Video details saved to {output_file}!")

if __name__ == "__main__":
    main()
