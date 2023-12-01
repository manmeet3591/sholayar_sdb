import streamlit as st
from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.discovery import build
import os

# Use Streamlit's secrets management
CLIENT_ID = st.secrets["GOOGLE_CLIENT_ID"]
CLIENT_SECRET = st.secrets["GOOGLE_CLIENT_SECRET"]
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
TOKEN_FILE = 'token.json'  # File to store the user's access and refresh tokens

def authenticate_user():
    credentials = None

    # Check if token file exists and has valid credentials
    if os.path.exists(TOKEN_FILE):
        credentials = google.auth.credentials.Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

    # If there are no valid credentials, go through the authorization flow
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secrets.json', SCOPES)
            credentials = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open(TOKEN_FILE, 'w') as token:
            token.write(credentials.to_json())

    drive_service = build('drive', 'v3', credentials=credentials)
    return drive_service

def list_drive_files(drive_service):
    # Call the Drive v3 API
    results = drive_service.files().list(
        pageSize=10, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        st.write('No files found.')
    else:
        st.write('Files:')
        for item in items:
            st.write(u'{0} ({1})'.format(item['name'], item['id']))

def main():
    st.title("Google Drive Integration in Streamlit")

    drive_service = authenticate_user()

    if drive_service:
        list_drive_files(drive_service)

if __name__ == "__main__":
    main()
