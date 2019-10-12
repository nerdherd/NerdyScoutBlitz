import gspread
from oauth2client.service_account import ServiceAccountCredentials

import spreadsheet
from match_team_data import MatchTeamData
from team_data import TeamData, teams_to_csv

beach_blitz_team_list = [4, 294, 399, 597, 687, 696, 968, 1138, 1836, 2122, 2637, 2659, 3309, 3473, 3476, 3647, 4079, 4201, 4276, 4322, 4619, 5012, 5199, 5810, 5818, 5966, 6072, 6220, 6535, 6560, 6904, 6960, 7042, 7157, 7230, 7447]

qual_2 = [7042, 696, 4201, 687, 4079, 2637]
qual_7 = [3647, 1836, 6072, 4201, 687, 4619]
qual_15 = [7157, 6560, 687, 5966, 5818, 5012]
qual_22 = [597, 7042, 687, 6535, 294, 6960]
qual_27 = [3647, 687, 5966, 6904, 4, 399]
qual_32 = [5818, 687, 1138, 3476, 3647, 4276]
qual_37 = [1138, 6535, 7230, 5810, 687, 4322]
qual_48 = [2122, 2637, 7157, 3309, 5012, 687]
qual_51 = [6220, 4322, 597, 6904, 2659, 687]
qual_57 = [696, 4276, 687, 5810, 5818, 1836]

# print(len(beach_blitz_team_list))
def generate_csv(team_list: list):
    sheet = spreadsheet.sheet
    scouting_data = sheet.get_all_values()
    scouting_data.remove(scouting_data[0])
    # team_list = [687, 330, 7042]
    team_dict = {}
    team_data_list = []
    # print(scouting_data)
    for team_num in team_list:
        team_dict.update({team_num : []})
        for data in scouting_data:
            if int(data[3]) == team_num:
                data_array = team_dict.get(team_num)
                data_array.append(MatchTeamData(data))
                team_dict.update({team_num : data_array})
    for team_num in team_list:
        team_data_list.append(TeamData(team_num, team_dict.get(team_num)))
    teams_to_csv(team_data_list)

# generate_csv([330, 7042, 687])
