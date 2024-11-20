import isodate
from datetime import datetime
from utils import parse_duration

def fetch_playlist_videos(youtube, playlist_id):
    videos = []
    next_page_token = None

    while True:
        request = youtube.playlistItems().list(
            part="snippet,contentDetails",
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page_token
        )
        response = request.execute()

        for item in response.get("items", []):
            video_id = item["contentDetails"]["videoId"]
            title = item["snippet"]["title"]
            videos.append({"video_id": video_id, "title": title})

        next_page_token = response.get("nextPageToken")
        if not next_page_token:
            break

    return videos

def fetch_video_details(youtube, video_id):
    try:
        request = youtube.videos().list(
            part="snippet,contentDetails,fileDetails,statistics",
            id=video_id
        )
        response = request.execute()

        if not response["items"]:
            print(f"No details found for video ID: {video_id}")
            return None

        video = response["items"][0]
        snippet = video.get("snippet", {})
        content_details = video.get("contentDetails", {})
        file_details = video.get("fileDetails", {})
        statistics = video.get("statistics", {})

        publishedAt = snippet.get("publishedAt", "Unknown")
        publishedAt_UTC = (
            datetime.strptime(publishedAt, "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d %H:%M:%S UTC")
            if publishedAt != "Unknown"
            else "Unknown"
        )

        return {
            "Duration": parse_duration(content_details.get("duration", "PT0S")),
            "Filename": file_details.get("fileName", "Unknown"),
            "Description": snippet.get("description", "No description"),
            "video-ID": video_id,
            "Published Date": publishedAt_UTC,
            "Title": snippet.get("title", "Unknown"),
            "Comments": statistics.get("commentCount", -1),
        }
    except Exception as e:
        print(f"Error fetching details for video ID: {video_id} - {e}")
        return None

def fetch_playlist_title(youtube, playlist_id):
    try:
        request = youtube.playlists().list(
            part="snippet",
            id=playlist_id
        )
        response = request.execute()
        playlist = response["items"][0]
        return playlist["snippet"]["title"]
    except Exception as e:
        print(f"Error fetching playlist title: {e}")
        return "unknown_playlist"
