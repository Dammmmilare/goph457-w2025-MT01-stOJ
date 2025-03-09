import numpy as np

# Constants for Question 1
mass_submerged = 332.1  # g
mass_wet = 537.3  # g
mass_dry = 530.9  # g
diameter = 5.16  # cm
height = 9.87  # cm
density_water = 1.0  # g/cm^3

# (a) Volume calculations
radius = diameter / 2  # cm
volume_geom = np.pi * radius**2 * height  # Geometric volume in cm^3
volume_water = (mass_wet - mass_submerged) / density_water  # Loss of mass in water method

# Errors
error_diameter = 0.05  # cm
error_height = 0.05  # cm
error_mass = 0.2  # g

# Error propagation
error_volume_geom = volume_geom * np.sqrt((2 * error_diameter / diameter)**2 + (error_height / height)**2)
error_volume_water = volume_water * np.sqrt((2 * error_mass / (mass_wet - mass_submerged))**2)

# Relative errors
relative_error_geom = error_volume_geom / volume_geom
relative_error_water = error_volume_water / volume_water

# (b) Specific gravity, water content, and dry density
Gs = mass_dry / (mass_dry - mass_submerged)
error_Gs = Gs * np.sqrt((error_mass / mass_dry)**2 + (error_mass / (mass_dry - mass_submerged))**2)

w = (mass_wet - mass_dry) / mass_dry
error_w = w * np.sqrt((error_mass / (mass_wet - mass_dry))**2 + (error_mass / mass_dry)**2)

dry_density = mass_dry / volume_water
error_dry_density = dry_density * np.sqrt((error_mass / mass_dry)**2 + (error_volume_water / volume_water)**2)

# (c) Void ratio and porosity
e = (Gs / dry_density) - 1
error_e = e * np.sqrt((error_Gs / Gs)**2 + (error_dry_density / dry_density)**2)

n = e / (1 + e)
error_n = error_e / (1 + e)**2

# (d) Saturation verification
S_r = (w * Gs) / e

# Printing results
print(f"Volume (Geometric Method): {volume_geom:.2f} ± {error_volume_geom:.2f} cm^3")
print(f"Volume (Water Displacement Method): {volume_water:.2f} ± {error_volume_water:.2f} cm^3")
print(f"Specific Gravity (Gs): {Gs:.3f} ± {error_Gs:.3f}")
print(f"Water Content (w): {w:.3f} ± {error_w:.3f}")
print(f"Dry Density (ρd): {dry_density:.3f} ± {error_dry_density:.3f} g/cm^3")
print(f"Void Ratio (e): {e:.3f} ± {error_e:.3f}")
print(f"Porosity (n): {n:.3f} ± {error_n:.3f}")
print(f"Saturation Ratio (S_r): {S_r:.3f}")

# Question 2 - Hydraulic Properties
# Given data
diameter_specimen = 6.0  # cm
height_specimen = 15.0  # cm
rho_air = 1.225  # kg/m^3
mu_air = 1.81e-5  # Pa.s
g = 9.81  # m/s^2

pressures = np.array([25, 50, 75, 100]) * 1e3  # Convert kPa to Pa
flow_rates = np.array([4.78e1, 9.49e1, 1.34e2, 1.87e2])  # cm^3/s

delta_h = pressures / (rho_air * g)  # Convert pressure to head difference (m)
K_air = flow_rates / delta_h  # Hydraulic conductivity in air (cm/s)
K_air_mean = np.mean(K_air)

k_permeability = K_air_mean * mu_air / (rho_air * g)  # Permeability (m^2)

# Falling Head Test Data
rho_water = 999.1  # kg/m^3
mu_water = 8.90e-4  # Pa.s
h_initial = 70.0  # cm
h_final = 11.0  # cm
time = 7200  # seconds
volume_collected = 871  # mL

delta_h_water = np.log(h_initial / h_final)
K_water = (volume_collected / (np.pi * (diameter_specimen / 2) ** 2 * time)) * delta_h_water  # cm/s
K_water_mean = np.mean(K_water)

k_permeability_water = K_water_mean * mu_water / (rho_water * g)  # Permeability (m^2)

# Printing results
print(f"Hydraulic Conductivity in Air (Ka): {K_air_mean:.3e} cm/s")
print(f"Permeability (k) from Air Test: {k_permeability:.3e} m^2")
print(f"Hydraulic Conductivity in Water (Kw): {K_water_mean:.3e} cm/s")
print(f"Permeability (k) from Water Test: {k_permeability_water:.3e} m^2")

# Question 3 - Effective Hydraulic Conductivity
# Given data
K_silty_sand = 5.8e-5  # m/s
K_clay = 3.6e-8  # m/s
K_gravel = 1.9e-2  # m/s
thickness_silty_sand = 5.6  # m
thickness_clay = 0.4  # m
thickness_gravel = 14.0 - 5.6 - 0.4  # m

# Effective hydraulic conductivity using weighted harmonic mean
H_total = thickness_silty_sand + thickness_clay + thickness_gravel
K_effective = H_total / (thickness_silty_sand / K_silty_sand + thickness_clay / K_clay + thickness_gravel / K_gravel)

# (b) Specific discharge and hydraulic gradient
hydraulic_gradient = 14.0 / H_total  # Assuming a total head drop of 14m
specific_discharge = K_effective * hydraulic_gradient

# (c) Total flow rate
width_excavation = 10  # m
length_excavation = 80  # m
total_flow_rate = specific_discharge * width_excavation * length_excavation * 3600  # Convert m^3/s to L/hr

# Printing results
print(f"Effective Hydraulic Conductivity (K_eff): {K_effective:.3e} m/s")
print(f"Hydraulic Gradient: {hydraulic_gradient:.3f}")
print(f"Specific Discharge: {specific_discharge:.3e} m/s")
print(f"Total Flow Rate: {total_flow_rate:.2f} L/hr")
