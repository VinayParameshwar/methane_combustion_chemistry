import cantera as ct
import numpy as np
from AFT import adiabatic_flame_temp
from NOx import NOx_concentration

# fuel and oxidizer data
# CH4 + 2(O2 + 3.76N2) --------> CO2 + 2H2O + 7.52 N2 (Stoichiometric Equation)
fuel = 'CH4'
oxidiser = 'O2:2,N2:7.56'

#Input Parameters
T0 = np.linspace(300,1300,11)  #in K 
P0 = np.array([1,2,5,20])*101325.0 # in Pa
phi = np.arange(0.4,2.01,0.01)

# Load GRI-Mech 3.0 (built-in mechanism)
gas = ct.Solution('gri30.yaml')

AFT = adiabatic_flame_temp(phi,T0, P0, fuel, oxidiser) 

NOx_Concentration = NOx_concentration(T0[0],P0[0],phi,AFT)





    


