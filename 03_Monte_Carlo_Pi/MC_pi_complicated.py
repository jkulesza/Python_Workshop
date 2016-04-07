import numpy as np
from MC_pi_simple import calc_pi
from matplotlib import pyplot as plt
from scipy import interpolate as interp

################################################################################
# Create scatter plot of individual points, styled by whether they are within or
# outside the circle.
################################################################################
n = 2500
x, y, pi, relerr = calc_pi(n)
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
plt.savefig('plot_complicated_MC_pi_points.png')

################################################################################
# Create 2d histogram (density) plot (manually).
################################################################################
n = 10000
x, y, pi, relerr = calc_pi(n)

H, xp, yp = np.histogram2d(x, y, bins=[10,10])
H = np.ma.masked_where(H == 0, H)
X, Y = np.meshgrid(xp, yp)

fig = plt.figure()
circle = plt.Circle((0,0), 1.0, color='r', linewidth=2.0, fill=False, zorder=0)
fig.gca().add_artist(circle)

plt.pcolormesh(X, Y, H.T, cmap='plasma')
plt.colorbar()

plt.xlim([0,1])
plt.ylim([0,1])
plt.axes().set_aspect('equal')
plt.savefig('plot_complicated_MC_pi_density.png')

################################################################################
# Create density plotting function to easily reproduce plots with common
# styling.  Returns a plot object.
################################################################################
def my2dhist(x, y, title = '', nbins_x = 25, nbins_y = 25):
    H, xp, yp = np.histogram2d(x, y, bins=[nbins_x, nbins_y])
    H = np.ma.masked_where(H == 0, H)
    X, Y = np.meshgrid(xp, yp)

    fig = plt.figure()
    circle = plt.Circle((0,0), 1.0, color='r', linewidth=2.0, fill=False, zorder=0)
    fig.gca().add_artist(circle)

    plt.pcolormesh(X, Y, H.T, cmap='plasma')
    plt.colorbar()

    if(title != ''):
        plt.title(title)
    plt.xlim([0,1])
    plt.ylim([0,1])
    plt.axes().set_aspect('equal')

    return(plt)

################################################################################
# Use the function above to create plots for a variety of sample sizes.
################################################################################
xe2, ye2, pie2, relerre2 = calc_pi(1e2)
xe4, ye4, pie4, relerre4 = calc_pi(1e4)
xe6, ye6, pie6, relerre6 = calc_pi(1e6)

plte2 = my2dhist(xe2, ye2, title=r'$\pi$ estimated as {:.5f} using {:d} samples'.format(pie2, int(1e2)))
plte4 = my2dhist(xe4, ye4, title=r'$\pi$ estimated as {:.5f} using {:d} samples'.format(pie4, int(1e4)))
plte6 = my2dhist(xe6, ye6, title=r'$\pi$ estimated as {:.5f} using {:d} samples'.format(pie6, int(1e6)))

plte2.savefig('plot_complicated_MC_pi_density_1e2_pts.png')
plte4.savefig('plot_complicated_MC_pi_density_1e4_pts.png')
plte6.savefig('plot_complicated_MC_pi_density_1e6_pts.png')

################################################################################
# Create a line plot showing convergence as n increases.
################################################################################

samples = [1e2, 1e3, 1e4, 1e5, 1e6, 1e7]
x   = np.empty(shape=(0))
y   = np.empty(shape=(0))
pi  = np.empty(shape=(0))
err = np.empty(shape=(0))
for n in samples:
    xi, yi, pii, erri = calc_pi(n)
    x = np.append(x, xi)
    y = np.append(y, yi)
    pi = np.append(pi, pii)
    err = np.append(err, erri*pii)

fig = plt.figure()
plt.plot(samples, pi, 'k.-', label='Estimate of $\pi\pm1,2\sigma$')
plt.fill_between(samples, pi-1*err, pi+1*err, color='#000000', alpha=0.1)
plt.fill_between(samples, pi-2*err, pi+2*err, color='#000000', alpha=0.1)
plt.axhline(y=np.pi, linewidth=0.5, color='#000000', linestyle='--', label=r'$\pi$')
plt.xticks(list(plt.xticks()[0]) + [np.pi])
plt.xscale('log')
plt.legend(loc='best')
plt.xlabel('Number Of Samples, $n$')
plt.ylabel(r'Estimated Value Of $\pi\pm2\sigma$ Versus Actual')

plt.savefig('plot_complicted_MC_pi_convergence.png')
plt.show()

