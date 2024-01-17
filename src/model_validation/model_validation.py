import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
import seaborn as sns
from src import constants
from src.thrust_curve import thrust_curve

#Filepaths
simulation_deliverance_filepath=constants.simulation_deliverance_filepath
simulation_boundless_filepath=constants.simulation_boundless_filepath
simulation_phoenix_filepath=constants.simulation_phoenix_filepath
all_validation_data = constants.all_validation_data

constants_deliverance=constants.constants_deliverance
constants_boundless=constants.constants_boundless

thrust_curve.run_thrust_curve(constants_deliverance, simulation_deliverance_filepath)
thrust_curve.run_thrust_curve(constants_boundless, simulation_boundless_filepath)


###ADD FILEPATH HERE!!!!!
#odel_file_path = constants.model_file_path
#data_file_path = constants.data_file_path



#Plotting Deliverance
df_simulation = pd.read_csv(simulation_deliverance_filepath)
df_experimental = pd.read_csv(all_validation_data)
# Create a figure with 3 subplots, arranged vertically
plt.figure(figsize=(10, 12))
# Subplot for m_dot vs time
plt.subplot(3, 1, 1)  # (3 rows, 1 column, 1st subplot)
plt.plot(df_simulation['time'], df_simulation['m_dot'], label='simulation')
plt.plot(df_experimental['Time'], df_experimental['UofT Deliverance II Tank Pressure'], label='experimental')
plt.title('m_dot vs Time')
plt.legend()
plt.xlabel('Time')
plt.ylabel('m_dot')
# Subplot for thrust vs time
plt.subplot(3, 1, 2)  # (3 rows, 1 column, 2nd subplot)
plt.plot(df_simulation['time'], df_simulation['thrust'], label='simulation')
plt.plot(df_experimental['Time'], df_experimental['UofT Deliverance II Thrust'], label='experimental')
plt.title('Thrust vs Time')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Thrust')
# Subplot for p_cc vs time
plt.subplot(3, 1, 3)  # (3 rows, 1 column, 3rd subplot)
plt.plot(df_simulation['time'], df_simulation['p_cc'], label='simulation')
plt.plot(df_experimental['Time'], df_experimental['UofT Deliverance II Chamber Pressure'], label='experimental')
plt.title('P_cc vs Time')
plt.xlabel('Time')
plt.ylabel('P_cc')
# Adjust layout to prevent overlap of subplots
plt.tight_layout()
plt.savefig('src/model_validation/validation_deliverance.png')

#Plotting Boundless
df_simulation = pd.read_csv(simulation_boundless_filepath)
df_experimental = pd.read_csv(all_validation_data)
# Create a figure with 3 subplots, arranged vertically
plt.figure(figsize=(10, 12))
# Subplot for m_dot vs time
plt.subplot(3, 1, 1)  # (3 rows, 1 column, 1st subplot)
plt.plot(df_simulation['time'], df_simulation['m_dot'], label='simulation')
plt.plot(df_experimental['Time'], df_experimental['UofW Boundless Tank Pressure'], label='experimental')
plt.title('m_dot vs Time')
plt.legend()
plt.xlabel('Time')
plt.ylabel('m_dot')
# Subplot for thrust vs time
plt.subplot(3, 1, 2)  # (3 rows, 1 column, 2nd subplot)
plt.plot(df_simulation['time'], df_simulation['thrust'], label='simulation')
plt.plot(df_experimental['Time'], df_experimental['UofW Boundless Thrust'], label='experimental')
plt.title('Thrust vs Time')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Thrust')
# Subplot for p_cc vs time
plt.subplot(3, 1, 3)  # (3 rows, 1 column, 3rd subplot)
plt.plot(df_simulation['time'], df_simulation['p_cc'], label='simulation')
plt.plot(df_experimental['Time'], df_experimental['UofW Boundless Chamber Pressure'], label='experimental')
plt.title('P_cc vs Time')
plt.xlabel('Time')
plt.ylabel('P_cc')
# Adjust layout to prevent overlap of subplots
plt.tight_layout()
plt.savefig('src/model_validation/validation_boundless.png')

"""
#Plotting Phoenix
df_simulation = pd.read_csv(simulation_phoenix_filepath)
df_experimental = pd.read_csv(all_validation_data)
# Create a figure with 3 subplots, arranged vertically
plt.figure(figsize=(10, 12))
# Subplot for m_dot vs time
plt.subplot(3, 1, 1)  # (3 rows, 1 column, 1st subplot)
plt.plot(df_simulation['time'], df_simulation['m_dot'], label='simulation')
plt.plot(df_experimental['Time'], df_experimental['Phoenix1A Model Tank Pressure'], label='experimental')
plt.title('m_dot vs Time')
plt.legend()
plt.xlabel('Time')
plt.ylabel('m_dot')
# Subplot for thrust vs time
plt.subplot(3, 1, 2)  # (3 rows, 1 column, 2nd subplot)
plt.plot(df_simulation['time'], df_simulation['thrust'], label='simulation')
plt.plot(df_experimental['Time'], df_experimental['UofW Boundless Thrust'], label='experimental')
plt.title('Thrust vs Time')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Thrust')
# Subplot for p_cc vs time
plt.subplot(3, 1, 3)  # (3 rows, 1 column, 3rd subplot)
plt.plot(df_simulation['time'], df_simulation['p_cc'], label='simulation')
plt.plot(df_experimental['Time'], df_experimental['UofW Boundless Chamber Pressure'], label='experimental')
plt.title('P_cc vs Time')
plt.xlabel('Time')
plt.ylabel('P_cc')
# Adjust layout to prevent overlap of subplots
plt.tight_layout()
plt.savefig('src/model_validation/validation_boundless.png')

"""
