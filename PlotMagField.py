import sys
import numpy as np
import matplotlib.pyplot as plt
import magpylib as mag3

# Magnetic Field Strengths
B0 = 1000
B1 = 1000

y0 = 1.25663706212e-6

# Functions for magnetic Field
def Bpole(X, Y):
    return -B0 * 2 * (1 / r)**3 * np.cos(theta), -B0 * (1 / r)**3 * np.sin(theta)

def Bwire(r1):
    return -B1 * 2 * (1 / r1)**3

# Grid of x, y points on a Cartesian grid
nx, ny = 64, 64
XMAX, YMAX = 40, 40
x = np.linspace(-XMAX, XMAX, nx)
y = np.linspace(0, 2*YMAX, ny)
X, Y = np.meshgrid(x, y)
#r, theta = np.hypot(X, Y), np.arctan2(Y, X)
#r1 = np.hypot(X, Y-50)

# Magnetic field vector, B = (Ex, Ey), as separate components
#Br1, Btheta1 = Bpole(r, theta)
#Br2 = Bwire(r1)

# Transform to Cartesian coordinates: NB make North point up, not to the right.
#c, s = np.cos(np.pi/2 + theta), np.sin(np.pi/2 + theta)
#Bx1 = -Btheta1 * s + Br1 * c
#By1 = Btheta1 * c + Br1 * s
#Bx2 = Br2 * c
#By2 = Br2 * s

# Add magnetic fields
#Bx = Bx1 + Bx2
#By = By1 + By2

m = [0, 1]
i = [1, 0]

mr = m[0] * X + m[1] * Y # dot product m * r
ir = i[0] * X + i[1] * Y # dot product m * i

r_squared = X**2 + Y**2
factor = 1 / ( np.sqrt(r_squared)**5 * 4 * np.pi) # pre factor, that is  multiplied with the vector 

Bx1 = factor * (3 * X * mr - m[0] * r_squared)
By1 = factor * (3 * Y * mr - m[1] * r_squared)

Bx2 = ir /r_squared
By2 = ir /r_squared

# Add magnetic fields
#Bx = Bx1 + Bx2
#By = By1 + By2
#Bx = Bx1
#By = By1
Bx = Bx2
By = By2


# Plot the streamlines with an appropriate colormap and arrow style
fig, ax = plt.subplots()

color = 2 * np.log(np.hypot(Bx, By))
ax.streamplot(x, y, Bx, By, color=color, linewidth=1.2, density=2, arrowstyle='-', arrowsize=1.5)

ax.set_xlim(-XMAX, XMAX)
ax.set_ylim(0, 2*YMAX)
ax.set_aspect('equal')
plt.show()