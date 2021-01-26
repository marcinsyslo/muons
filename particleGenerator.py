import numpy as np
from constants import Constants

###############################
# cosmic_muons generator      #
# name: particleGenerator.py  #
# author: Albert Szadziński   #  
###############################

# Example usage:
# model = MuonDistribution().Earth()
# model.get_muon() # optional param: theta_range = [min, max]
# output: flux [m^-2s^-1sr^1], theta [rad], Energy [Gev]


class MuonDistribution:
    def __init__(self, planetR=0, d=0):
        self.R = planetR
        self.pi = Constants.CONSTANTS["PI"]
        self.d = d

    @classmethod
    def Earth(cls):
        return MuonDistribution(Constants.CONSTANTS["earthR"], Constants.CONSTANTS["chapmanD"])

    def chapmanEq(self, theta):
        #DOI: 10.1142/S0217751X18501750
        D = np.sqrt(self.R**2/self.d**2 * np.cos(theta)**2 + 2*self.R / self.d + 1) - self.R/self.d * np.cos(theta)
        return 1/D**2

    def fluxEq(self,_theta):
        I_0 = 85.6 # m^-2 sec^-1 sr^1
        n = 3.1
        return  I_0 * np.cos(_theta)**(n-1)
    
    def GaisserEq(self,E,_theta):
        #https://arxiv.org/abs/1509.06176
        I_0 = 70 # _flux # m^-2 sec^-1 sr^1
        E_0 = 4.29 # GeV
        n = 3.1
        ie = 1/854 # 1/GeV
        #return 0.14*(E*(1+(3.64/(E*np.cos(_theta)**1.29))))**(-2.7)*((1/(1+(1.1*E*np.cos(_theta)/115)))+(0.054/(1+(1.1*E*np.cos(_theta)/850))))
        return np.random.standard_gamma(2)

    def neumann(self,_range, _distribution):
        _r1, _r2 = _range[0]+(_range[1]-_range[0])*np.random.uniform(), np.random.uniform()

        while _distribution(_r1)/_range[1] <= _r2:
            _r1 = _range[0]+(_range[1]-_range[0])*np.random.uniform()
            _r2 = np.random.uniform()
        return _r1

    def get_muon(self, _range=[0,np.pi/2]):
        _theta = self.neumann(_range, self.chapmanEq)
        _flux = self.fluxEq(_theta)
        _energy = self.GaisserEq(0,0) 
        return _flux, _theta, _energy

    def generator(self, nparticle=1000):
        pass
        #yield 1
        
