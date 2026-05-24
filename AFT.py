def adiabatic_flame_temp(phi,T0, P0, fuel, oxidiser):
    import cantera as ct
    gas = ct.Solution('gri30.yaml')

    AFT_phi = [0]*len(phi)
    AFT_T = [0]*len(T0)
    AFT_P = [0]*len(P0)

    for i in range(len(phi)):
        gas.set_equivalence_ratio(phi[i],fuel,oxidiser)
        gas.TP = T0[0], P0[0]
        gas.equilibrate('HP','auto')
        AFT_phi[i] = gas.T

    for i in range(len(T0)):
        gas.set_equivalence_ratio(phi[60],fuel,oxidiser)
        gas.TP = T0[i], P0[0]
        gas.equilibrate('HP','auto')
        AFT_T[i] = gas.T

    for i in range(len(P0)):
        gas.set_equivalence_ratio(phi[60],fuel,oxidiser)
        gas.TP = T0[0], P0[i]
        gas.equilibrate('HP','auto')
        AFT_P[i] = gas.T

    

    plotting(phi,T0, P0,AFT_phi, AFT_T, AFT_P)    
    
    return AFT_phi


def plotting(phi,T0, P0,AFT_phi, AFT_T, AFT_P):
    import matplotlib.pyplot as matplot

    matplot.figure()
    matplot.plot(phi, AFT_phi)
    matplot.xlabel('Equivalence Ratio (\phi)')
    matplot.ylabel('Adiabatic Flame Temperature')
    matplot.title("Adiabatic Flame Temperature vs Equivalence Ratio")
    matplot.grid()
    matplot.show()

    matplot.figure()
    matplot.plot(T0, AFT_T)
    matplot.xlabel('Inlet Temperature')
    matplot.ylabel('Adiabatic Flame Temperature')
    matplot.title("Adiabatic Flame Temperature vs Inlet Temperature")
    matplot.grid()
    matplot.show()

    matplot.figure()
    matplot.plot(P0, AFT_P)
    matplot.xlabel('Inlet Pressure')
    matplot.ylabel('Adiabatic Flame Temperature')
    matplot.title("Adiabatic Flame Temperature vs Inlet Pressure")
    matplot.grid()
    matplot.show()
    