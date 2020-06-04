# %%
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

from scipy.stats import t  # sudo pip3 install scipy
from math import sqrt

start_time = time.time()


data_folder = "/home/ashwin/Documents/MSc/pg-scramble/MANO-Benchmarking-Framework/results/mvs_thesis/data/thesis-report/"
OUTPUT_PATH = "{}/Final/Graphs".format(data_folder)

NO_CORES = 16

try:
    if not os.path.exists(OUTPUT_PATH):
        os.makedirs(OUTPUT_PATH)
except OSError:
    print('Error: Creating directory. ' + OUTPUT_PATH)

SELECTED_DOCKERS = ['tfplugin', 'servicelifecyclemanagement',
                    'mvplugin', 'mv-policy-plugin']

policy_cpu_file = os.path.join(
    data_folder, 'Policy', 'Final', 'System-CPU-Final-Results.csv')
policy_mem_file = os.path.join(
    data_folder, 'Policy', 'Final', 'System-RAM-Final-Results.csv')
history_cpu_file = os.path.join(
    data_folder, 'History', 'Final', 'System-CPU-Final-Results.csv')
history_mem_file = os.path.join(
    data_folder, 'History', 'Final', 'System-RAM-Final-Results.csv')

policy_docker_files_cpu = [y for x in os.walk(os.path.join(
    data_folder, 'Policy')) for y in glob(os.path.join(x[0], '*-CPU-Docker-Final-Results.csv'))]

policy_docker_files_mem = [y for x in os.walk(os.path.join(
    data_folder, 'Policy')) for y in glob(os.path.join(x[0], '*-MEM-Docker-Final-Results.csv'))]

history_docker_files_cpu = [y for x in os.walk(os.path.join(
    data_folder, 'History')) for y in glob(os.path.join(x[0], '*-CPU-Docker-Final-Results.csv'))]
history_docker_files_mem = [y for x in os.walk(os.path.join(
    data_folder, 'History')) for y in glob(os.path.join(x[0], '*-MEM-Docker-Final-Results.csv'))]

# Policy
policy_cpu_df = pd.read_csv(policy_cpu_file)
policy_mem_df = pd.read_csv(policy_mem_file)

policy_cpu_df = policy_cpu_df.sort_values('Instances', ascending=True)
policy_mem_df = policy_mem_df.sort_values('Instances', ascending=True)

# History
history_cpu_df = pd.read_csv(history_cpu_file)
history_mem_df = pd.read_csv(history_mem_file)

history_cpu_df = history_cpu_df.sort_values('Instances', ascending=True)
history_mem_df = history_mem_df.sort_values('Instances', ascending=True)

# Dockers data
policy_dockers_cpu = {}
policy_dockers_mem = {}
history_dockers_cpu = {}
history_dockers_mem = {}

for _docker in policy_docker_files_cpu:
    _docker_name = Path(_docker).name.split("-CPU-Docker-Final-Results.csv")[0]

    _tmp_df = pd.read_csv(_docker)
    _tmp_df = _tmp_df.sort_values('Instances', ascending=True)

    policy_dockers_cpu[_docker_name] = _tmp_df

for _docker in policy_docker_files_mem:
    _docker_name = Path(_docker).name.split("-MEM-Docker-Final-Results.csv")[0]

    _tmp_df = pd.read_csv(_docker)
    _tmp_df = _tmp_df.sort_values('Instances', ascending=True)

    policy_dockers_mem[_docker_name] = _tmp_df

for _docker in history_docker_files_cpu:
    _docker_name = Path(_docker).name.split("-CPU-Docker-Final-Results.csv")[0]

    _tmp_df = pd.read_csv(_docker)
    _tmp_df = _tmp_df.sort_values('Instances', ascending=True)

    history_dockers_cpu[_docker_name] = _tmp_df

for _docker in history_docker_files_mem:
    _docker_name = Path(_docker).name.split("-MEM-Docker-Final-Results.csv")[0]

    _tmp_df = pd.read_csv(_docker)
    _tmp_df = _tmp_df.sort_values('Instances', ascending=True)

    history_dockers_mem[_docker_name] = _tmp_df

# %%

# ###################################
# System CPU Mean
# ###################################

# sns.set(style='whitegrid', palette='muted', font_scale=1.5)
sns.set_style("whitegrid")
sns.set_palette("colorblind")

fig, ax = plt.subplots(figsize=(5, 4))

index = np.arange(len(history_cpu_df['Instances']))
width = 0.30

# ax.bar(index, history_cpu_df['CPU Mean'], width=width, label="History", edgecolor="black")
# ax.bar(index+width, policy_cpu_df['CPU Mean'], width=width,  label="Policy", edgecolor="black")
# Error
ax.bar(index, history_cpu_df['CPU Mean'], yerr=history_cpu_df['CPU SD'], capsize=3, width=width, label="History", edgecolor="black")
ax.bar(index+width, policy_cpu_df['CPU Mean'], yerr=policy_cpu_df['CPU SD'], capsize=3, width=width,  label="Policy", edgecolor="black")

plt.xticks(index+(width/2), history_cpu_df['Instances'], fontsize=12)
plt.legend(loc=2, borderaxespad=0.1)

plt.xlabel('Instances', fontsize=16)
plt.ylabel('CPU (%)', fontsize=16)

plt.ylim(top=60)

plt.savefig('{}/{}.png'.format(OUTPUT_PATH, "overhead_cpu_mean_pvh"),
            bbox_inches='tight', dpi=300)


# %%

# ###################################
# System CPU Max
# ###################################

# sns.set(style='whitegrid', palette='muted', font_scale=1.5)
sns.set_style("whitegrid")
sns.set_palette("colorblind")

fig, ax = plt.subplots(figsize=(5, 4))

index = np.arange(len(history_cpu_df['Instances']))
width = 0.30

# ax.bar(index, history_cpu_df['CPU Mean'], width=width, label="History", edgecolor="black")
# ax.bar(index+width, policy_cpu_df['CPU Mean'], width=width,  label="Policy", edgecolor="black")
# Error
ax.bar(index, history_cpu_df['CPU Max'], yerr=history_cpu_df['CPU Max SD'], capsize=3, width=width, label="History", edgecolor="black")
ax.bar(index+width, policy_cpu_df['CPU Max'], yerr=policy_cpu_df['CPU Max SD'], capsize=3, width=width,  label="Policy", edgecolor="black")

plt.xticks(index+(width/2), history_cpu_df['Instances'], fontsize=12)
plt.legend(loc=2, borderaxespad=0.1)

plt.xlabel('Instances', fontsize=16)
plt.ylabel('CPU (%)', fontsize=16)

plt.ylim(top=60)

plt.savefig('{}/{}.png'.format(OUTPUT_PATH, "overhead_cpu_max_pvh"),
            bbox_inches='tight', dpi=300)

# ###################################
# System Mem Mean
# ###################################

# sns.set(style='whitegrid', palette='muted', font_scale=1.5)
sns.set_style("whitegrid")
sns.set_palette("colorblind")

fig, ax = plt.subplots(figsize=(5, 4))

index = np.arange(len(history_mem_df['Instances']))
width = 0.30

# Error
ax.bar(index, history_mem_df['MEM Mean'], yerr=history_mem_df['MEM SD'], capsize=3, width=width, label="History", edgecolor="black")
ax.bar(index+width, policy_mem_df['MEM Mean'], yerr=policy_mem_df['MEM SD'], capsize=3, width=width,  label="Policy", edgecolor="black")

plt.xticks(index+(width/2), history_mem_df['Instances'], fontsize=12)
plt.legend(loc=2, borderaxespad=0.1)

plt.xlabel('Instances', fontsize=16)
plt.ylabel('MEM (MB)', fontsize=16)

plt.ylim(top=15000)

plt.savefig('{}/{}.png'.format(OUTPUT_PATH, "overhead_mem_mean_pvh"),
            bbox_inches='tight', dpi=300)


# %%

# ###################################
# System MEM Max
# ###################################

# sns.set(style='whitegrid', palette='muted', font_scale=1.5)
sns.set_style("whitegrid")
sns.set_palette("colorblind")

fig, ax = plt.subplots(figsize=(5, 4))

index = np.arange(len(history_mem_df['Instances']))
width = 0.30

# Error
ax.bar(index, history_mem_df['MEM Max'], yerr=history_mem_df['MEM Max SD'], capsize=3, width=width, label="History", edgecolor="black")
ax.bar(index+width, policy_mem_df['MEM Max'], yerr=policy_mem_df['MEM Max SD'], capsize=3, width=width,  label="Policy", edgecolor="black")

plt.xticks(index+(width/2), history_mem_df['Instances'], fontsize=12)
plt.legend(loc=2, borderaxespad=0.1)

plt.xlabel('Instances', fontsize=16)
plt.ylabel('MEM (MB)', fontsize=16)

plt.ylim(top=15000)

plt.savefig('{}/{}.png'.format(OUTPUT_PATH, "overhead_mem_max_pvh"),
            bbox_inches='tight', dpi=300)

# %%
# ###################################
# Docker cpu mean
# ###################################

# sns.set(style='whitegrid', palette='muted', font_scale=1.5)
sns.set_style("whitegrid")
sns.set_palette("colorblind")

for _dockerName, _DockerValues in policy_dockers_cpu.items():
    fig, ax = plt.subplots(figsize=(5, 4))

    index = np.arange(len(_DockerValues['Instances']))
    width = 0.30

    # Error
    ax.bar(index, history_dockers_cpu[_dockerName]['CPU Mean']/NO_CORES, yerr=history_dockers_cpu[_dockerName]['CPU SD']/NO_CORES, capsize=3, width=width, label="History", edgecolor="black")
    ax.bar(index+width, policy_dockers_cpu[_dockerName]['CPU Mean']/NO_CORES, yerr=policy_dockers_cpu[_dockerName]['CPU SD']/NO_CORES, capsize=3, width=width,  label="Policy", edgecolor="black")

    plt.xticks(index+(width/2), history_mem_df['Instances'], fontsize=12)
    plt.legend(loc=2, borderaxespad=0.1)

    plt.xlabel('Instances', fontsize=16)
    plt.ylabel('MEM (MB)', fontsize=16)

    if _dockerName == "tfplugin":
        plt.ylim(top=45)
    # elif _dockerName == "tfplugin":

    plt.savefig('{}/{}.png'.format(OUTPUT_PATH, "overhead_{}_cpu_mean_pvh".format(_dockerName)),
            bbox_inches='tight', dpi=300)

# %%
# ###################################
# Docker cpu max
# ###################################

# sns.set(style='whitegrid', palette='muted', font_scale=1.5)
sns.set_style("whitegrid")
sns.set_palette("colorblind")

for _dockerName, _DockerValues in policy_dockers_cpu.items():
    fig, ax = plt.subplots(figsize=(5, 4))

    index = np.arange(len(_DockerValues['Instances']))
    width = 0.30

    # Error
    ax.bar(index, history_dockers_cpu[_dockerName]['CPU Max']/NO_CORES, yerr=history_dockers_cpu[_dockerName]['CPU Max SD']/16, capsize=3, width=width, label="History", edgecolor="black")
    ax.bar(index+width, policy_dockers_cpu[_dockerName]['CPU Max']/NO_CORES, yerr=policy_dockers_cpu[_dockerName]['CPU Max SD']/16, capsize=3, width=width,  label="Policy", edgecolor="black")

    plt.xticks(index+(width/2), history_mem_df['Instances'], fontsize=12)
    plt.legend(loc=2, borderaxespad=0.1)

    plt.xlabel('Instances', fontsize=16)
    plt.ylabel('MEM (MB)', fontsize=16)

    if _dockerName == "tfplugin":
        plt.ylim(top=45)


    plt.savefig('{}/{}.png'.format(OUTPUT_PATH, "overhead_{}_cpu_max_pvh".format(_dockerName)),
            bbox_inches='tight', dpi=300)


# %%
# ###################################
# Docker mem mean
# ###################################

# sns.set(style='whitegrid', palette='muted', font_scale=1.5)
sns.set_style("whitegrid")
sns.set_palette("colorblind")

for _dockerName, _DockerValues in policy_dockers_mem.items():
    fig, ax = plt.subplots(figsize=(5, 4))

    index = np.arange(len(_DockerValues['Instances']))
    width = 0.30

    # Error
    ax.bar(index, history_dockers_mem[_dockerName]['MEM Mean'], yerr=history_dockers_mem[_dockerName]['MEM SD'], capsize=3, width=width, label="History", edgecolor="black")
    ax.bar(index+width, policy_dockers_mem[_dockerName]['MEM Mean'], yerr=policy_dockers_mem[_dockerName]['MEM SD'], capsize=3, width=width,  label="Policy", edgecolor="black")

    plt.xticks(index+(width/2), history_mem_df['Instances'], fontsize=12)
    plt.legend(loc=2, borderaxespad=0.1)

    plt.xlabel('Instances', fontsize=16)
    plt.ylabel('MEM (MB)', fontsize=16)

    if _dockerName == "tfplugin":
        plt.ylim(top=1150)

    plt.savefig('{}/{}.png'.format(OUTPUT_PATH, "overhead_{}_mem_mean_pvh".format(_dockerName)),
            bbox_inches='tight', dpi=300)

# %%
# ###################################
# Docker mem max
# ###################################

# sns.set(style='whitegrid', palette='muted', font_scale=1.5)
sns.set_style("whitegrid")
sns.set_palette("colorblind")

for _dockerName, _DockerValues in policy_dockers_mem.items():
    fig, ax = plt.subplots(figsize=(5, 4))

    index = np.arange(len(_DockerValues['Instances']))
    width = 0.30

    # Error
    ax.bar(index, history_dockers_mem[_dockerName]['MEM Max'], yerr=history_dockers_mem[_dockerName]['MEM Max SD'], capsize=3, width=width, label="History", edgecolor="black")
    ax.bar(index+width, policy_dockers_mem[_dockerName]['MEM Max'], yerr=policy_dockers_mem[_dockerName]['MEM Max SD'], capsize=3, width=width,  label="Policy", edgecolor="black")

    plt.xticks(index+(width/2), history_mem_df['Instances'], fontsize=12)
    plt.legend(loc=2, borderaxespad=0.1)

    plt.xlabel('Instances', fontsize=16)
    plt.ylabel('MEM (MB)', fontsize=16)

    if _dockerName == "tfplugin":
        plt.ylim(top=1150)

    plt.savefig('{}/{}.png'.format(OUTPUT_PATH, "overhead_{}_mem_max_pvh".format(_dockerName)),
            bbox_inches='tight', dpi=300)


#########################################
#########################################
# END
#########################################
#########################################


print("Total time: {}".format(time.time() - start_time))


# %%
