import numpy as np
import matplotlib.pyplot as plt

N = 10000
tMax = 100


forces = np.random.randn(tMax, N)

h = np.cumsum(forces, axis=0)



plt.figure(figsize=(10,6))
plt.plot(h[:, :200], linewidth=0.5)
plt.title('Displacement as a function of time of Brownian motion')
plt.xlabel('Time')
plt.ylabel('Displacement')


times_to_plot = [4, 9, 19, 49, 99]
labels = ['t=5', 't=10', 't=20', 't=50', 't=100']
bins = np.arange(-50, 52)

plt.figure(figsize=(10,6))
for t, label in zip(times_to_plot, labels):
    plt.hist(h[t, :], bins=bins, histtype='step', label=label)

plt.title('Histograms of Displacement for Brownian particles')
plt.xlabel('Displacement')
plt.ylabel('Number of particles')
plt.legend()


plt.show()

#GRAPH WILL LOAD IN BEHIND THE HISTOGRAM SO JUST MOVE THE HISTOGRAM WINDOW