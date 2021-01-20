import math


class Materials:
    IRON = {
        "z": 26,
        "a": 55,
        "molar mass": 0.005,  # kg/mol (Fe)
        "density": 7874,  # kg/m3 (SiO2)
        "i": 717000 / (1.6 * math.pow(10, -19))  # eV/mol
    }
    SILICON = {
        "z": 14,
        "a": 28,
        "molar mass": 0.006,  # kg/mol (SiO2)
        "density": 2330,  # kg/m3 (SiO2)
        "i": 786000 / (1.6 * math.pow(10, -19))  # eV/mol
    }
    CARBON = {
        "z": 6,
        "a": 12,
        "molar mass": 0.0012,
        "density": 2000,  # kg/m3 (C)
        "i": 1087000 / (1.6 * math.pow(10, -19))  # eV/mol
    }
    AIR = {
        "z": 7,
        "a": 14,
        "molar mass": 0.0028,  # kg/mol (N)
        "density": 808,  # kg/m3 (N)
        "i": 1402000 / (1.6 * math.pow(10, -19))  # eV/mol
    }
