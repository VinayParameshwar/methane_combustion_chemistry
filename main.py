import cantera as ct
import numpy as np
import matplotlib as matplot

# fuel and oxidizer data
# CH4 + 2(O2 + 3.76N2) --------> CO2 + 2H2O + 7.52 N2 (Stoichiometric Equation)
fuel = 'CH4'
oxidiser = 'O2:2,N2:7.56'

#Input Parameters
T0 = 300.0  #in K 
P0 = 101325.0 # in Pa
phi = np.arange(0.6,2.01,0.01)

# Load GRI-Mech 3.0 (built-in mechanism)
gas = ct.Solution('gri30.yaml')
gas.TPX = 300, ct.one_atm, 'CH4:1, O2:2, N2:7.52'

