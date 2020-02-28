import deps.gspread
from deps.oauth2client.service_account import ServiceAccountCredentials

import spreadsheet

sheet = spreadsheet.get_sheet('UpdatedAnalysisSheet')
sheet.clear()