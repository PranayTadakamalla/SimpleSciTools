import math

# User input for refractive indices, diameter, and wavelength
n1 = float(input('Enter the refractive index of the core (n1): '))
n2 = float(input('Enter the refractive index of the cladding (n2): '))
d = float(input('Enter the diameter of the core (in micrometers, µm): '))
l = float(input('Enter the wavelength of light (in micrometers, µm): '))

# Calculate the Numerical Aperture (NA)
NA = math.sqrt(n1**2 - n2**2)

# Calculate the velocity (v) of light in the fiber
v = (d * math.pi * NA) / l

# Calculate the number of modes in the step-index fiber (SIF)
modes = (v**2) / 2

# Output the results with clear explanations
print(f'\nNumerical Aperture (NA) = {NA:.4f}')
print(f'Velocity of light in fiber (v) = {v:.2f} µm/s')
print(f'Number of modes in the Step-Index Fiber (SIF) = {modes:.2f}')
