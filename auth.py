import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]
CLIENT_SECRETS_FILE = "client_secret.json"

def authenticate_youtube():
    if not os.path.exists(CLIENT_SECRETS_FILE):
        raise FileNotFoundError(f"OAuth 2.0 file '{CLIENT_SECRETS_FILE}' not found.")
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_local_server(port=8080)
    youtube = build("youtube", "v3", credentials=credentials)
    return youtube
