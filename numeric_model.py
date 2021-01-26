import matplotlib.pyplot as plt
import numpy as np
import logging as log

from materials import Materials
from constants import Constants
from bethe_formula import EnergyWaste
from units import Units

from resources.perlin_noise import PerlinNoise


class NumericModel:
    def __init__(self, file_path="", cut=None, low_x=-9999, low_y=-9999,
                 max_x=9999, max_y=9999):
        self.file_path = file_path
        self.low_x = low_x
        self.low_y = low_y
        self.max_x = max_x
        self.max_y = max_y
        self.model_data = []
        self.cut = cut

    def start_model_processing(self):
        try:
            with open(self.file_path) as data_file:
                new_dat_x, new_dat_y, new_dat_z = self.separated_axes_values_from_file(
                    data_file)  # Function creates data table x, y, z from exported map in txt format
                # self.create_2d_vis(new_dat_x, new_dat_y, new_dat_z) # Function creates 2d visualisation of waste energy based on distance between two points
                # new_dat_x, new_dat_y, new_dat_z = self.generate_model() # Function creates random model based on Perlin Noise
                x, y, z = self.separated_axes_values(self.create_2d_vis(new_dat_z, res=30))
                self.model_plot_3d(x, y, z)  # Function shows data after cut (low_x, low_y, max_x.. etc..)

        except IndexError or IOError or FileNotFoundError as e:
            log.critical(
                f"{e} | LOCATION OF EXCEPTION: {self.__class__.__name__} | method: {self.start_model_processing().__name__}")

    def separated_axes_values_from_file(self, data_file):
        for line in data_file:
            line_temp = line.split(',')
            self.model_data.append([float(line_temp[0]), float(line_temp[1]), float(line_temp[2])])
        new_dat_x = []
        new_dat_y = []
        new_dat_z = []
        if self.cut:
            for dat in self.model_data:
                if self.low_x < dat[0] < self.max_x and self.low_y < dat[1] < self.max_y:
                    self.append_data_to_separate_array(dat, new_dat_x, new_dat_y, new_dat_z)
        else:
            for dat in self.model_data:
                self.append_data_to_separate_array(dat, new_dat_x, new_dat_y, new_dat_z)
        return new_dat_x, new_dat_y, new_dat_z

    def separated_axes_values(self, data):
        new_dat_x = []
        new_dat_y = []
        new_dat_z = []
        for dat in self.model_data:
            self.append_data_to_separate_array(dat, new_dat_x, new_dat_y, new_dat_z)
        return new_dat_x, new_dat_y, new_dat_z

    def get_numeric_model(self):
        return self.model_data

    @staticmethod
    def append_data_to_separate_array(dat, new_dat_x, new_dat_y, new_dat_z):
        new_dat_x.append(dat[0])
        new_dat_y.append(dat[1])
        new_dat_z.append(dat[2])

    @staticmethod
    def generate_model():
        noise = PerlinNoise(octaves=10, seed=1)
        xpix, ypix = 100, 100
        pic = [[noise([i / xpix, j / ypix]) for j in range(xpix)] for i in range(ypix)]
        return pic[0], pic[1], pic[2]

    @staticmethod
    def create_2d_vis(dat_z, res=30):
        e_s = EnergyWaste(material=Materials.SILICON, constants=Constants.CONSTANTS)
        e_c = EnergyWaste(material=Materials.CARBON, constants=Constants.CONSTANTS)
        x_y_tab = [[]]
        k = 50
        for i in range(res):
            for j in range(res):
                x_y_tab.append([i, j, dat_z[k]])
                k += 1
        temp = []
        for cord in x_y_tab:
            temp.append([cord[0], cord[1], e_s.energy_waste(unit=Units.MEV, dist=cord[2])[0]])
        return temp

    @staticmethod
    def model_plot_3d(new_dat_x, new_dat_y, new_dat_z):
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.plot_trisurf(np.array(new_dat_x), np.array(new_dat_y), np.array(new_dat_z), linewidth=0.2, antialiased=True)
        plt.show()
