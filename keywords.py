import pickle
from googleapiclient.discovery import build
def main():
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    return sheet
