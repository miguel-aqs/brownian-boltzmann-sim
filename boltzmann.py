import numpy as np
import matplotlib.pyplot as plt

N = 2000
tMax = 1000


forces = np.random.randn(tMax, N)

h = np.cumsum(forces, axis=0)

plt.figure('Displacement of Unbound Brownian Motion', figsize=(10,6))
plt.plot(h[:, :200], linewidth=0.5)
plt.title('Displacement as a function of time of Brownian motion')
plt.xlabel('Time')
plt.xlim(left=0)  
plt.ylabel('Displacement')


times_to_plot = [4, 9, 19, 49, 99]
labels = ['t=5', 't=10', 't=20', 't=50', 't=100']
bins = np.arange(-50, 52)

plt.figure('Histogram of Displacement of Unbound Brownian Motion', figsize=(10,6))
for t, label in zip(times_to_plot, labels):
    plt.hist(h[t, :], bins=bins, histtype='step', label=label)

plt.title('Histograms of Displacement for Brownian particles')
plt.xlabel('Displacement')
plt.ylabel('Number of particles')
plt.legend()

h_reflect = np.zeros((2000,1000))
h_reflect[0, :] = 5

for t in range(1,2000):
    step = np.random.randn(1000)
    h_reflect[t, :] = abs(h_reflect[t-1, :] + step)

plt.figure('Displacement of a Bound Brownian Motion', figsize=(10,6))
plt.plot(h_reflect[:, :200], linewidth=0.5)
plt.title('Displacement as a function of time of Brownian motion')
plt.xlabel('Time')
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.ylabel('Displacement')

bins = np.arange(0, 102)

plt.figure('Histogram of Displacement of Bound Brownian Motion', figsize=(10,6))
for t, label in zip(times_to_plot, labels):
    plt.hist(h_reflect[t, :], bins=bins, histtype='step', label=label)

plt.title('Histograms of Displacement for Brownian particles')
plt.xlabel('Displacement')
plt.xlim(left=0)
plt.ylabel('Number of particles')
plt.legend()



plt.show()

#GRAPH WILL LOAD IN BEHIND THE HISTOGRAM SO JUST MOVE THE HISTOGRAM WINDOW