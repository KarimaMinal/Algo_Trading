from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import pandas as pd

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'service_account.json'

def authenticate():
    creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return build('sheets', 'v4', credentials=creds)

def update_sheet(spreadsheet_id, sheet_range, dataframe):
    service = authenticate()
    sheet = service.spreadsheets()

    dataframe.columns = [str(c) for c in dataframe.columns]
    dataframe = dataframe.fillna('-')

    values = [list(dataframe.columns)] + dataframe.astype(str).values.tolist()
    body = {'values': values}

    sheet.values().update(
        spreadsheetId=spreadsheet_id,
        range=sheet_range,
        valueInputOption="RAW",
        body=body
    ).execute()

def update_trades_sheet(spreadsheet_id, sheet_range, dataframe):
    update_sheet(spreadsheet_id, sheet_range, dataframe)

def update_summary_sheet(spreadsheet_id, sheet_range, dataframe):
    update_sheet(spreadsheet_id, sheet_range, dataframe)

def update_ml_sheet(spreadsheet_id, sheet_range, dataframe):
    update_sheet(spreadsheet_id, sheet_range, dataframe)
