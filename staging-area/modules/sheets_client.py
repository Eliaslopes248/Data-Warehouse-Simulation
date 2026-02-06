"""
This module has the class for a client
that interacts with the google sheets api
"""


from google.oauth2.service_account  import Credentials
from googleapiclient.discovery      import build
import os


class SheetClient():
    # construct client instance
    def __init__(self, source_type, sheet_id, sheet_range):
        self.source_type = source_type 
        self.sheet_id    = sheet_id
        self.sheet_range = sheet_range
        self.SCOPES      =  ["https://www.googleapis.com/auth/spreadsheets"]
        self.creds       = self.authClient()  
        self.service     = self.initService()


    # load json credentials
    def authClient(self):
        # Get the directory where this file is located
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Go up one level to staging-area, then into secrets
        staging_dir = os.path.dirname(current_dir)
        cred_path = os.path.join(staging_dir, "secrets", "cred.json")
        
        return Credentials.from_service_account_file(
                cred_path,
                scopes=self.SCOPES
            )

    # auth client and create wrapper
    def initService(self):
        return build("sheets", "v4", credentials= self.creds)

    # extract data from sheet
    def getValues(self):
        # init sheet
        sheet = self.service.spreadsheets()
        # fetch data from sheet
        result = sheet.values().get(
            spreadsheetId   =self.sheet_id,
            range           =self.sheet_range
        ).execute()
        # send data back
        return result

