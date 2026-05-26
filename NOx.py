def NOx_concentration(T0,P0,phi,AFT):
    import numpy as np
    import math as mt

    #NASA polynomials
    a1 = 6.434
    a2 = -0.2755
    a3 = 0.02396
    a4 = -0.111*10**(-2)
    a5 = 0.8258
    a6 = -25.80

    t = 0.005

    X_N2 = 0.79 # Mole Fraction of N2
    X_O2 = 0.21 # Mole Fraction of O2
    R = 8.314   # Universal Gas Constant

    concentration_NO = np.zeros(len(AFT))

    for i in range(len(AFT)):
        
        C_N2 = X_N2 * P0 /(AFT[i]*R)
        C_O2 = X_O2 * P0/(AFT[i]*R)

        Kf_1 = 1.8 * 10**(8) * (mt.exp(-318000/(R*AFT[i])))

        theta = AFT[i]/1000

        Kp_log = a1 + (a2 * theta) + (a3 * theta ** 2) + (a4 * theta ** 3) + (a5 * mt.log(theta)) + (a6 / theta)

        Kp = 10**(Kp_log)

        C_NO = Kf_1 * (mt.sqrt(Kp * P0 / (AFT[i] * R))) * mt.sqrt(C_O2) * C_N2 * t

        concentration_NO[i] = 0.42 * C_NO * 10 ** 6

    plotting(concentration_NO, AFT, phi)
    return concentration_NO

def plotting(concentration_NO, AFT, phi):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as matplot
    import numpy as np

    fig, axis1 = matplot.subplots()

    axis1.plot(phi, AFT, 'r-')
    axis1.set_xlabel('Equivalence Ratio')
    axis1.set_ylabel('Adiabatic Flame Temperature', color='r')

    axis2 = axis1.twinx()
    axis2.plot(phi, concentration_NO, 'b-')
    axis2.set_ylabel('NO concentration [NO] in PPM', color='b')

    matplot.title("NO concentration for calculated AFT")

    matplot.xticks(np.arange(0.4, 2.01, 0.2))

    axis1.grid(True)
    axis2.grid(True)

    matplot.grid()
    matplot.savefig('Images/NOx_vs_phi.png')



