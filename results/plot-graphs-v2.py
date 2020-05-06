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
RPM_INDIVIDUAL_TIMES = True
MISSED_REQUESTS_BAR = True

INPUT_PATH = "/home/ashwin/Documents/WHB-Hadi/ScalabilityPaper/Data/FINAL/OSM/case1/Final"
OUTPUT_PATH = "/home/ashwin/Documents/WHB-Hadi/ScalabilityPaper/Data/FINAL/OSM/case1/Graphs"

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
    sys_cpu_files = [y for x in os.walk(INPUT_PATH) for y in glob(os.path.join(x[0], 'System-CPU-Final-Results.csv'))]

    for _sys_cpu_files in sys_cpu_files:

        df = pd.read_csv(_sys_cpu_files)
        df = df.sort_values('RPM')

        sns.set(style='whitegrid', palette='muted', font_scale=1.5)
        fig, ax = plt.subplots(figsize=(35,20))
        plt.title('CPU v/s RPM', fontsize=30)

        plt.xlabel('RPM', fontsize=25)
        plt.ylabel('CPU (%)', fontsize=25)

        index = np.arange(len(df['RPM']))
        width = 0.30 

        # ax.bar(index-width, df['mean'], yerr=df['std']['mean'], label = "mean", alpha=0.5, capsize=10)
        ax.bar(index-width, df['CPU Min'], width=width, label = "min", alpha=0.5, capsize=10, color = 'g')
        ax.bar(index, df['CPU Mean'], width=width, label = "mean", alpha=0.5, capsize=10, color = 'b')
        ax.bar(index+width, df['CPU Max'], width=width,  label = "max", alpha=0.5, capsize=10, color = 'r')
        # Error 
        # ax.bar(index-width, df['CPU Min'],  yerr=df['CPU Min SD'], width=width, label = "min", alpha=0.5, capsize=10, color = 'g')
        # ax.bar(index, df['CPU Mean'], yerr=df['CPU SD'], width=width, label = "mean", alpha=0.5, capsize=10, color = 'b')
        # ax.bar(index+width, df['CPU Max'], yerr=df['CPU Max SD'], width=width,  label = "max", alpha=0.5, capsize=10, color = 'r')

        plt.xticks(index, df['RPM'])
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        plt.savefig('{}/{}.png'.format(OUTPUT_PATH, "Pishahang - RPM vs CPU") ,bbox_inches='tight',dpi=100)


#########################################
# RPM_INDIVIDUAL_TIMES
#########################################

if RPM_INDIVIDUAL_TIMES:
    sys_cpu_files = [y for x in os.walk(INPUT_PATH) for y in glob(os.path.join(x[0], 'Individual-Times-Final-Results.csv'))]

    for _sys_cpu_files in sys_cpu_files:

        df = pd.read_csv(_sys_cpu_files)
        df = df.sort_values('RPM')

        sns.set(style='whitegrid', palette='muted', font_scale=1.5)
        fig, ax = plt.subplots(figsize=(35,20))
        plt.title('Deployment Times v/s RPM', fontsize=30)

        plt.xlabel('RPM', fontsize=25)
        plt.ylabel('Deployment Time (s)', fontsize=25)

        index = np.arange(len(df['RPM']))
        width = 0.30 

        # ax.bar(index-width, df['mean'], yerr=df['std']['mean'], label = "mean", alpha=0.5, capsize=10)
        ax.bar(index-width, df['Min'], width=width, label = "min", alpha=0.5, capsize=10, color = 'g')
        ax.bar(index, df['Mean'], width=width, label = "mean", alpha=0.5, capsize=10, color = 'b')
        ax.bar(index+width, df['Max'], width=width,  label = "max", alpha=0.5, capsize=10, color = 'r')

        # Error
        # ax.bar(index-width, df['Min'],  yerr=df['Min SD'], width=width, label = "min", alpha=0.5, capsize=10, color = 'g')
        # ax.bar(index, df['Mean'], yerr=df['SD'], width=width, label = "mean", alpha=0.5, capsize=10, color = 'b')
        # ax.bar(index+width, df['Max'], yerr=df['Max SD'], width=width,  label = "max", alpha=0.5, capsize=10, color = 'r')

        plt.xticks(index, df['RPM'])
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        plt.savefig('{}/{}.png'.format(OUTPUT_PATH, "OSM - RPM vs Deployment Times") ,bbox_inches='tight',dpi=100)

#########################################
# MISSED_REQUESTS_BAR
#########################################

if MISSED_REQUESTS_BAR:
    sys_cpu_files = [y for x in os.walk(INPUT_PATH) for y in glob(os.path.join(x[0], 'Lost-Requests-Final-Results.csv'))]

    for _sys_cpu_files in sys_cpu_files:

        df = pd.read_csv(_sys_cpu_files)
        df = df.sort_values('RPM')

        sns.set(style='whitegrid', palette='muted', font_scale=1.5)
        fig, ax = plt.subplots(figsize=(35,20))
        plt.title('Missed Requests v/s RPM', fontsize=30)

        plt.xlabel('RPM', fontsize=25)
        plt.ylabel('Deployment Time (s)', fontsize=25)

        index = np.arange(len(df['RPM']))
        width = 0.30 

        ax.bar(index, df['Lost'], width=width, label = "lost", alpha=0.5, capsize=10, color = 'b')

        plt.xticks(index, df['RPM'])
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        plt.savefig('{}/{}.png'.format(OUTPUT_PATH, "OSM - RPM vs Missed Requests") ,bbox_inches='tight',dpi=100)



#########################################
#########################################
# END
#########################################
#########################################




print("Total time: {}".format(time.time() - start_time))
