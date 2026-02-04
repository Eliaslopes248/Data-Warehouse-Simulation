from google.oauth2.service_account  import Credentials
from googleapiclient.discovery      import build

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

creds = Credentials.from_service_account_file(
    "../secrets/comp267-service-account-6047ed12fda6.json",
    scopes=SCOPES
)

service = build("sheets", "v4", credentials=creds)

sheet = service.spreadsheets()
result = sheet.values().get(
    spreadsheetId="1y2PKW_Jk4DLWFEGo9wdSdVTpweXU1QN90wOh0BfT6Uo",
    range="Sheet1"
).execute()

values = result.get("values", [])
print(values)