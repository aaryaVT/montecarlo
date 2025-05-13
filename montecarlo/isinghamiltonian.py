import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random
import math
import copy as cp
from .bitstring import *
random.seed(2)

class IsingHamiltonian:

    def __init__(self, G):
        self.G = G
        self.length = G.number_of_nodes()
        self.mu = np.zeros(self.length)

    def energy(self, bs: BitString):
        
        E = 0
        si = 0
        sj = 0
        M = 0

        for i, j in self.G.edges:
            if bs.config[i] == 0:
                si = -1
            else:
                si = 1
            if bs.config[j] == 0:
                sj = -1
            else:
                sj = 1
            J = self.G[i][j]['weight']
            M = self.mu[i] * si
            E += J * si * sj  + M    
        return E
    
    def compute_average_values(self, T: float):
    
        bs = BitString(self.length)
        E  = 0.0  #energy
        M  = 0.0  # the excess number of spins
        EE = 0.0  
        MM = 0.0
        Z = 0.0  # energy for z
        k = 1  # the constant k 
        beta = 1/(k * T)
        EN = 0.0
        
        i = 0

        for i in range(2**len(bs)):
            bs.set_integer_config(i)
            Z += np.exp( -1 * beta * self.energy(bs))
        
        # to calculating all the values
        for i in range(2**len(bs)):
            bs.set_integer_config(i)
            EN = self.energy(bs)
            P = np.exp( -beta * EN) / Z
            E += EN * P
            EE += (EN ** 2) * P     
            m = bs.on() - bs.off()
            M += m * P
            MM += (m ** 2) * P

        HC = (EE - (E ** 2)) / (T ** 2)
        MS = (MM - (M ** 2)) / T    
        
        return E, M, HC, MS
    
    def set_mu(self, mus: np.array):
        self.mu = mus

