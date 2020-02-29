import statistics
from match_team_data import MatchTeamData


class TeamData():

    def __init__(self, team_number, match_data : list):
        self.match_data = match_data
        self.team_number = team_number
        self.auto_score_data = []
        self.auto_ball_data_high = []
        self.auto_ball_data_low = []
        self.teleop_score_data = []
        self.teleop_ball_data_high = []
        self.teleop_ball_data_low = []
        self.ball_accuracy_data = []
        self.climb_data = []

        self.mean_auto_score = 0
        self.mean_auto_balls_high = 0
        self.mean_auto_balls_low = 0
        self.max_auto_score = 0
        self.max_auto_balls_high = 0
        self.max_auto_balls_low = 0
        self.mean_teleop_balls_high = 0
        self.max_teleop_balls_high = 0
        self.mean_teleop_balls_low = 0
        self.max_teleop_balls_low = 0
        self.mean_teleop_score = 0
        self.max_teleop_score = 0
        self.mean_ball_accuracy = 0
        self.climb_frequency = 0
        self.calc()

    def calc(self):
        for match in self.match_data:
            # match = MatchTeamData([])
            self.auto_ball_data_high.append(match.auto_balls_high)
            self.auto_ball_data_low.append(match.auto_balls_low)
            self.auto_score_data.append(match.auto_points)
            self.teleop_ball_data_high.append(match.high_balls)
            self.teleop_ball_data_low.append(match.low_balls)
            self.teleop_score_data.append(match.teleop_points)
            self.ball_accuracy_data.append(match.high_shot_accuracy)
            self.climb_data.append(match.climb_points)

            self.mean_auto_score = statistics.mean(self.auto_score_data)
            self.mean_auto_balls_high = statistics.mean(self.auto_ball_data_high)
            # print(self.auto_ball_data_high)
            # print(self.mean_auto_balls_high)
            self.mean_auto_balls_low = statistics.mean(self.auto_ball_data_low)
            self.mean_teleop_balls_high = statistics.mean(self.teleop_ball_data_high)
            self.mean_teleop_balls_low = statistics.mean(self.teleop_ball_data_low)
            self.mean_teleop_score = statistics.mean(self.teleop_score_data)
            self.mean_ball_accuracy = statistics.mean(self.ball_accuracy_data)

            self.max_auto_balls_high = max(self.auto_ball_data_high)
            self.max_auto_balls_low = max(self.auto_ball_data_low)
            self.max_auto_score = max(self.auto_score_data)
            self.max_teleop_balls_high = max(self.teleop_ball_data_high)
            self.max_teleop_balls_low = max(self.teleop_ball_data_low)
            self.max_teleop_score = max(self.teleop_score_data)
            print(self.climb_data)
            self.climb_frequency = self.climb_data.count(25)
            # for x in self.climb_data:
                # print(x)
                # if x == 25:
                #     self.climb_frequency += 1
            print(self.climb_frequency)


        # self.
        # print(self.team_number)
        # self.mean_hatches = statistics.mean(self.hatch_data)
        # self.mean_cargo = statistics.mean(self.cargo_data)
        # self.median_hatches = statistics.median(self.hatch_data)
        # self.median_cargo = statistics.median(self.cargo_data)
        # self.median_climb_points = statistics.median(self.climb_data)
        # self.max_climb_points = max(self.climb_data)
        # self.max_climb_level = max(self.climb_level_data)
        # try:
        #     self.mode_climb_level = statistics.mode(self.climb_level_data)
        # except:
        #     self.mode_climb_level = max(self.climb_level_data)
        # self.mean_points_per_match = statistics.mean(self.point_data)
        # self.median_points_per_match = statistics.median(self.point_data)
        # self.max_cargo = max(self.cargo_data)
        # self.max_hatches = max(self.hatch_data)

    def to_list(self):
        return  [self.team_number, self.mean_auto_score, self.max_auto_score, self.mean_auto_balls_low, self.mean_auto_balls_high, self.max_auto_balls_low, self.max_auto_balls_high, self.mean_teleop_balls_low, self.mean_teleop_balls_high, self.max_teleop_balls_low, self.max_teleop_balls_high, self.mean_teleop_score, self.max_teleop_score, self.mean_ball_accuracy, self.climb_frequency]

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




