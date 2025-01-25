import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.backends.backend_pdf import PdfPages

# Temperature values (in Celsius) and corresponding Is values
Tc = np.array([75, 70, 65, 60, 55, 50, 45, 40, 35])
Tk = [x + 273 for x in Tc]  # Convert Celsius to Kelvin
Is = np.array([29, 25, 23, 22, 21, 21, 20, 19, 18])

# Calculate x = 1000/T and y = log10(Is)
x = [1000 / t for t in Tk]
y = [math.log10(i * (10**-6)) for i in Is]

# Perform linear fit
f = np.polyfit(x, y, 1)
slope = f[0]

# Plot the data and linear fit
plt.figure(figsize=(8, 6))  # Increase figure size for better visibility
plt.scatter(x, y, label='Experimental Data', color='b', marker='o', edgecolor='black', s=100)
plt.plot(x, np.polyval(f, x), label='Linear Fit', color='r', linewidth=2)

# Add grid, labels, and title
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.xlabel('1000/T (1/K)', fontsize=12)
plt.ylabel('Log10(Is) (Log scale)', fontsize=12)
plt.title('Linear Fit of Experimental Data for Energy Band Gap', fontsize=14)

# Calculate the energy band gap
Eg = 0.198 * slope
print("Slope of the linear fit: ", slope)
print('Energy Band Gap of Semiconductor =', Eg)

# Show the plot
plt.show()

# Save the plot to PDF if the user wants it
while True:
    dwn = input('Want to download graph (yes/no): ')
    if dwn == 'yes':
        with PdfPages('Linear Fit of Experimental Data.pdf') as pdf:
            pdf.savefig()
        print('Please check the directory, where you open this file')
        break
    elif dwn == 'no':
        break
    else:
        print('Please Select (yes/no): ')
