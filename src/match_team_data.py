class MatchTeamData():


    def __init__(self, raw_data : list):
        self.raw_data = raw_data
        self.match_number = int(raw_data[2])
        self.team_number = int(raw_data[3])
        self.hab_start = hab_level_number(self.raw_data[5])
        self.preload = preload_number(self.raw_data[6])
        self.autoline = autoline_number(self.raw_data[7])
        self.sandstorm_rocket_hatches = int(self.raw_data[8])
        self.sandstorm_rocket_cargo = int(self.raw_data[9])
        self.sandstorm_cargo_ship_hatches = int(self.raw_data[10])
        self.sandstorm_cargo_ship_cargo = int(self.raw_data[11])
        self.sandstorm_hatches_dropped = int(self.raw_data[12])
        self.sandstorm_cargo_dropped = int(self.raw_data[13])
        self.rocket_hatches_level_1 = int(self.raw_data[14])
        self.rocket_hatches_level_2 = int(self.raw_data[15])
        self.rocket_hatches_level_3 = int(self.raw_data[16])
        self.rocket_cargo_level_1 = int(self.raw_data[17])
        self.rocket_cargo_level_2 = int(self.raw_data[18])
        self.rocket_cargo_level_3 = int(self.raw_data[19])
        self.cargo_ship_hatches = int(self.raw_data[20])
        self.cargo_ship_cargo = int(self.raw_data[21])
        self.played_defense = autoline_number(self.raw_data[22])
        self.defense_type = self.raw_data[23]
        self.climb_level = int(self.raw_data[24])
        self.driver_skill = int(self.raw_data[25])
        self.comments = self.raw_data[26]
        self.hatch_points = (self.sandstorm_rocket_hatches + self.sandstorm_cargo_ship_hatches + self.rocket_hatches_level_3 + self.rocket_hatches_level_2 + self.rocket_hatches_level_1 + self.cargo_ship_hatches) * 2
        self.cargo_points = (self.sandstorm_rocket_cargo + self.sandstorm_cargo_ship_cargo + self.rocket_cargo_level_3 + self.rocket_cargo_level_2 + self.rocket_cargo_level_1 + self.cargo_ship_cargo) * 3
        self.climb_points = get_climb_points(self.climb_level)
        self.total_points = self.hatch_points + self.cargo_points + self.climb_points


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

def get_climb_points(level : int):
    if level == 1:
        return 3
    elif level == 2:
        return 6
    elif level == 3:
        return 12
    else:
        return 0

# print(hab_level_number('Level 2'))
