import matplotlib.pyplot as plt
import numpy as np

import particleGenerator as pg

if __name__ == "__main__":
    muon_model = pg.MuonDistribution().Earth()
    particles = []
    for i in range(8000):
        particles.append(muon_model.get_muon())

    particles = np.array(particles).T

    plt.hist(particles[1],bins=200)
    plt.xlabel("Theta [rad]")
    plt.ylabel("counts")
    plt.show()
    plt.clf()

    plt.plot(particles[1], particles[0], "ro")
    plt.xlabel("Theta [rad]")
    plt.ylabel("flux [$m^{-2} s^{-1} sr^1$]")
    plt.yscale("log")
    plt.show()
    plt.clf()

    plt.hist(particles[2],bins=200)
    plt.xlabel("Energy [GeV]")
    plt.ylabel("counts")
    plt.show()
    plt.clf()

