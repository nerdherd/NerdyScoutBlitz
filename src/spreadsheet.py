import gspread as gspread
from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a client to interact with the Google Drive API
scope =  ['https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name("NerdyScoutBlitz-52160ecf0355.json", scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("Beach Blitz Match Scouting (Responses)").sheet1
# Scout 687, 330, 1197, 3309, 3476, 7042
def get_sheet(sheet_name : str):
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name("NerdyScoutBlitz-52160ecf0355.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open(sheet_name).sheet1
    return sheet

# Extract and print all of the values
# list_of_hashes = sheet.get_all_records()
# print(list_of_hashes)
# print(sheet.get_all_values())
# print(sheet.get_all_values()[0])
# print(sheet.get_all_values()[1])
# headers = []
# headers = sheet.get_all_values()[0]
# for x in range(len(headers)):
#     print(x, headers[x])

