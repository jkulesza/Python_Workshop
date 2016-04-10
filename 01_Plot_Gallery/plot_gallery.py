from matplotlib import pyplot as plt
import numpy as np

################################################################################
# Create data.
################################################################################
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
y1 = np.sin(x - 1 * np.pi / 4)
y2 = np.sin(x - 2 * np.pi / 4)
y3 = np.sin(x - 3 * np.pi / 4)
y4 = np.sin(x - 4 * np.pi / 4)
y5 = np.sin(x - 5 * np.pi / 4)
y6 = np.sin(x - 6 * np.pi / 4)
y7 = np.sin(x - 7 * np.pi / 4)
 
################################################################################
# Most simple plot.
################################################################################
plt.figure()
plt.plot(x, y)
plt.savefig('plot_most_simple.png') 

################################################################################
# Add axis labels.
################################################################################
plt.figure()
plt.plot(x, y)

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot Of sin(x)')
plt.savefig('plot_axis_labels.png') 

################################################################################
# Create different plot styles using Mablab styling.
################################################################################
plt.figure()
plt.plot(x, y, 'k-')
plt.plot(x, y1, 'k--')
plt.plot(x, y2, 'k-.')
plt.plot(x, y3, 'k:')
plt.plot(x, y4, 'r.')
plt.plot(x, y5, 'go')
plt.plot(x, y6, 'b^')
plt.plot(x, y7, 'cx')
plt.plot(x, y7, 'g+')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot Of sin(x) Using Various Styles') 
plt.savefig('plot_plot_styles.png') 

################################################################################
# Create different plot styles using explicit styling & HEX color codes.
################################################################################
plt.figure()
plt.plot(x, y, color='#000000', linestyle='-')
plt.plot(x, y1, color='#ff0000', ls='-', linewidth=0.5)
plt.plot(x, y2, color='#00ff00', ls='-', lw=0.5, marker='o')
plt.plot(x, y3, color='#0000ff', ls='-', lw=0.5, marker='o', markersize=3)
plt.plot(x, y4, color='#0000ff', ls='-', lw=0.5, marker='o', ms=3, markerfacecolor='#ff0000')
plt.plot(x, y5, color='#0000ff', ls='-', lw=0.5, marker='o', ms=3, mfc='#ff0000', markeredgewidth=0)
plt.plot(x, y6, color='#0000ff', ls='-', lw=0.5, marker='o', ms=3, mfc='#ff0000', mew=0)

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot Of sin(x) Using Various Styles') 
plt.savefig('plot_plot_style_keywords.png') 

################################################################################
# Plot labeling & annotation.
################################################################################
plt.figure()
plt.plot(x, y, color='#000000', linestyle='-', label='sin(x)') 
plt.plot(x, y4, color='#000000', linestyle='--', label='sin(x-pi)') 

plt.annotate('Maximum', xy=(np.pi/2,1), xytext=(2,0.5), 
                arrowprops=dict(facecolor='black'))

lgd = plt.legend(loc='upper right', ncol=1)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot Of sin(x) With Annotation') 
plt.savefig('plot_labels_annotation.png') 

################################################################################
# Plot saving options.
################################################################################
plt.figure()
plt.plot(x, y, color='#000000', linestyle='-', label='sin(x)') 
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot Of sin(x) Using Various Output Options') 
plt.savefig('plot_sin_save_default.png') 
plt.savefig('plot_sin_save_300_dpi.png', dpi=300) 
plt.savefig('plot_sin_save_300_dpi_tight.png', dpi=300, bbox_inches='tight') 
plt.savefig('plot_sin_save_300_dpi_tight.pdf', dpi=300, bbox_inches='tight') 

# Notes:
#
# 1. Tightening the border with the bbox_inches argument can help remove 
#    unneeded whitespace; however, this can clip elements outside of the plot 
#    such as axis labels, legends, etc.  As such, be sure to examine plots to 
#    ensure that all peripheral elements are present.  If this approach cannot
#    be made to work, using external tools to automatically crop the images
#    can be more straightforward (e.g., mogrify -trim image.png from the 
#    ImageMagick suite of tools).
#
# 2. Note that we adjust the image resolution (dots per inch --- dpi) to 
#    increase the image size.  This provides a benefit whereby images can be 
#    made large on a printed page without appearing pixelated.  Alternatively,
#    we generated a PDF file, which is a "vector" format, which allows for 
#    unlimited scaling.  However, a caution: plotting *very* detailed data
#    (such as nuclear cross sections) with PDF or other vector formats can lead 
#    to large files.
#

################################################################################
# Show the plots.
################################################################################
plt.show()
 
