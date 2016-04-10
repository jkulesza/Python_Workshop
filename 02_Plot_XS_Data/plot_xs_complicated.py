from matplotlib import pyplot as plt
from matplotlib import cm, colors, ticker, rc
import numpy as np
import pylab

# Set plot aspect ratio to 'the golden ratio' and control plot font/size to
# conform nicely the appearance of a typical LaTeX document.
#
# The colorscheme for lines / points has been redefined using a colorbrewer2.org
# qualitative 8-class palette.
fig_width     = 6.5
golden_ratio  = (np.sqrt(5)-1.0)/2.0
fig_height    = fig_width*golden_ratio
fig_size      =  [fig_width,fig_height]
fig_font_size = 10

params        = { 'axes.labelsize'   : 10,
                  'axes.linewidth'   : 0.5,
                  'axes.titlesize'   : 10,
                  'backend'          : 'ps',
                  'figure.dpi'       : 300,
                  'figure.figsize'   : fig_size,
                  'font.family'      : 'serif',
                  'font.serif'       : ['Computer Modern'],
                  'font.size'        : fig_font_size,
                  'legend.fontsize'  : 0.8*fig_font_size,
                  'lines.linewidth'  : 0.5,
                  'lines.markersize' : 2,
                  'savefig.dpi'      : 600,
                  'savefig.bbox'     : 'tight',
                  'text.usetex'      : True,
                  'xtick.labelsize'  : 0.8*fig_font_size,
                  'ytick.labelsize'  : 0.8*fig_font_size,
                  'axes.color_cycle' : ['#1f78b4',
                                        '#33a02c',
                                        '#ff7f00',
                                        '#e31a1c',
                                        '#a6cee3',
                                        '#b2df8a',
                                        '#fdbf6f',
                                        '#fb9a99'] 
}

pylab.rcParams.update(params)

################################################################################

# Load data from file
E, sig_t, sig_s, sig_a = np.genfromtxt('janis_endfb7_fe-56.csv', delimiter=',',
                                        unpack=True, skip_header=3)

# Create a figure with three cross sections displayed using separate axes.
fig, (ax0, ax1, ax2) = plt.subplots(nrows=3) 

ax0.loglog(E, sig_t)
ax1.loglog(E, sig_s)
ax2.loglog(E, sig_a)

ax0.set_xlabel(r'Energy, $E$ (eV)')
ax1.set_xlabel(r'Energy, $E$ (eV)')
ax2.set_xlabel(r'Energy, $E$ (eV)')

ax0.set_ylabel(r'$^{56}$Fe $\sigma_t$ (barns)')
ax1.set_ylabel(r'$^{56}$Fe $\sigma_\gamma$ (barns)')
ax2.set_ylabel(r'$^{56}$Fe $\sigma_a$ (barns)')
 
ax0.grid()
ax1.grid()
ax2.grid()

fig.tight_layout()
plt.savefig('plot_complicated_01_janis_endfb7_fe-56_3up.png')

# Create a figure with three cross sections displayed using separate axes but
# with shared x-axes.
fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, sharex=True) 

ax0.plot(E, sig_t)
ax1.plot(E, sig_s)
ax2.plot(E, sig_a)

# Explicitly set axis scaling.
ax0.set_xscale('log')
ax1.set_xscale('log') # Redundant
ax2.set_xscale('log') # Redundant

ax0.set_yscale('log')
ax1.set_yscale('log')
ax2.set_yscale('log')

ax2.set_xlabel(r'Energy, $E$ (eV)')

ax0.set_ylabel(r'$^{56}$Fe $\sigma_t$ (barns)')
ax1.set_ylabel(r'$^{56}$Fe $\sigma_\gamma$ (barns)')
ax2.set_ylabel(r'$^{56}$Fe $\sigma_a$ (barns)')
 
ax0.grid()
ax1.grid()
ax2.grid()

fig.tight_layout()
plt.savefig('plot_complicated_01_janis_endfb7_fe-56_3up_sharedx.png')
 
# Create a figure with three cross sections displayed using separate axes but
# with shared x- and y-axes.
fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, sharex=True, sharey=True) 

ax0.plot(E, sig_t)
ax1.plot(E, sig_s)
ax2.plot(E, sig_a)

# Explicitly set axis scaling.
ax0.set_xscale('log')
ax1.set_xscale('log') # Redundant
ax2.set_xscale('log') # Redundant

ax0.set_yscale('log')
ax1.set_yscale('log') # Redundant
ax2.set_yscale('log') # Redundant

ax2.set_xlabel(r'Energy, $E$ (eV)')

ax0.set_ylabel(r'$^{56}$Fe $\sigma_t$ (barns)')
ax1.set_ylabel(r'$^{56}$Fe $\sigma_\gamma$ (barns)')
ax2.set_ylabel(r'$^{56}$Fe $\sigma_a$ (barns)')
 
ax0.grid()
ax1.grid()
ax2.grid()

fig.tight_layout()
plt.savefig('plot_complicated_01_janis_endfb7_fe-56_3up_sharedx.png')
 




plt.show() 


