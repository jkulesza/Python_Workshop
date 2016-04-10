from matplotlib import pyplot as plt
import numpy as np

# Load data from file
E, mt103 = np.genfromtxt('janis_irdf-2002_MG_ni-58.csv', delimiter=',', unpack=True, skip_header=3)

# Create several histogram plots using "steps."  Note that the display mode
# 'post' gives the correct appearance (compare with the plot from JANIS).
plt.figure()
plt.step(E, mt103, 'r-', where='pre',  label='pre, default')
plt.step(E, mt103, 'g-', where='post', label='post') 
plt.step(E, mt103, 'b-', where='mid',  label='mid')
plt.xlabel('E (eV)')
plt.ylabel('Ni-58 (n,p) Microscopic Cross Section (barns)')
plt.title('Histogram Plotting Styles')
plt.xlim((E.min(), E.max()))
plt.xscale('log')
plt.yscale('log')
plt.grid()
plt.legend(loc='best')
plt.savefig('plot_ni-58_mt103.png')

# Show the plots.
plt.show()

