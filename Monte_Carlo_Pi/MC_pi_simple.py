import numpy as np
from matplotlib import pyplot as plt

# Function to calculate pi by comparing if a random x,y pair falls within a
# circle with unit radius.  Return the x,y values and estimated value of pi.
def calc_pi(n):
    x = np.random.rand(n)
    y = np.random.rand(n)
    within = np.less_equal(np.sqrt(x*x+y*y),1.0)
    pi = np.sum(within) / n * 4.0
    relerr = np.sqrt((4/np.pi - 1) / n)
    return(x, y, pi, relerr)

if __name__ == '__main__':

    # Create scatter plot of individual points.
    n = 2500
    x, y, pi, err = calc_pi(n)
    fig = plt.figure()
    
    plt.scatter(x, y, marker='x', color='k')
    
    plt.xlim([0,1])
    plt.ylim([0,1])
    plt.title(r'$\pi$ estimated as {:.5f} using {:d} samples'.format(pi, n))
    plt.axes().set_aspect('equal')
    plt.savefig('plot_simple_MC_pi_points.png')
    plt.show()
    
