import numpy as np
import csv
import math
import pandas as pd
import seaborn as sns
import matplotlib as plt
from collections import namedtuple

def intometer(x):
    return x*0.0254

# Dictionary to hold the constants
constants = {}
#constants_file = 'src/ramses_constants.csv'
constants_file = 'src/bens_validation_data/UofT_Deliverance_II/UofT_Deliverance_Constants.csv'


# Reading the CSV file
with open(constants_file, mode='r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        # Assuming the columns are named 'Variable', 'Value', and 'Comment'
        var_name = row['Variable']
        value = row['Value']
        
        # Convert numeric values from strings
        try:
            # This tries to convert value to a float if possible
            value = float(value)
        except ValueError: 
            # If value is not a number, keep it as a string
            print(f'Cound not convert {value} to float')
            pass

        # Add the variable to the dictionary
        constants[var_name] = value

# Now you can access the variables like this:
# constants['oxName'], constants['rho_ox_liq'], etc.

# Example to print a variable
#print("Value of oxName:", constants.get('oxName', 'Not Found'))

#LAUNCH PAD DATA FOR LAUNCH CANADA
latitude=47.989083
longitude=-81.853361
elevation=370.3

launch_rail_length=25 #m
inclination = 85 #deg from ground
heading = 0

year = 2023
month = 10
date = 24
hour = 13

###ENGINE DATA
oxName = 'N2O'
rho_ox_liq = constants.get('rho_ox_liquid') #kg/m^3
rho_ox_gas = constants.get('rho_ox_gas') #kg/m^3

fuelName = 'paraffin'
rho_fuel = constants.get('rho_fuel') # kg/m^3

# RocketCEA doesnt have paraffin built in: create it below
#C32H66 from RPA Paraffin Wax Composition
CEA_fuel_str = f"""
fuel paraffin  C 32   H 66    wt%=100.00
h,KJ/Kgmol=-1860600     t(k)=298.15   rho,kg/m3={rho_fuel}
"""

m_fuel_i = constants.get('m_fuel_i') #kg
a = constants.get('a') #m/s
n = constants.get('n')
L = constants.get('L') #m
A_port_i = constants.get('A_port_i') #m^2
 
A_throat = constants.get('A_throat') #m^2
A_exit = constants.get('A_exit') #m^2

r_tank = intometer(5.5/2) #m --> for trajectory sim
height_tank = intometer(40) #m --> for trajectory sim
V_tank = constants.get('V_tank') #m^3

P_tank = constants.get('P_tank') #Pa
fill_level = constants.get('fill_level')
C_d = constants.get('C_d')
inj_orifice_dia = constants.get('inj_orifice_dia')
inj_orifice_count = constants.get('inj_orifice_count')
inj_area = math.pi*(inj_orifice_dia/2)**2
C_inj = C_d*inj_area*inj_orifice_count
#C_inj = constants.get('C_inj')

P_atm = constants.get('P_atm') #Pa
timestep = constants.get('timestep') #s
all_error = constants.get('all_error')

###ROCKET DATA --> MVH-1
rocket_fuselage_rad = intometer(5.5/2) #m --> for trajectory sim
rocket_dry_mass = 30 #kg

nosecone_shape = 'Power Series'
nosecone_length = 0.47 #m

###FILEPATHS FOR VALIDATION
model_file_path = r'src/thrust.csv'
data_file_path = r'src/bens_validation_data/UofT_Deliverance_II/UofT_Deliverance_II_Thrust.csv'
all_validation_data = r'src/bens_validation_data/All_Validation_Data/all_validation_data.csv'
simulation_deliverance_filepath = r'src/model_validation/simulation_deliverance.csv'
simulation_boundless_filepath = r'src/model_validation/simulation_boundless.csv'
simulation_phoenix_filepath = r'src/model_validation/simulation_phoenix.csv'



###SENSITIVITY ANALYSIS INFORMATION!!!!
"""
Variables to analyize:
fill_level
C_inj
V_tank
P_tank
m_fuel_i
a
L
A_port_i
A_throat
A_exit
P_cc
"""

test_var = "a"
min_bound = 0.1
max_bound = 0.2
num_iterations=5





#Fix for Error: qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
#export QT_QPA_PLATFORM=offscreen  








###################### DELIVERANCE CONSTANTS ##################################
constants_deliverance = {}


###ENGINE DATA
constants_deliverance['oxName'] = 'N2O'
constants_deliverance['rho_ox_liq'] = 1220 #kg/m^3
constants_deliverance['rho_ox_gas'] = 1.9277 #kg/m^3
constants_deliverance['fuelName'] = 'paraffin'
constants_deliverance['rho_fuel'] = 930 # kg/m^3

# RocketCEA doesnt have paraffin built in: create it below
#C32H66 from RPA Paraffin Wax Composition
constants_deliverance['CEA_fuel_str'] = f"""
fuel paraffin  C 32   H 66    wt%=100.00
h,KJ/Kgmol=-1860600     t(k)=298.15   rho,kg/m3={rho_fuel}
"""
#TODO fuel mass calc
constants_deliverance['m_fuel_i'] = 0.8142857143
constants_deliverance['a'] = 0.000155
constants_deliverance['n'] = 0.5
constants_deliverance['L'] = 0.508
constants_deliverance['A_port_i'] = 0.005999468075
constants_deliverance['A_throat'] = 0.001063617609
constants_deliverance['A_exit'] = 0.005275543340
#constants_deliverance['rho_fuel'] = 900.0
constants_deliverance['D_port_i'] = 0.0874
constants_deliverance['D_throat'] = 0.0368
constants_deliverance['nozzle_area_ratio'] = 4.96
constants_deliverance['V_tank'] = 0.012
constants_deliverance['P_tank'] = 3820000.0
#TODO Fill level calc
constants_deliverance['fill_level'] = 0.555555
constants_deliverance['C_d'] = 0.21
inj_orifice_dia = 0.0015
inj_orifice_area = math.pi*(inj_orifice_dia/2)**2
inj_orifice_count = 37.0
constants_deliverance['C_inj']= C_inj*inj_orifice_area*inj_orifice_count
#constants_deliverance['C_inj'] = 1.40076e-05
#TODO Fix C_inj

constants_deliverance['P_atm'] = 101325.0
constants_deliverance['timestep'] = 0.05
constants_deliverance['all_error'] = 0.01

#Convert dictionary to named tuple to be accessed by dot notation
tuples_deliverance = namedtuple('tuples_deliverance', constants_deliverance.keys())
constants_deliverance = tuples_deliverance(**constants_deliverance)




###################### BOUNDLESS CONSTANTS ##################################
constants_boundless = {}


###ENGINE DATA
constants_boundless['oxName'] = 'N2O'
constants_boundless['rho_ox_liq'] = 1220 #kg/m^3
constants_boundless['rho_ox_gas'] = 1.9277 #kg/m^3
constants_boundless['fuelName'] = 'paraffin'
constants_boundless['rho_fuel'] = 930 # kg/m^3

# RocketCEA doesnt have paraffin built in: create it below
#C32H66 from RPA Paraffin Wax Composition
constants_boundless['CEA_fuel_str'] = f"""
fuel paraffin  C 32   H 66    wt%=100.00
h,KJ/Kgmol=-1860600     t(k)=298.15   rho,kg/m3={constants_boundless['rho_fuel']}
"""
constants_boundless['m_fuel_i'] = 0.8142857143
constants_boundless['a'] = 0.000155
constants_boundless['n'] = 0.5
constants_boundless['L'] = 0.419
constants_boundless['A_port_i'] = 0.005999468075
constants_boundless['A_throat'] = 0.0407
nozzle_area_ratio = 5
constants_boundless['A_exit'] = nozzle_area_ratio*constants_boundless['A_throat']
constants_boundless['rho_fuel'] = 900.0
constants_boundless['D_port_i'] = 0.055
constants_boundless['D_throat'] = 0.0368
constants_boundless['nozzle_area_ratio'] = 4.96
constants_boundless['V_tank'] = 0.0298
constants_boundless['P_tank'] = 4930000.0
constants_boundless['fill_level'] = 0.555555
constants_boundless['C_d'] = 0.30
inj_orifice_dia = 0.00305
inj_orifice_area = math.pi*(inj_orifice_dia/2)**2
inj_orifice_count = 12.0
constants_boundless['C_inj']  = constants_boundless['C_d']*inj_orifice_area*inj_orifice_count
#constants_boundless['C_inj'] = 1.40076e-05
#TODO Fix C_inj

constants_boundless['P_atm'] = 101325.0
constants_boundless['timestep'] = 0.05
constants_boundless['all_error'] = 0.01

#Convert dictionary to named tuple to be accessed by dot notation
tuples_boundless = namedtuple('tuples_boundless', constants_boundless.keys())
constants_boundless = tuples_boundless(**constants_boundless)




###################### PHOENIX CONSTANTS ##################################
constants_phoenix = {}