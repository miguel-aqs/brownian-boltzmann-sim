# Brownian Motion - Boltzmann Distribution Simulation

A Python implementation of a Boltzmann distribution and Brownian motion simulation, adapted from a MATLAB-based framework. 

This project models the random walk of 10,000 particles undergoing Brownian motion. By introducing a reflecting boundary and gravitational drift, the simulation demonstrates how macroscopic statistical behaviors, like the Boltzmann distribution, emerge from purely random thermal fluctuations.

## Dependencies
This project is built using standard Python and requires the following external libraries:
* **NumPy** (for vectorized particle matrix operations)
* **Matplotlib** (for plotting trajectories and histograms)

## Features
Each part is toggleable to view one or multiple at the same time.
* **Part 1:** Unbound Brownian motion (random walk).
* **Part 2:** Introduction of a reflecting boundary ($h=0$).
* **Part 3:** Addition of gravitational drift to achieve steady-state Boltzmann distribution.