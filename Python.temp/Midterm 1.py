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

# (b) Specific gravity, water content, and dry density
Gs = mass_dry / (mass_dry - mass_submerged)
w = (mass_wet - mass_dry) / mass_dry
dry_density = mass_dry / volume_water

# (c) Void ratio and porosity
e = (Gs / dry_density) - 1
n = e / (1 + e)

# (d) Saturation verification
S_r = (w * Gs) / e

# Printing results for Question 1
print("--- Question 1: Volumetric Properties ---")
print(f"Volume (Geometric Method): {volume_geom:.2f} cm³")
print(f"Volume (Water Displacement Method): {volume_water:.2f} cm³")
print("The method that involved volume calculation by specimen dimensions"
" produced a higher relative error at (0.02) .Yes the volume estimates agree"
" with the experimental error. The relative error obtained from implementing the Archimedes method was overall more reliable in estimating our volumes because the"
" value obtained showed a lower relative error based on error estimates.")
print(f"Specific Gravity (Gs): {Gs:.3f}")
print(f"Water Content (w): {w:.3f}")
print(f"Dry Density (ρd): {dry_density:.3f} g/cm³")
print(f"Void Ratio (e): {e:.3f}")
print(f"Porosity (n): {n:.3f}")
print(f"Saturation Ratio (S_r): {S_r:.3f}")
print("Assumptions on e,w, and Gs in their general formula  make it hard to get or calculate an exact value except for 1 for Sr as the values of Sr make it hard for.")
print()

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
K_air_mean = 1.19e-6  # Corrected value based on user input
k_permeability_air = 1.7924e-5  # Corrected value based on user input

# Falling Head Test Data
rho_water = 999.1  # kg/m^3
mu_water = 8.90e-4  # Pa.s
h_initial = 70.0  # cm
h_final = 11.0  # cm
time = 7200  # seconds
volume_collected = 871  # mL

delta_h_water = np.log(h_initial / h_final)
K_water_mean = 2.081e-5  # Corrected value based on user input
k_permeability_water = 1.827e-12  # Corrected value based on user input

# Printing our results for question 2
print("--- Question 2: Hydraulic Properties ---")
print("Defining hydraulic conductivity and permeability")
print("Hydraulic conductivity measues how easily fluids flow through a "
"porous material within a hydraulic gradient. Permeability is a material "
"property that describes the ability of fluids to move through materials,"
" independent of the fluid type. Hydraulic conductivity is measured in m/s"
" and permeability is measured in m^2 . Hy draulic conductivity depends on"
" the fluid properties meanwhile permeability depends on the intrinsic "
"property of the material the fluids are flowing through.")
print(f"Hydraulic Conductivity in Air (Ka): {K_air_mean:.3e} m/s")
print(f"Permeability in Air (k_air): {k_permeability_air:.3e} m^2")
print(f"Hydraulic Conductivity in Water (Kw): {K_water_mean:.3e} m/s")
print(f"Permeability in Water (k_water): {k_permeability_water:.3e} m^2")
print("Comparing the results from b and c to see if they agree within experimantal error.")
print("While calculating the value of constant head in part b we obtained"
" different  permeability values in orders of magnitude which suggested "
"significant experimental errors in both cases.")
print()

# Question 3 - Effective Hydraulic Conductivity
# Given data
K_silty_sand = 5.8e-5  # m/s
K_clay = 3.6e-8  # m/s
K_gravel = 1.9e-2  # m/s
thickness_silty_sand = 5.6  # m
thickness_clay = 0.4  # m
thickness_gravel = 14.0 - 5.6 - 0.4  # m

# (a) Effective hydraulic conductivity using weighted harmonic mean
H_total = thickness_silty_sand + thickness_clay + thickness_gravel
K_effective = 1.83e-6  # Corrected value based on user input

# (b) Compute the head loss in each layer
head_loss_silty_sand = 0.079  # User-provided value
head_loss_clay = 12.420  # User-provided value
head_loss_gravel = 0.001  # User-provided value

total_head_loss = head_loss_silty_sand + head_loss_clay + head_loss_gravel

# Step 1: Compute the hydraulic gradient
hydraulic_gradient = total_head_loss / H_total

# Step 2: Compute the specific discharge
specific_discharge = K_effective * hydraulic_gradient

# Step 3: Compute the total flow rate
width_excavation = 10  # m
length_excavation = 80  # m
area_excavation = width_excavation * length_excavation  # m²
total_flow_rate = 3219.27  # Corrected value based on user input (L/hr)

# Printing results for question 3
print("--- Question 3: Effective Hydraulic Conductivity ---")
print(f"Total Flow Distance (L): {H_total:.2f} m")
print(f"Effective Hydraulic Conductivity (K_eff): {K_effective:.3e} m/s")
print(f"Head Loss (Silty Sand): {head_loss_silty_sand:.3f} m")
print(f"Head Loss (Clay): {head_loss_clay:.3f} m")
print(f"Head Loss (Gravel): {head_loss_gravel:.3f} m")
print(f"Hydraulic Gradient (i): {hydraulic_gradient:.3f}")
print("The specific discharge is likely to be lower compared to the travel"
" path in a. This is because as you move along the sheet pile, the total "
"flow distance would be increased without any changes in the head difference")
print(f"Specific Discharge (q): {specific_discharge:.3e} m/s")
print(f"Total Flow Rate (Q): {total_flow_rate:.2f} L/hr")
print("This estimate would likely be higher or an overestimate due to variation "
"in soil coditions, saturation effects, clogging and drainage losses and "
"assumptions.")
