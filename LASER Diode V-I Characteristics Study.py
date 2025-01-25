import matplotlib.pyplot as plt

# Function to get valid input
def get_input(prompt):
    while True:
        try:
            input_values = input(prompt)
            values = [float(value) for value in input_values.split(',')]
            return values
        except ValueError:
            print("Invalid input! Please enter numeric values separated by commas.")

# User input for voltage and currents
voltage = get_input("Enter Voltage (V) values (separated by commas): ")

# Get current values for different resistances
current_1 = get_input("Enter Current (mA) values for R = 100Ω (separated by commas): ")
current_2 = get_input("Enter Current (mA) values for R = 150Ω (separated by commas): ")
current_3 = get_input("Enter Current (mA) values for R = 220Ω (separated by commas): ")

# Plot the V-I Characteristics for each resistance
plt.figure(figsize=(8, 6))

plt.plot(voltage, current_1, marker='o', linestyle='-', color='b', label='R = 100Ω')
plt.plot(voltage, current_2, marker='s', linestyle='--', color='g', label='R = 150Ω')
plt.plot(voltage, current_3, marker='^', linestyle='-.', color='r', label='R = 220Ω')

# Labels and title
plt.xlabel('Voltage (V)')
plt.ylabel('Current (mA)')
plt.title('V-I Characteristics Graph of LASER Diode')

# Adding a grid and legend
plt.grid(True)
plt.legend()

# Show the plot
plt.show()
