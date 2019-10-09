import gspread
from oauth2client.service_account import ServiceAccountCredentials

import spreadsheet
from match_team_data import MatchTeamData
from team_data import TeamData, teams_to_csv

sheet = spreadsheet.sheet
scouting_data = sheet.get_all_values()

# for x in range(0, len(scouting_data)):
#     print(scouting_data[x])
scouting_data.remove(scouting_data[0])
team_list = [687, 330, 7042]
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

# for team in team_data_list:
#     print(team.max_climb_points)

# print(team_dict)
# print(team_dict.items())
teams_to_csv(team_data_list)
