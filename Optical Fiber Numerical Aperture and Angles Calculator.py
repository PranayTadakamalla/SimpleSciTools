import math

# Input: Refractive indices for the core and cladding
n1 = float(input('Enter refractive index of the core (n1): '))
n2 = float(input('Enter refractive index of the cladding (n2): '))

# Calculate the Numerical Aperture (NA)
NA = math.sqrt(n1**2 - n2**2)

# Calculate the Acceptance Angle (ɑ) and convert it to degrees
ɑ = math.asin(NA)

# Calculate the Critical Angle (𝞱) and convert it to degrees
𝞱 = math.asin(n2 / n1)

# Display the results
print(f'\nNumerical Aperture (NA) = {NA:.4f}')
print(f'Acceptance Angle (𝛼) = {math.degrees(ɑ):.2f}°')
print(f'Critical Angle (𝞱) = {math.degrees(𝞱):.2f}°')
