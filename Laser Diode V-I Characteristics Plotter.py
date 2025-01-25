import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Data for voltage and current
volt = [0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0]

# Current data for different resistances
l1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0.3, 1.1, 2.1, 3.1, 4.1, 5.2, 6.2, 7.3, 8.3, 9.4, 10.5, 11.6]
l2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0.3, 0.9, 1.7, 2.5, 3.3, 4.1, 4.9, 5.7, 6.6, 7.4, 8.3, 9.1]
l3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0.2, 0.7, 1.3, 1.9, 2.5, 3.2, 3.8, 4.4, 5.1, 5.7, 6.4, 7.0]

# Plotting the V-I characteristics for each resistance
plt.figure(figsize=(8, 6))

plt.plot(volt, l1, label="100 Ω", color="blue", marker='o')
plt.plot(volt, l2, label="150 Ω", color="green", marker='s')
plt.plot(volt, l3, label="200 Ω", color="red", marker='^')

# Setting plot limits
plt.xlim(0, 4.4)
plt.ylim(0, 12.5)

# Adding labels and title
plt.xlabel('Voltage (V)')
plt.ylabel('Current (mA)')
plt.title('V-I Characteristics of Laser Diode')

# Displaying the legend
plt.legend()

# Display the plot
plt.show()

# Prompt the user if they want to download the graph
while True:
    dwn = input('Do you want to download the graph as a PDF (yes/no)? ').strip().lower()
    if dwn == 'yes':
        with PdfPages('V-I_Characteristics_of_Laser_Diode.pdf') as pdf:
            # Save the current figure to the PDF file
            pdf.savefig()
            plt.close()  # Close the figure to prevent memory overload
        print('Graph has been saved as "V-I_Characteristics_of_Laser_Diode.pdf" in the current directory.')
        break
    elif dwn == 'no':
        print('Graph not saved.')
        break
    else:
        print('Please enter "yes" or "no".')
