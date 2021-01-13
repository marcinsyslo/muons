import math


class Materials:
    IRON = {
        "z": 26,
        "a": 55,
        "mol mass": 0.005,  # kg/mol (Fe)
        "density": 7874,  # kg/m3 (SiO2)
        "i": 717000 / (1.6 * math.pow(10, -19))  # eV/mol
    }
    SILICON = {
        "z": 14,
        "a": 28,
        "mol mass": 0.006, # kg/mol (SiO2)
        "density": 2330, # kg/m3 (SiO2)
        "i": 786000/(1.6*math.pow(10,-19)) # eV/mol
    }
    AIR = {
        "z": 7,
        "a": 14,
        "mol mass": 0.0028, # kg/mol (N)
        "density": 808, # kg/m3 (N)
        "i": 1402000/(1.6*math.pow(10,-19)) # eV/mol
    }
