import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# Magnetic Field Strengths
B0 = 100
B1 = 10

pos1 = [-10, 30]
pos2 = [0, 50]

# Functions for magnetic Field
def Bpole(X, Y):
    m = [0, 1]
    mr = m[0] * X + m[1] * Y 
    r = np.sqrt(X**2 + Y**2)
    mag = B0 / r**5
    bx = mag * (3 * X * mr - m[0] * r**2)
    by = mag * (3 * Y * mr - m[1] * r**2)
    return bx, by

def Bwire(X, Y, pos):
    Xtrans = X - pos[0]
    Ytrans = Y - pos[1]
    r = np.sqrt((Xtrans)**2+(Ytrans)**2)
    mag = B1 / r**3
    bx = mag * (np.cos(np.arctan2(Xtrans,Ytrans)))
    by = mag * (-np.sin(np.arctan2(Xtrans,Ytrans)))                                
    return bx, by

# Grid of x, y points on a Cartesian grid
nx, ny = 64, 64
XMAX, YMAX = 40, 40
x = np.linspace(-XMAX, XMAX, nx)
y = np.linspace(0, 2*YMAX, ny)
X, Y = np.meshgrid(x, y)

#Calculate Vectors
BpoleX, BpoleY = Bpole(X, Y)
Bwire1X, Bwire1Y = Bwire(X, Y, pos1)
Bwire2X, Bwire2Y = Bwire(X, Y, pos2)

# Add magnetic fields
Bx = -(BpoleX + Bwire1X + Bwire2X)
By = -(BpoleY + Bwire1Y + Bwire2Y)

# Plot the streamlines with an appropriate colormap and arrow style
fig, ax = plt.subplots()
#plt.style.use('dark_background')
print(matplotlib.__version__)

#Polt Style
ax.streamplot(x, y, Bx, By, color='black', linewidth=1.2, density=2, arrowstyle='-', arrowsize=1.5)

ax.set_xlim(-XMAX, XMAX)
ax.set_ylim(0, 2*YMAX)
ax.set_aspect('equal')
plt.show()