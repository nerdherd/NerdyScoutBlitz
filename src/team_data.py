import statistics
from match_team_data import MatchTeamData
import math


class TeamData():

    def __init__(self, team_number, match_data : list):
        self.match_data = match_data
        self.team_number = team_number
        self.hatch_data_sandstorm = []
        self.cargo_data_sandstorm = []
        self.hatch_data = []
        self.cargo_data = []
        self.climb_data = []
        self.comments = []
        self.point_data = []
        self.climb_level_data = []
        self.mean_hatches = 0
        self.mean_cargo = 0
        self.median_hatches = 0
        self.median_cargo = 0
        self.median_climb_points = 0
        self.max_climb_points = 0
        self.max_climb_level = 0
        self.mode_climb_level = 0
        self.median_points_per_match = 0
        self.mean_points_per_match = 0
        self.max_hatches = 0
        self.max_cargo = 0
        self.calc()

    def calc(self):
        for match in self.match_data:
        #     match = MatchTeamData([])
            self.hatch_data.append(
                match.sandstorm_cargo_ship_hatches + match.rocket_hatches_level_1 + match.rocket_hatches_level_2 + match.rocket_hatches_level_3 + match.cargo_ship_hatches + match.sandstorm_rocket_hatches)

            self.cargo_data.append(
                match.sandstorm_cargo_ship_cargo + match.rocket_cargo_level_1 + match.rocket_cargo_level_2 + match.rocket_cargo_level_3 + match.cargo_ship_cargo + match.sandstorm_rocket_cargo)
            self.cargo_data_sandstorm.append(match.sandstorm_cargo_ship_cargo + match.sandstorm_rocket_cargo)
            self.hatch_data_sandstorm.append(match.sandstorm_cargo_ship_hatches + match.sandstorm_rocket_hatches)
            self.climb_data.append(match.climb_points)
            self.comments.append(match.comments)
            self.point_data.append(match.total_points)
            self.climb_level_data.append(match.climb_level)
        # self.
        print(self.team_number)
        self.mean_hatches = statistics.mean(self.hatch_data)
        self.mean_cargo = statistics.mean(self.cargo_data)
        self.median_hatches = statistics.median(self.hatch_data)
        self.median_cargo = statistics.median(self.cargo_data)
        self.median_climb_points = statistics.median(self.climb_data)
        self.max_climb_points = max(self.climb_data)
        self.max_climb_level = max(self.climb_level_data)
        try:
            self.mode_climb_level = statistics.mode(self.climb_level_data)
        except:
            self.mode_climb_level = max(self.climb_level_data)
        self.mean_points_per_match = statistics.mean(self.point_data)
        self.median_points_per_match = statistics.median(self.point_data)
        self.max_cargo = max(self.cargo_data)
        self.max_hatches = max(self.hatch_data)


def teams_to_csv(teams: list):
    csv = open("teams.csv", "w")
    csv.write("Team,AverageHatches,AverageCargo,MedianHatches,MedianCargo,MaxClimbLevel,MostFrequentClimbLevel,MeanPointsPerMatch,MedianPointsPerMatch,MaxCargo,MaxHatches,Comments\n")
    for team in teams:
        # team = TeamData(0, [])
        csv.write(data_to_csv_string([team.team_number, team.mean_hatches, team.mean_cargo, team.median_hatches, team.median_cargo, team.max_climb_level, team.mode_climb_level, team.mean_points_per_match, team.median_points_per_match, team.max_cargo, team.max_hatches, format_comments(team.comments)]))
    # csv.write()
    csv.close()


def data_to_csv_string(data : list):
    string = ''
    for x in data:
        string = string + str(x) + ','
    string = string + '\n'
    return string

def format_comments(comments : list):
    string = ''
    for x in comments:
        string = string + x + ';'
    return string

# teams_to_csv([])
# print(data_to_csv_string([1, 2, 3, 4, 5]))




