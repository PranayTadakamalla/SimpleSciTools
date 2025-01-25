import math

# Constants
N = 2500 / 2.54  # Number of lines per cm (converted from lines per inch)

# Input: Distance between screen and grating
d = float(input('Enter the distance between Screen and Grating (in cm): '))

# Orders for the maxima
n = [1, 2, 3]

# Loop to calculate and display the wavelength for each order
for i in range(3):
    # Input: Distance between corresponding maxima for the given order
    x2 = float(input(f'Enter the distance between Corresponding Maxima of Order {n[i]} (in cm): '))
    
    # Calculate x (half the distance between maxima)
    x = x2 / 2
    
    # Calculate sin(theta)
    sin𝞱 = x / math.sqrt(x**2 + d**2)
    
    # Calculate the wavelength
    λ = (sin𝞱 * 10**8) / (N * n[i])
    
    # Output the result for the current order
    print(f'Wavelength of Laser Beam for Order {n[i]} = {λ:.2f} nm')

