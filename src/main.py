import gspread
from oauth2client.service_account import ServiceAccountCredentials

import spreadsheet
from match_team_data import MatchTeamData
from team_data import TeamData, teams_to_csv

beach_blitz_team_list = [4, 294, 399, 597, 599, 687, 696, 968, 1138, 1836, 2122, 2637, 2659, 3309, 3473, 3476, 3647, 4079, 4201, 4276, 4322, 4619, 5012, 5199, 5818, 5966, 6072, 6220, 6535, 6560, 6904, 6960, 7042, 7157, 7230, 7447]

qual_5 = [5199, 687, 5818, 7042, 2637, 4619]
qual_11 = [7447, 687, 6560, 1138, 696, 7230]
qual_18 = [696, 6904, 687, 599, 6220, 399]
qual_21 = [4619, 687, 4, 3473, 5199, 4201]
qual_29 = [7447, 3647, 2659, 687, 6535, 399]
qual_35 = [3476, 6535, 597, 687, 6960, 3473]
qual_39 = [6560, 1836, 4276, 687, 6960, 3473]
qual_48 = [687, 1138, 5966, 4276, 7157, 4322]
qual_53 = [2122, 6960, 2637, 2659, 3309, 687]
qual_59 = [294, 5012, 7157, 1836, 597, 687]

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

generate_csv([330, 7042, 687])
