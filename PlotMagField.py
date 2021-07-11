##########################################################################
# Libraries
##########################################################################
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


##########################################################################
# Inputs
##########################################################################

# Magnetic Field Strengths Multiplocators
B0 = 100
B1 = 10

# Data from openCV
pos = [[-10, 30, 0.9], [0, 50, 1.1]]

# Plotparameters
ny = 64
nx = 64
XMAX = 50
YMAX = 80


##########################################################################
# Functions
##########################################################################

# Functions for magnetic Fields
def Bpole(X, Y):
    m = [0, 1]
    mr = m[0] * X + m[1] * Y 
    r = np.sqrt(X**2 + Y**2)
    mag = B0 / r**5
    bx = mag * (3 * X * mr - m[0] * r**2)
    by = mag * (3 * Y * mr - m[1] * r**2)
    return bx, by

def Bwire(X, Y, pos, k):
    Xtrans = X - pos[0]
    Ytrans = Y - pos[1]
    r = np.sqrt((Xtrans)**2+(Ytrans)**2)
    mag = (k * B1) / (r**3)
    bx = mag * (np.cos(np.arctan2(Xtrans,Ytrans)))
    by = mag * (-np.sin(np.arctan2(Xtrans,Ytrans)))                                
    return bx, by

# Calculate Added Vector Field
def Bfield(pos):
    n = len(pos)
    Bx, By = Bpole(X, Y)
    for i in range(0, n):
        BwireX, BwireY = Bwire(X, Y, [pos[i][0], pos[i][1]], pos[i][2])
        Bx = Bx + BwireX
        By = By + BwireY
    #i = 0
    return Bx, By

# Grid of x, y points on a Cartesian grid
def meshgrid(nx, ny, XMAX, YMAX):
    x = np.linspace(-XMAX, XMAX, nx)
    y = np.linspace(0, YMAX, ny)
    X, Y = np.meshgrid(x, y)
    return X, Y


##########################################################################
# Setup
##########################################################################

# Create Meshgrid
X, Y = meshgrid(nx, ny, XMAX, YMAX)

# Create Plot
fig, ax = plt.subplots()
Bx, By = Bfield(pos)
ax.streamplot(X, Y, Bx, By, color='black', linewidth=1.2, density=2, arrowstyle='-', arrowsize=1.5)  

# Plot Styling
#plt.style.use('dark_background')
ax.set_xlim(-XMAX, XMAX)
ax.set_ylim(0, YMAX)
ax.set_aspect('equal')

plt.show()

#Animation
#ani = FuncAnimation(fig, update, interval=50, blit=False)