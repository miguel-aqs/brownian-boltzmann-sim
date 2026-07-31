import numpy as np
import matplotlib.pyplot as plt

tMax = 2000
N = 1000
dh = -0.05
initialH = 5 #note that initialH is only for showBound and showBoundBiased since showBase starts at 0

#molar masses and kelvin
m_O16 = 18.0
m_O18 = 20.0
T_cold = 260
T_warm = 300

showBase = False
showBound = True
showBoundBiased = True
showStDev = True
showIsotopeSim = True


forces = np.random.randn(tMax, N)

h = np.cumsum(forces, axis=0) 

times_to_plot = [4, 9, 19, 49, 99]
labels = ['t=5', 't=10', 't=20', 't=50', 't=100']
bins = np.arange(-50, 52)

if showBase:
    plt.figure('Displacement of Unbound Brownian Motion', figsize=(10,6))
    plt.plot(h[:, :200], linewidth=0.5)
    plt.title('Displacement as a function of time of unbound Brownian motion')
    plt.xlabel('Time')
    plt.xlim(left=0, right=tMax)  
    plt.ylabel('Displacement')

    plt.figure('Histogram of Displacement of Unbound Brownian Motion', figsize=(10,6))
    for t, label in zip(times_to_plot, labels):
        plt.hist(h[t, :], bins=bins, histtype='step', label=label)

    plt.title('Histograms of Displacement for Unbound Brownian particles')
    plt.xlabel('Displacement')
    plt.ylabel('Number of particles')
    plt.legend()

if showBound:
    h_reflect = np.zeros((tMax,N))
    h_reflect[0, :] = initialH

    for t in range(1,tMax):
        step = np.random.randn(N)
        h_reflect[t, :] = abs(h_reflect[t-1, :] + step)

    plt.figure('Displacement of Bound Brownian Motion', figsize=(10,6))
    plt.plot(h_reflect[:, :200], linewidth=0.5)
    plt.title('Displacement as a function of time of bound Brownian motion')
    plt.xlabel('Time')
    plt.xlim(left=0, right=tMax)
    plt.ylim(bottom=0)
    plt.ylabel('Displacement')

    bins = np.arange(0, 102)

    plt.figure('Histogram of Displacement of Bound Brownian Motion', figsize=(10,6))
    for t, label in zip(times_to_plot, labels):
        plt.hist(h_reflect[t, :], bins=bins, histtype='step', label=label)

    plt.title('Histograms of Displacement for Bound Brownian particles')
    plt.xlabel('Displacement')
    plt.xlim(left=0, right=60)
    plt.ylabel('Number of particles')
    plt.legend()

if showBoundBiased:
    h_final = np.zeros((tMax,N))
    h_final[0, :] = initialH

    for t in range(1,tMax):
        step = np.random.randn(N)
        h_final[t, :] = abs(h_final[t-1, :] + step + dh)

    plt.figure('Displacement of a Biased Bound Brownian Motion', figsize=(10,6))
    plt.plot(h_final[:, :200], linewidth=0.5)
    plt.title('Displacement as a function of time of Biased Bound Brownian motion')
    plt.xlabel('Time')
    plt.xlim(left=0, right=tMax)
    plt.ylim(bottom=0)
    plt.ylabel('Displacement')

    bins = np.arange(0, 102)

    plt.figure('Histogram of Displacement of Biased Bound Brownian Motion', figsize=(10,6))
    for t, label in zip(times_to_plot, labels):
        plt.hist(h_final[t, :], bins=bins, histtype='step', label=label)

    plt.title('Histograms of Displacement for Biased Bound Brownian particles')
    plt.xlabel('Displacement')
    plt.xlim(left=0, right=60)
    plt.ylabel('Number of particles')
    plt.legend()

if showStDev:
    plt.figure('Standard Deviation Comparison', figsize=(10,6))

    if showBase:
        plt.plot(np.std(h, axis=1), label='Unbound Brownian Motion')

    if showBound:
        plt.plot(np.std(h_reflect, axis=1), label='Bound (No Gravity)')

    if showBoundBiased:
        plt.plot(np.std(h_final, axis=1), label='Bound + Gravity')

    plt.title('Particle Spread ($\sigma$) Over Time (Standard Deviation)')
    plt.xlabel('Time Step')
    plt.ylabel('Standard Deviation ($\sigma$)')
    plt.xlim(left=0, right=tMax)
    plt.ylim(bottom=0)
    plt.legend()

if showIsotopeSim:
    def run_isotope_sim(mass, temp, tMax=2000, N=1000):
        step_scale = np.sqrt(temp / mass) * 0.1   
        dh = -(mass / temp) * 0.5                  
    
        h_sim = np.zeros((tMax, N))
        h_sim[0, :] = 5.0  
    
        for t in range(1, tMax):
            step = np.random.randn(N) * step_scale
            h_sim[t, :] = np.abs(h_sim[t-1, :] + step + dh)
        
        return h_sim
    
    h_O16_cold = run_isotope_sim(m_O16, T_cold)
    h_O18_cold = run_isotope_sim(m_O18, T_cold)
    h_O16_warm = run_isotope_sim(m_O16, T_warm)
    h_O18_warm = run_isotope_sim(m_O18, T_warm)

    plt.figure('Climate Isotope Spread Comparison (Standard Deviation)', figsize=(10, 6))
    plt.plot(np.std(h_O16_warm, axis=1), label='H2(16O) - Warm (300K)', color='red')
    plt.plot(np.std(h_O18_warm, axis=1), label='H2(18O) - Warm (300K)', color='orange')
    plt.plot(np.std(h_O16_cold, axis=1), label='H2(16O) - Cold (260K)', color='cyan')
    plt.plot(np.std(h_O18_cold, axis=1), label='H2(18O) - Cold (260K)', color='blue')

    plt.title('Vertical Atmospheric Spread ($\sigma$) of Water Isotopes Across Climates')
    plt.xlabel('Time Step')
    plt.ylabel('Standard Deviation ($\sigma$)')
    plt.xlim(left=0, right=tMax)
    plt.ylim(bottom=0)
    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.figure('Climate Isotope Comparison (Mean)', figsize=(10, 6))
    plt.plot(np.mean(h_O16_warm, axis=1), label='H2(16O) - Warm (300K)', color='red')
    plt.plot(np.mean(h_O18_warm, axis=1), label='H2(18O) - Warm (300K)', color='orange')
    plt.plot(np.mean(h_O16_cold, axis=1), label='H2(16O) - Cold (260K)', color='cyan')
    plt.plot(np.mean(h_O18_cold, axis=1), label='H2(18O) - Cold (260K)', color='blue')

    plt.title('Mean Vertical Atmospheric Spread of Water Isotopes Across Climates')
    plt.xlabel('Time Step')
    plt.ylabel('Mean')
    plt.xlim(left=0, right=tMax)
    plt.ylim(bottom=0)
    plt.legend()
    plt.grid(True, alpha=0.3)

plt.show()

#GRAPH WILL LOAD IN BEHIND THE HISTOGRAM SO JUST MOVE THE HISTOGRAM WINDOW