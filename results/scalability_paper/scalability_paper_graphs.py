import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import seaborn as sns

_dir = os.path.dirname(os.path.abspath(__file__))

################
# CPU
################

df = pd.read_csv("{}/data/cpu.csv".format(_dir))
df = df.sort_values('RPM')

X_LABEL = 'Requests per minute (RPM)'
Y_LABEL = 'CPU Usage (%)'

osm_means = df["OSM"]
pish_means = df["Pishahang"]
rpm = df["RPM"]

ind = np.arange(len(rpm))
width = 0.35
sns.set(style='whitegrid', palette='muted', font_scale=1.5)

fig, ax = plt.subplots()

rects1 = ax.bar(ind - width/2, pish_means, width, label='Pishahang',color = 'b')
rects2 = ax.bar(ind + width/2, osm_means, width, label='OSM', color = 'g')

# Labels, title and custom x-axis tick labels, etc.
ax.set_title('')

ax.set_xlabel(X_LABEL)
ax.set_ylabel(Y_LABEL)
ax.set_xticks(ind)

ax.set_xticklabels(rpm)
ax.legend()
fig.tight_layout()

plt.savefig('{}/graphs/CPU - OSM-vs-Pishahang.png'.format(_dir), bbox_inches='tight', dpi=100)

################
# Mem
################

df = pd.read_csv("{}/data/mem.csv".format(_dir))
df = df.sort_values('RPM')

X_LABEL = 'Requests per minute (RPM)'
Y_LABEL = 'Memory Usage (MB)'

osm_means = df["OSM"]
pish_means = df["Pishahang"]
rpm = df["RPM"]

ind = np.arange(len(rpm))
width = 0.35
sns.set(style='whitegrid', palette='muted', font_scale=1.5)

fig, ax = plt.subplots()

rects1 = ax.bar(ind - width/2, pish_means, width, label='Pishahang',color = 'b')
rects2 = ax.bar(ind + width/2, osm_means, width, label='OSM', color = 'g')

# Labels, title and custom x-axis tick labels, etc.
ax.set_title('')

ax.set_xlabel(X_LABEL)
ax.set_ylabel(Y_LABEL)
ax.set_xticks(ind)

ax.set_xticklabels(rpm)
ax.legend()
fig.tight_layout()

plt.savefig('{}/graphs/MEM - OSM-vs-Pishahang.png'.format(_dir), bbox_inches='tight', dpi=100)

#####################
# Deployment Times
#####################

df = pd.read_csv("{}/data/deployment_times.csv".format(_dir))
df = df.sort_values('RPM')

X_LABEL = 'Requests per minute (RPM)'
Y_LABEL = 'Deployment Time (s)'

osm_means = df["OSM"]
pish_means = df["Pishahang"]
rpm = df["RPM"]

ind = np.arange(len(rpm))
width = 0.35
sns.set(style='whitegrid', palette='muted', font_scale=1.5)

fig, ax = plt.subplots()

rects1 = ax.bar(ind - width/2, pish_means, width, label='Pishahang',color = 'b')
rects2 = ax.bar(ind + width/2, osm_means, width, label='OSM', color = 'g')

# Labels, title and custom x-axis tick labels, etc.
ax.set_title('')

ax.set_xlabel(X_LABEL)
ax.set_ylabel(Y_LABEL)
ax.set_xticks(ind)

ax.set_xticklabels(rpm)
ax.legend()
fig.tight_layout()

plt.savefig('{}/graphs/Deployment - OSM-vs-Pishahang.png'.format(_dir), bbox_inches='tight', dpi=100)


#####################
# Lost Requests
#####################

df = pd.read_csv("{}/data/lost_requests.csv".format(_dir))
df = df.sort_values('RPM')

X_LABEL = 'Requests per minute (RPM)'
Y_LABEL = '# Failed Requests'

osm_means = df["OSM"]
pish_means = df["Pishahang"]
rpm = df["RPM"]

ind = np.arange(len(rpm))
width = 0.35
sns.set(style='whitegrid', palette='muted', font_scale=1.5)

fig, ax = plt.subplots()

rects1 = ax.bar(ind - width/2, pish_means, width, label='Pishahang',color = 'b')
rects2 = ax.bar(ind + width/2, osm_means, width, label='OSM', color = 'g')

# Labels, title and custom x-axis tick labels, etc.
ax.set_title('')

ax.set_xlabel(X_LABEL)
ax.set_ylabel(Y_LABEL)
ax.set_xticks(ind)

ax.set_xticklabels(rpm)
ax.legend()
fig.tight_layout()

plt.savefig('{}/graphs/Failed - OSM-vs-Pishahang.png'.format(_dir), bbox_inches='tight', dpi=100)
