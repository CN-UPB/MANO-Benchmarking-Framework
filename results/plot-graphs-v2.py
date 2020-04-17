import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import csv
import pandas as pd
import os
from glob import glob
from pathlib import Path
import time
import seaborn as sns
import matplotlib.dates as mdates
import datetime as dt
import statistics
from csv import reader

# from scipy.interpolate import spline


from scipy.stats import t # sudo pip3 install scipy
from math import sqrt

start_time = time.time()

# Scalability Paper

RPM_INSTANCES_SYSTEM_CPU_BAR = True

OUTPUT_PATH = "/home/ashwin/Documents/WHB-Hadi/ScalabilityPaper/Data/rpm-instances-1//Graphs"

# --------------

# sys_load_files = [y for x in os.walk(INPUT_PATH) for y in glob(os.path.join(x[0], '*-System-Load-Final-Results.csv'))]
# sys_ram_files = [y for x in os.walk(INPUT_PATH) for y in glob(os.path.join(x[0], '*-System-RAM-Final-Results.csv'))]

# #osm_rpm_doc_cpu_files = [y for x in os.walk(INPUT_PATH) for y in glob(os.path.join(x[0], '*-CPU-RPM-Final-Results.csv'))]
# pish_rpm_doc_cpu_files = [y for x in os.walk(INPUT_PATH) for y in glob(os.path.join(x[0], '*-CPU-RPM-Final-Results.csv'))]
# pish_rpm_doc_mem_files = [y for x in os.walk(INPUT_PATH) for y in glob(os.path.join(x[0], '*-MEM-RPM-Final-Results.csv'))]



##############################################
# System CPU Bar Chart vs RPM_INSTANCES 
##############################################

if RPM_INSTANCES_SYSTEM_CPU_BAR:
    INPUT_PATH = "/home/ashwin/Documents/WHB-Hadi/ScalabilityPaper/Data/rpm-instances-1/Final"
    sys_cpu_files = [y for x in os.walk(INPUT_PATH) for y in glob(os.path.join(x[0], 'System-CPU-Final-Results.csv'))]

    data_dict = {}
    pishahang_data_dict = {}
    rpmset = []  
    runset = [] 

    i_mean = []
    i_std = []
    i_max = []
    i_min = []

    for _sys_cpu_files in sys_cpu_files:

        df = pd.read_csv(_sys_cpu_files)

        sns.set(style='whitegrid', palette='muted', font_scale=1.5)
        fig, ax = plt.subplots(figsize=(35,20))
        plt.title('CPU v/s RPM', fontsize=30)

        plt.xlabel('RPM', fontsize=25)
        plt.ylabel('CPU (%)', fontsize=25)

        index = np.arange(len(df['RPM']))
        width = 0.30 

        # ax.bar(index-width, df['mean'], yerr=df['std']['mean'], label = "mean", alpha=0.5, capsize=10)
        ax.bar(index-width, df['CPU Min'],  yerr=df['CPU Min SD'], width=width, label = "min", alpha=0.5, capsize=10, color = 'g')
        ax.bar(index, df['CPU Mean'], yerr=df['CPU SD'], width=width, label = "mean", alpha=0.5, capsize=10, color = 'b')
        ax.bar(index+width, df['CPU Max'], yerr=df['CPU Max SD'], width=width,  label = "max", alpha=0.5, capsize=10, color = 'r')

        plt.xticks(index, df['RPM'])
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        plt.savefig('{}/{}.png'.format(OUTPUT_PATH, "Pishahang - RPM vs CPU") ,bbox_inches='tight',dpi=100)


#########################################
# RPM_INDIVIDUAL_TIMES
#########################################

if RPM_INDIVIDUAL_TIMES:
    RPM_E2E_PATH = "/home/ashwin/Documents/WHB-Hadi/ScalabilityPaper/Data/FINAL-150-3000rpm/150-final-1/150"
    pishahang_ind_files = [y for x in os.walk(RPM_E2E_PATH) for y in glob(os.path.join(x[0], 'individual-times.csv'))]
    pishahang_data_dict = {}
    rpmset = []  
    runset = [] 

    i_mean = []
    i_std = []
    i_max = []
    i_min = []

    for _i_file in pishahang_ind_files:
        rpm = Path(_i_file).parent.name.split("_rpm")[1].split("_")[0]   
        rpmset.append(int(rpm))
        run =  Path(_i_file).parent.name.split("rpm")[1].split("_")[1].split("-")[0]   
        runset.append(run)
        i_data = pd.read_csv(_i_file)
        i_mean.append(i_data["mean"][0])
        i_std.append(i_data["std"][0])
        i_max.append(i_data["max"][0])
        i_min.append(i_data["min"][0])

    dict = {
        'rpm': rpmset,
        'run': runset,
        'mean': i_mean,
        'std': i_std,
        'max': i_max,
        'min': i_min
        }

    df = pd.DataFrame(dict)
    df = df.sort_values('rpm')
    df = df = df.groupby(['rpm']).agg(['mean', 'std']).reset_index()

    dataf = df.reset_index()

    sns.set(style='whitegrid', palette='muted', font_scale=1.5)
    fig, ax = plt.subplots(figsize=(35,20))
    plt.title('Individual Times v/s RPM', fontsize=30)

    plt.xlabel('RPM', fontsize=25)
    plt.ylabel('Individual Time (sec)', fontsize=25)

    index = np.arange(len(dataf['mean']))
    width = 0.30 

    # ax.bar(index-width, dataf['mean']['mean'], yerr=dataf['std']['mean'], label = "mean", alpha=0.5, capsize=10)
    ax.bar(index-width, dataf['mean']['mean'],  yerr=dataf['mean']['std'], width=width, label = "mean", alpha=0.5, capsize=10, color = 'b')
    ax.bar(index, dataf['max']['mean'], yerr=dataf['max']['std'], width=width, label = "max", alpha=0.5, capsize=10, color = 'r')
    ax.bar(index+width, dataf['min']['mean'], yerr=dataf['min']['std'], width=width,  label = "min", alpha=0.5, capsize=10, color = 'g')

    plt.xticks(index, df['rpm'])
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.savefig('{}/{}.png'.format(OUTPUT_PATH, "Pishahang - RPM vs Individual") ,bbox_inches='tight',dpi=100)


#########################################
#########################################
# END
#########################################
#########################################




print("Total time: {}".format(time.time() - start_time))
