import math

# Welcome message
print("Welcome to the Energy Band Gap Calculator!")
print("This program calculates the Energy Band Gap of a semiconductor based on the given parameters.")

# User input for temperature and current
Tc = float(input("\nEnter the value of Temperature (in ℃): "))
Is = float(input("Enter the value of Current (in μA): "))

# Convert temperature to Kelvin
Tk = Tc + 273

# Slope calculation
Slope = math.log10(Is * (10 ** -6)) / (1000 / Tk)

# Energy band gap calculation
Eg = 0.198 * Slope

# Display the result in a clear and formatted way
print("\n--------------------------------------------")
print(f"Energy Band Gap of Semiconductor = {Eg:.6f} eV")
print("--------------------------------------------")
print("\nNote: The Energy Band Gap value indicates the energy difference between the conduction band and the valence band.")
print("Thank you for using the Energy Band Gap Calculator!")
