import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D 

# Global consts for fluid flow (included in Lorenz equations)
prandtl_number = 10 # AKA. sigma in certain texts, ratio of momentum diffusivity and thermal diffusivity
rayleigh_number = 28 # it is the measure of instability in a fluid, mainly caused by convection
beta = 2.667 # abs(8/3) measure of compressibility of a fluid ( relative volume change )
dt = 100 # max time point
steps = 10000 # total no of time points
# refer "https://mathworld.wolfram.com/LorenzAttractor.html" for complete formulaic breakdown
def lorenzAttractorGenerator(X, t):
    # This method of fluid movement, essentially assumes that the fluid is cooled from below and heated from above
    x, y, z = X
    xBar = -prandtl_number * (x - y)
    yBar = rayleigh_number * x - y - x*z
    zBar = -beta*z + x*y 
    print(xBar, yBar, zBar)
    return xBar, yBar, zBar

if __name__ == "__main__":
   
    t = np.linspace(0, dt, steps)
    f = odeint(lorenzAttractorGenerator, (0, 1, 1.05), t) # solving the differential equation output using odeint
    x, y, z = f.T

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    s = 10
    c = np.linspace(0,1,steps)
    for i in range(0,steps-s,s):
        ax.plot(x[i:i+s+1], y[i:i+s+1], z[i:i+s+1], color=(1,c[i],0), alpha=0.4)

    ax.set_axis_off()
    plt.show()
    
    """
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    s = 10
    c = np.linspace(0,1,n)
    for i in range(0,n-s,s):
    ax.plot(x[i:i+s+1], y[i:i+s+1], z[i:i+s+1], color=(1,c[i],0), alpha=0.4)
    ax.plot(xArr, yArr, zArr, lw=0.5)
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    ax.set_title("Lorenz Attractor")
    plt.show()
    """

    pass



