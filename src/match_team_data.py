class MatchTeamData():


    def __init__(self, raw_data : list):
        self.raw_data = raw_data
        self.match_number = int(raw_data[2])
        self.team_number = int(raw_data[3])
        self.initiation_line = autoline_number(self.raw_data[5])
        self.auto_balls_high = int(self.raw_data[6])
        self.auto_balls_low = int(self.raw_data[7])
        self.auto_balls_missed_high = int(self.raw_data[8])
        self.auto_balls_missed_low = int(self.raw_data[9])
        self.auto_balls_picked_up = int(self.raw_data[10])
        self.high_balls = int(self.raw_data[11])
        self.low_balls = int(self.raw_data[12])
        self.high_balls_missed = int(self.raw_data[13])
        self.low_balls_missed = int(self.raw_data[14])
        self.control_panel_rot = autoline_number(self.raw_data[16])
        self.control_panel_pos = autoline_number(self.raw_data[17])
        self.control_panel_speed = autoline_number(self.raw_data[18])
        self.defense = autoline_number(self.raw_data[19])
        self.defense_type = self.raw_data[20]
        # change to number?
        self.climb_location = self.raw_data[21]
        self.buddy_climb = int(autoline_number(raw_data[22]))
        self.driver_skill = autoline_number(self.raw_data[23])
        self.comments = self.raw_data[24]
        self.inner_port_accuracy = float(int(self.raw_data[25])/5)
        self.climb_points = get_climb_points(self.climb_location)
        self.auto_points = 5 + self.auto_balls_high * (1- self.inner_port_accuracy) * 2 + self.auto_balls_high * self.inner_port_accuracy * 3 + self.auto_balls_low
        self.teleop_points = self.high_balls * (1 - self.inner_port_accuracy) * 2 + self.high_balls * self.inner_port_accuracy * 3 + self.low_balls + self.climb_points
        self.high_shot_accuracy = 1 - ((self.high_balls_missed + self.auto_balls_missed_high) / (self.high_balls + self.auto_balls_high))







def string_to_num(string_num_dict : dict, key : str):
        return string_num_dict.get(key)

# Level 1 returns a value of 1, Level 2 returns a value of 2
def hab_level_number(level : str):
        return string_to_num({ 'Level 1' : 1, 'Level 2' : 2}, level)

# none returns 0, hatch returns 1, cargo returns 2
def preload_number(preload : str):
    return string_to_num({'None' : 0, 'Hatch' : 1, 'Cargo' : 2}, preload)

# yes returns 1, no returns 0
def autoline_number(cross : str):
    return string_to_num({'No' : 0, 'Yes' : 1}, cross)

def get_climb_points(location : str):
    if location == "Middle":
        return 25
    elif location == "Side":
        return 25
    else:
        return 0

# print(hab_level_number('Level 2'))
