import numpy as np
import matplotlib.pyplot as plt

tMax = 2000
N = 1000
dh = -0.05

showBase = True
showBound = True
showBoundBiased = True
showStDev = True


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
    h_reflect[0, :] = 5

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
    h_final[0, :] = 5

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


plt.show()

#GRAPH WILL LOAD IN BEHIND THE HISTOGRAM SO JUST MOVE THE HISTOGRAM WINDOW