#from src import constants

from src.thrust_curve.bens_ox_tank import OxTank
from src.thrust_curve.combustion_chamber import cc
   
import matplotlib.pyplot as plt
import numpy as np
import csv

def run_thrust_curve(config, output_file):
    #INPUT VARIABLES
    time_arr = []
    m_dot_arr = []
    thrust_arr = []
    p_cc_arr = []

    P_cc = config.P_atm

    r1ox = OxTank(config.oxName, config.timestep, config.fill_level, config.C_inj,
                config.V_tank, config.P_tank, config.P_atm, config.all_error)


    r1cc = cc(config.oxName, config.fuelName, config.CEA_fuel_str, config.m_fuel_i, 
            config.rho_fuel, config.a, config.n, config.L, config.A_port_i, 
            config.P_atm, config.A_throat, config.A_exit, config.timestep)

    ###ENTER THRUST CURVE
    while r1ox.t < 7:
        r1ox.inst(P_cc)
        r1cc.inst(r1ox.m_dot_ox, P_cc)

        time_arr.append(r1ox.t)
        m_dot_arr.append(r1ox.m_dot_ox)
        thrust_arr.append(r1cc.instThrust)
        p_cc_arr.append(r1cc.P_cc)


    ###WRITE CSV FOR VALIDATION
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['time', 'm_dot', 'thrust', 'p_cc'])  #Writing the header

        for time, m_dot, thrust, p_cc in zip(time_arr, m_dot_arr, thrust_arr, p_cc_arr):
            writer.writerow([time, m_dot, thrust, p_cc])

        print(f"Data written to {output_file}")


    ###WRITE CSV FOR FLIGHT SIM
    m_dot_combined_arr = list(zip(time_arr,m_dot_arr))
    thrust_combined_arr = list(zip(time_arr, thrust_arr))

    with open(r'./src/m_dot_ox.csv' , 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(m_dot_combined_arr)

    with open(r'./src/thrust.csv' , 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(thrust_combined_arr)



    ###PLOTS
    plt.subplot(1,2,1)
    plt.plot(time_arr,m_dot_arr)
    plt.xlabel('Time (s)')
    plt.ylabel('m_dot_ox (kg/s)')
    plt.title('Mass Flow Rate Over Timee')
    plt.grid(True)

    plt.subplot(1,2,2)
    plt.plot(time_arr,thrust_arr)
    plt.xlabel('Time')
    plt.ylabel('Thrust')
    plt.title('Thrust Curve')
    plt.grid(True)

    plt.savefig('src/thrust_curve/thrustPlot.png')

