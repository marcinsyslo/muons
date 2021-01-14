import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict


from particle import Particle
from materials import Materials
from constants import Constants
from bethe_formula import EnergyWaste

from resources.perlin_noise import PerlinNoise


class NumericModel:
    def __init__(self, file_path="", cut=None, low_x=-9999, low_y=-9999,
                 max_x=9999, max_y=9999, particle_vector=None):
        if particle_vector is None:
            particle_vector = [1, 0, 0]  # surface
        self.file_path = file_path
        self.low_x = low_x
        self.low_y = low_y
        self.max_x = max_x
        self.max_y = max_y
        self.model_data = []
        self.cut = cut
        self.particle_vector = particle_vector
        self.log = ""

    def start_model_processing(self):
        try:
            with open(self.file_path) as data_file:
                new_dat_x, new_dat_y, new_dat_z = self.separated_axes_values(data_file) # Function creates data table x, y, z from exported map in txt format
                # self.create_2d_vis(new_dat_x, new_dat_y, new_dat_z) # Function creates 2d visualisation of waste energy based on distance between two points
                # new_dat_x, new_dat_y, new_dat_z = self.generate_model() # Function creates random model based on Perlin Noise
                self.create_2d_vis(new_dat_x, new_dat_y, new_dat_z)
                self.model_plot_3d(new_dat_x, new_dat_y, new_dat_z) # Function shows data after cut (low_x, low_y, max_x.. etc..)

        except IndexError or IOError as e:
            self.log = e
        finally:
            print(self.log)

    def separated_axes_values(self, data_file):
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
        return pic[0], pic[2], pic[1]

    @staticmethod
    def create_2d_vis(dat_x, dat_y, dat_z):
        e = EnergyWaste(material=Materials.SILICON, dist=1, constants=Constants.CONSTANTS)
        dat = []
        i = 0
        for x in dat_x:
            dat.append([x, dat_y[i], dat_z[i]])
            i += 1
        sorted_x = sorted(dat, key=lambda x_d: x_d[0])
        sorted_y = sorted(dat, key=lambda y_d: y_d[1])
        temp_x_y = []
        i = 0
        for x in sorted_x:
            temp_x_y.append([i,x[0],x[1],x[2]])
            i += 1
        print(temp_x_y)
        sorted_x_y = sorted(temp_x_y, key=lambda x: x[2]) # [x_index, x,y(sorted),z]
        print(sorted_x_y)

    @staticmethod
    def check_dist_underground(x, y, z, dat_x, dat_y, dat_z, vec=None):
        if vec is None:
            vec = [1, 0, 0]
        muon = Particle(size=1, x=x, y=y, z=z)
        r = len(dat_x)

    @staticmethod
    def model_plot_3d(new_dat_x, new_dat_y, new_dat_z):
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.plot_trisurf(np.array(new_dat_x), np.array(new_dat_y), np.array(new_dat_z), linewidth=0.2, antialiased=True)
        plt.show()
