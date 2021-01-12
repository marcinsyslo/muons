from materials import Materials
from constants import Constants
import math


class EnergyWaste:
    def __init__(self, material=Materials.AIR, dist=1, constants=Constants.CONSTANTS):
        self.electron_mass = constants.get("electron mass")
        self.electron_charge = constants.get("electron charge")
        self.muon_charge = constants.get("muon charge")
        self.muon_mass = constants.get("muon mass")
        self.B = constants.get("muon speed")
        self.c = constants.get("speed of light")
        self.PI = constants.get("PI")
        self.permittivity = constants.get("permittivity")
        self.av = constants.get("avogadro")
        self.a = material.get("a")
        self.z = material.get("z")
        self.density = material.get("density")
        self.mol_mass = material.get("mol mass")
        self.I = material.get("i")

    def energy_waste(self):
        return -((4 * self.PI * self.av * self.z * self.density)/(self.a * self.mol_mass * self.electron_mass * self.c * self.c)) * (math.pow((self.electron_charge * self.electron_charge)/(4 * self.PI * self.permittivity), 2) * ((self.muon_charge * self.muon_charge)/(self.B * self.B)) * (0.5*math.log(2*self.electron_mass*self.c*self.c*self.B*self.B*self.t_max(), math.e)/((1-(self.B*self.B))*self.I*self.I)) -(self.B*self.B))

    def t_max(self):
        con_y = self.y(self.B)
        return (2*self.electron_mass*(self.c * self.c) * (self.B * self.B) * (con_y * con_y))/(1+(2 * con_y * (
                self.electron_mass/self.muon_mass))+(math.pow(self.electron_mass/self.muon_mass, 2)))

    @staticmethod
    def y(b):
        return math.pow(1/(1-(math.pow(b, 2))), 0.5)
