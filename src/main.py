import gspread as gspread
from oauth2client.service_account import ServiceAccountCredentials

import spreadsheet
from match_team_data import MatchTeamData
from team_data import *

# team_list = [4, 294, 399, 597, 687, 696, 968, 1138, 1836, 2122, 2637, 2659, 3309, 3473, 3476, 3647, 4079, 4201, 4276, 4322, 4619, 5012, 5199, 5810, 5818, 5966, 6072, 6220, 6535, 6560, 6904, 6960, 7042, 7157, 7230, 7447]
# team_list = [207, 597, 606, 687, 841, 980, 987, 1197, 1452, 1515, 1759, 1836, 2576, 2637, 2710, 3408, 3512, 3952, 4019, 4123, 4201, 4400, 4501, 4578, 4964, 4999, 5089, 5124, 5510, 5512, 5553, 5634, 5669, 5802, 6000, 6658, 6904, 6938, 7033, 7051, 7185, 7447, 7455, 8159]
# team_list = [207, 597, 606, 687, 841, 980, 987, 1197, 1515, 1759, 1836, 2576, 2637, 2710, 3408, 3512, 3952, 4019, 4123, 4201, 4400, 4501, 4578, 4964, 4999, 5089, 5124, 5510, 5512, 5553, 5634, 5669, 5802, 6000, 6658, 6904, 6938, 7033, 7051, 7185, 7447, 7455, 8159]
headers = ["Team", "Average Auto Score", "Max Auto Score", "Average Auto Balls Low", "Average Auto Balls High", "Max Auto Balls Low", "Max Auto Balls High", "Average Teleop Balls Low", "Average Teleop Balls High", "Max Teleop Balls Low", "Max Teleop Balls High", "Average Teleop Score", "Max Teleop Score", "Ball Accuracy (High)", "Climb Frequency", "Control Panel Rotation Frequency", "Control Panel Position Frequency", "Matches Scouted"]
# output_sheet = "LAR Analyzed Data"
# input_sheet = "LAR Match Scouting Form (Responses)"
output_sheet = "LAR Analyzed Data"
input_sheet = "Test Scouting Form (Responses-New)"
# print(len(beach_blitz_team_list))
def generate_csv(team_list: list):
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name("NerdyScoutBlitz-52160ecf0355.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open(input_sheet).sheet1
    scouting_data = sheet.get_all_values()
    scouting_data.remove(scouting_data[0])
    # team_list = [687, 330, 7042]
    team_dict = {}
    team_data_list = []
    # print(scouting_data)
    for team_num in team_list:
        # print(team_num)
        team_dict.update({team_num : []})
        # team_list = []
        for data in scouting_data:
            # print(data)
            # try:
                # print(data)
                # print(team_num)
            if (data[3] != '') and (int(data[3]) == team_num):
                # print(team_num, 971)
                data_array = team_dict.get(team_num)
                data_array.append(MatchTeamData(data))
                team_dict.update({team_num : data_array})
            # except:
            #     pass
    print("yes")
    print(team_list)
    for team_num in team_list:
        print(team_list)
        # print(team_num)
        try:
            team_data_list.append(TeamData(team_num, team_dict.get(team_num)))
        # print(TeamData(team_num, team_dict.get(team_num)))
        except:
            pass
    # teams_to_csv(team_data_list)
    # print(team_data_list[0].team_number)

    analyzed_sheet = spreadsheet.get_sheet(output_sheet)
    analyzed_sheet.clear()
    analyzed_sheet.append_row(headers)
    # analyzed_sheet.append_row([1, 2, 3, 4])
    for team in team_data_list:
        analyzed_sheet.append_row(team.to_list())
        # return team.to_list()
        # print(team.to_list())
        # print(len(team.to_list()))
        # print(len(headers))

# generate_csv([330, 7042, 687])


#generate_csv(team_list)
def run(event, context):
    generate_csv([207, 597, 606, 687, 841, 980, 987, 1197, 1452, 1515, 1759, 1836, 2576, 2637, 2710, 3408, 3512, 3952, 4019, 4123, 4201, 4400, 4501, 4578, 4964, 4999, 5089, 5124, 5510, 5512, 5553, 5634, 5669, 5802, 6000, 6658, 6904, 6938, 7033, 7051, 7185, 7447, 7455, 8159])


# generate_csv([207, 597, 606, 687, 841, 980, 987, 1197, 1452, 1515, 1759, 1836, 2576, 2637, 2710, 3408, 3512, 3952, 4019, 4123, 4201, 4400, 4501, 4578, 4964, 4999, 5089, 5124, 5510, 5512, 5553, 5634, 5669, 5802, 6000, 6658, 6904, 6938, 7033, 7051, 7185, 7447, 7455, 8159])
