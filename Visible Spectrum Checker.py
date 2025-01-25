# Constants
h = 6.62 * (10**-34)  # Planck's constant in J·s
c = 3 * (10**8)       # Speed of light in m/s
l = 10**(-10)         # Conversion factor for angstroms to meters
j = 6.24 * (10**18)   # Conversion factor for eV to Joules

# User input for energy levels
e1 = float(input('Enter the value of E1 (in eV): '))
e2 = float(input('Enter the value of E2 (in eV): '))

# Calculate the energy difference
e = e2 - e1

# Calculate the wavelength using the formula
wl = (h * c * j) / (e * l)

# Output the wavelength
print(f'\nThe Wavelength corresponding to the energy levels is: {wl:.2f} nm')

# Determine if the wavelength is in the visible spectrum (400 nm to 800 nm)
if 4000 <= wl <= 8000:
    print('It is Visible')
else:
    print('It is Not Visible')
