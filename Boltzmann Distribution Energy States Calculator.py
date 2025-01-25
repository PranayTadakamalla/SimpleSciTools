import math

# Welcome message
print("Welcome to the Relative Population Calculator!")
print("This program calculates the relative population of two states based on the given parameters.")

# User input for wavelength and temperature
wl = float(input("\nEnter the value of Wavelength (in Å): "))
t = float(input("Enter the value of Temperature (in K): "))

# Constants
h = 6.62 * (10 ** -34)  # Planck's constant (in Joules * seconds)
c = 3 * (10 ** 8)       # Speed of light (in meters per second)
k = 1.38 * (10 ** -23)  # Boltzmann constant (in Joules per Kelvin)
l = 10 ** -10           # Conversion factor (in meters)

# Energy calculation
e = (h * c) / (wl * l)

# Boltzmann factor
x = e / (k * t)

# Relative population using Boltzmann distribution
n = math.e ** (-x)

# Display the result in a more readable way
print("\n--------------------------------------------")
print(f"The relative population of the two states is: {n:.6e}")
print("--------------------------------------------")
print("\nNote: A higher value indicates a greater population of the lower energy state.")
print("Thank you for using the Relative Population Calculator!")
