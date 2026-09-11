# Methane Combustion Modelling and Mechanism Reduction

A set of combustion chemistry studies on methane, progressing from hand-coded thermochemistry to detailed kinetics simulations, automatic mechanism generation and mechanism reduction. The work was completed as part of the **Combustion Chemistry** module at the Technical University of Munich (TUM).

The project is organised as nine exercises. The early exercises build the fundamentals from first principles (stoichiometry, energy balances, equilibrium). The later exercises use established tools (Cantera, RMG, pyMARS) to compute flame properties, analyse reaction pathways, and build and simplify chemical kinetic mechanisms.

---

## Tools

| Tool | Used for |
|---|---|
| **MATLAB** | Mixture stoichiometry calculations |
| **Python** (NumPy, Matplotlib) | Iterative thermochemistry solvers, post-processing and plotting |
| **[Cantera](https://cantera.org)** | Equilibrium, laminar flame speed, ignition delay, sensitivity and reaction path analysis |
| **[RMG](https://reactionmechanismgenerator.github.io)** (Reaction Mechanism Generator) | Automatic generation of a methane–air kinetic mechanism |
| **[pyMARS](https://github.com/Niemeyer-Research-Group/pyMARS)** | Reduction of a detailed kinetic mechanism |
| **[GRI-Mech 3.0](http://combustion.berkeley.edu/gri-mech/)** | Reference detailed mechanism for natural gas combustion |

---

## Exercises

### 1. Air–fuel ratio, mole fractions and mixture stoichiometry *(MATLAB)*

A MATLAB function that computes the oxidiser requirement, air–fuel ratio and mixture mole fractions for any hydrocarbon of the form CₓHᵧ. The function runs with or without user input:

| Call | Behaviour |
|---|---|
| `tutorial1` | Uses methane (x = 1, y = 4) and 55.5 litres of fuel as defaults |
| `tutorial1(x, y)` | User-defined hydrocarbon, default fuel quantity of 55.5 litres |
| `tutorial1(x, y, z)` | User-defined hydrocarbon and fuel quantity *z* in litres |

### 2. Heating values and adiabatic flame temperature *(Python)*

An iterative solver that calculates heating values and the adiabatic flame temperature (AFT) of methane from an energy balance between reactants and products, using enthalpies of formation and sensible enthalpy. The AFT is computed across equivalence ratios from 0.1 to 2.0 for combustion with both **air** and **pure oxygen**. For rich mixtures, the product composition is resolved using a temperature-dependent equilibrium constant.

### 3. Adiabatic flame temperature using Cantera *(Python, Cantera)*

The AFT of methane–air mixtures is recalculated with Cantera's chemical equilibrium solver over the same range of equivalence ratios. The results from the iterative solver in Exercise 2 are imported and compared against Cantera to assess the simplified approach.

### 4. NO formation at varying equivalence ratio *(Python)*

Nitric oxide concentration is estimated from the **Zeldovich (thermal NO) mechanism** as a function of equivalence ratio. The flame temperatures from both Exercise 2 and Exercise 3 are used as inputs, so the sensitivity of NO formation to the predicted flame temperature can be compared directly.

### 5. Laminar flame speed of premixed methane–air *(Python, Cantera)*

Laminar flame speed is computed with one-dimensional premixed flame simulations across equivalence ratios from 0.5 to 1.5, and compared against experimental data. Two parametric studies are performed:

- **Effect of pressure:** 1, 2, 5 and 20 atm at an initial temperature of 298 K
- **Effect of initial temperature:** 358, 393 and 428 K at 1 atm

### 6. Ignition delay time *(Python, Cantera)*

Ignition delay times are computed over a range of initial temperatures and compared against experimental data. The study covers:

- **Equivalence ratios:** 0.5, 1.0 and 1.5 (lean, stoichiometric and rich)
- **Pressures:** 1, 3, 5 and 10 atm

### 7. Sensitivity and reaction path analysis *(Python, Cantera)*

A sensitivity analysis identifies which elementary reactions have the strongest influence on laminar flame speed for a stoichiometric mixture at 298 K. Reaction path diagrams following carbon are generated to trace how methane is broken down into CO₂. Both analyses are carried out at **1 atm** and **20 atm** to examine how pressure changes the dominant chemistry.

### 8. Mechanism generation with RMG *(RMG, Cantera)*

A methane–air kinetic mechanism is generated automatically using the Reaction Mechanism Generator, supplemented with established thermochemistry and reaction libraries. The generated mechanism is benchmarked against **GRI-Mech 3.0** through:

- Laminar flame speed across equivalence ratios
- Ignition delay time at an equivalence ratio of 1.1
- Flame speed sensitivity analysis
- Reaction path diagrams

### 9. Mechanism reduction with pyMARS *(pyMARS, Cantera)*

The detailed GRI-Mech 3.0 mechanism is reduced using pyMARS with a sensitivity-based reduction method, producing two reduced mechanisms of **58 and 83 reactions**. Each reduced mechanism is checked against the full mechanism by comparing ignition delay times at an equivalence ratio of 1.1, and its reaction path diagram is compared to identify which intermediate species were removed during reduction.

---

## Requirements

- MATLAB (Exercise 1)
- Python 3 with NumPy and Matplotlib
- Cantera
- RMG-Py (Exercise 8)
- pyMARS (Exercise 9)

Cantera, RMG and pyMARS are most easily installed through conda. Refer to the official installation guide for each tool, linked in the Tools table above.

---

## Copyright

© 2024 Vinay Parameshwar. All rights reserved.
