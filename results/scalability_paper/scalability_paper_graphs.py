import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import seaborn as sns

_dir = os.path.dirname(os.path.abspath(__file__))


##############################################
# Container CPU and MEM horizontal bars
##############################################

'''
List of all available docker names are here, choose from the list and add it to the wanted list below

Pishahang (Desending order)

'son-gtkkpi', 'son-monitor-pushgateway', 'son-monitor-prometheus','son-sp-infrabstract', 'son-monitor-influxdb','servicelifecyclemanagement', 'son-broker','functionlifecyclemanagement', 'son-postgres', 'son-monitor-probe','son-catalogue-repos', 'placementplugin', 'son-keycloak','cloudservicelifecyclemanagement', 'son-gtkapi', 'son-gtksrv','son-gtkusr', 'son-mongo', 'son-redis', 'sdn-plugin', 'son-gtkvim','son-gtkrlt', 'wim-adaptor', 'son-monitor-manager','pluginmanager', 'son-bss', 'son-monitor-postgres', 'son-gtkrec','son-validate', 'son-gtkfnct', 'son-gtklic', 'son-gtkpkg','son-gtkcsrv', 'specificmanagerregistry', 'son-gui','placementexecutive', 'son-sec-gw'

OSM (Desending order)
'osm_keystone', 'osm_nbi', 'osm_mysql', 'osm_grafana', 'osm_kafka','osm_prometheus', 'osm_ro', 'osm_lcm', 'osm_mongo','osm_zookeeper', 'osm_prometheus-cadvisor', 'osm_pol','osm_light-ui', 'osm_mon'

'''

_docker_wanted_list_pishahang = ['son-sp-infrabstract', 'servicelifecyclemanagement', 'son-broker','functionlifecyclemanagement', 'son-postgres', 'son-catalogue-repos', 'placementplugin', 'son-keycloak','cloudservicelifecyclemanagement', 'son-gtkapi', 'son-gtksrv','son-gtkusr', 'son-mongo', 'son-redis', 'sdn-plugin', 'son-gtkvim']

_docker_wanted_list_osm = ['osm_keystone', 'osm_nbi', 'osm_mysql', 'osm_grafana', 'osm_kafka','osm_prometheus', 'osm_ro', 'osm_lcm', 'osm_mongo','osm_zookeeper', 'osm_prometheus-cadvisor', 'osm_pol','osm_light-ui', 'osm_mon']


for mano in ['pishahang', 'osm']:
    docker_cpu_file = "{}/data/{}_containers_cpu.csv".format(_dir, mano)
    docker_mem_file = "{}/data/{}_containers_mem.csv".format(_dir, mano)

    # FOR CPU
    df = pd.read_csv(docker_cpu_file)
    if mano == 'pishahang':
        df = df[df['Docker Container'].isin(_docker_wanted_list_pishahang)]
    elif mano == 'osm':
        df = df[df['Docker Container'].isin(_docker_wanted_list_osm)]

    df = df.sort_values('CPU Mean', ascending=True)

    sns.set(style='whitegrid', palette='muted', font_scale=1.5)
    fig, ax = plt.subplots()
    # plt.title('{} | Container v/s CPU', fontsize=30)

    plt.xlabel('CPU (%)', fontsize=25)
    plt.ylabel('Containers', fontsize=25)

    index = np.arange(len(df['CPU Mean']))
    width = 0.35 

    ax.barh(index, df['CPU Mean'], height=width, label = "mean", alpha=0.5, capsize=10, color = 'b')
    # ax.barh(index+width, df['CPU Max'], height=width,  label = "max", alpha=0.5, capsize=10, color = 'r')

    plt.yticks(index, df['Docker Container'])
    # plt.legend(loc='center left')
    plt.savefig('{}/graphs/{} - Containers vs CPU.png'.format(_dir, mano), bbox_inches='tight', dpi=100)



    # For MEM

    df = pd.read_csv(docker_mem_file)
    if mano == 'pishahang':
        df = df[df['Docker Container'].isin(_docker_wanted_list_pishahang)]
    elif mano == 'osm':
        df = df[df['Docker Container'].isin(_docker_wanted_list_osm)]
    
    df = df.sort_values('MEM Mean', ascending=True)

    sns.set(style='whitegrid', palette='muted', font_scale=1.5)
    fig, ax = plt.subplots()
    # plt.title('Container v/s MEM', fontsize=30)

    plt.xlabel('MEM (MB)', fontsize=25)
    plt.ylabel('Containers', fontsize=25)

    index = np.arange(len(df['MEM Mean']))
    width = 0.35 

    ax.barh(index, df['MEM Mean'], height=width, label = "mean", alpha=0.5, capsize=10, color = 'b')
    # ax.barh(index+width, df['MEM Max'], height=width,  label = "max", alpha=0.5, capsize=10, color = 'r')

    plt.yticks(index, df['Docker Container'])
    # plt.legend(loc='center left')
    plt.savefig('{}/graphs/{} - Containers vs MEM.png'.format(_dir, mano), bbox_inches='tight', dpi=100)



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
