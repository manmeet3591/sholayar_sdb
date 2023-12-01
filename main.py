import streamlit as st
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
import google.auth
import os

# Use Streamlit's secrets management
CLIENT_ID = st.secrets["GOOGLE_CLIENT_ID"]
CLIENT_SECRET = st.secrets["GOOGLE_CLIENT_SECRET"]
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

def authenticate_user():
    # Create a flow instance to manage the OAuth 2.0 Authorization Grant Flow steps
    flow = Flow.from_client_config(
        client_config={
            "web": {
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET,
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://accounts.google.com/o/oauth2/token"
            }
        },
        scopes=SCOPES,
        redirect_uri="http://localhost:8501"
    )

    # Generate the authorization URL
    auth_url, state = flow.authorization_url(prompt='consent')

    st.write('Please go to this URL and authorize access:', auth_url)

    # Ask for the authorization response URL
    auth_response = st.text_input('Enter the full URL you were redirected to:')

    if auth_response:
        # Use the response URL to fetch the access token
        flow.fetch_token(authorization_response=auth_response)

        # Use the access token to build the Google Drive service
        credentials = flow.credentials
        drive_service = build('drive', 'v3', credentials=credentials)
        return drive_service
    return None

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
