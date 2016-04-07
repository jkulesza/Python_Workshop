import numpy as np


# Calculate pi by comparing if a random x,y pair falls within a circle with unit
# radius.  Return the x,y values and estimated value of pi.
def calc_pi(n):
    x = np.random.rand(n)
    y = np.random.rand(n)
    within = np.less_equal(np.sqrt(x*x+y*y),1.0)
    pi = np.sum(within) / n * 4.0
    return(x,y,pi)

# Create plots.
from matplotlib import pyplot as plt

# Create scatter plot of individual points, styled by whether they are within or
# outside the circle.
n = 2500
x, y, pi = calc_pi(n)
fig = plt.figure()
circle = plt.Circle((0,0), 1.0, color='r', linewidth=2.0, fill=False, zorder=0)
fig.gca().add_artist(circle)

x_in = np.ma.masked_where(x*x + y*y < 1.0, x)
y_in = np.ma.masked_where(x*x + y*y < 1.0, y)
x_out = np.ma.masked_where(x*x + y*y > 1.0, x)
y_out = np.ma.masked_where(x*x + y*y > 1.0, y)

plt.scatter(x_in, y_in, marker='x', color='k')
plt.scatter(x_out, y_out, marker='.', color='k')

plt.xlim([0,1])
plt.ylim([0,1])
plt.title(r'$\pi$ estimated as ' + '{:.5f}'.format(pi) + ' using ' + str(n) + ' points')
plt.axes().set_aspect('equal')
plt.savefig('plot_MC_pi.png')
plt.show() 

# Create density plot 
n = 10000
x, y, pi = calc_pi(n)
fig = plt.figure()
circle = plt.Circle((0,0), 1.0, color='r', linewidth=2.0, fill=False, zorder=0)
fig.gca().add_artist(circle)

plt.scatter(x_in, y_in, marker='x', color='k')
plt.scatter(x_out, y_out, marker='.', color='k')

plt.xlim([0,1])
plt.ylim([0,1])
plt.axes().set_aspect('equal')
plt.savefig('plot_MC_pi.png')
plt.show() 

#
