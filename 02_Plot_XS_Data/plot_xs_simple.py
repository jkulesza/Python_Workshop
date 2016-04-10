from matplotlib import pyplot as plt
import numpy as np

# Load data from file
E, sig_t, sig_s, sig_a = np.genfromtxt('janis_endfb7_fe-56.csv', delimiter=',',
                                        unpack=True, skip_header=3)

# Create a simple plot of total cross section.
plt.figure()
plt.loglog(E, sig_t)
plt.xlabel('E (eV)')
plt.ylabel('Fe-56 Total Cross Section (barns)')
plt.grid()
plt.savefig('plot_simple_01_janis_endfb7_fe-56_sig_t.png')

# Create a simple plot of total, scattering, and elastic cross sections.
plt.figure()
plt.loglog(E, sig_t, label=r'$\sigma_t$')
plt.loglog(E, sig_s, label=r'$\sigma_s$')
plt.loglog(E, sig_a, label=r'$\sigma_\gamma$')
plt.xlabel('E (eV)')
plt.ylabel('Cross Section (barns)')
plt.legend(loc='best')
plt.grid()
plt.savefig('plot_simple_02_janis_endfb7_fe-56_3on1.png')

# Calculate and plot scattering ratio (sigma_s / sigma_t).
c = sig_s / sig_t
plt.figure()
plt.loglog(E, c)
plt.xlabel('E (eV)')
plt.ylabel('Scattering Ratio, $c$')
plt.grid()
plt.savefig('plot_simple_03_janis_endfb7_fe-56_c.png')

# Show the plots.
plt.show()

