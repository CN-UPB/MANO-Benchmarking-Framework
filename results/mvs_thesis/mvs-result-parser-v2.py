# import csv
from collections import Counter
import ntpath
import pandas as pd # pip install pandas
import os
from glob import glob
import time
from pathlib import Path
import json
import statistics
import csv

data_folder = "/home/ashwin/Documents/MSc/pg-scramble/MANO-Benchmarking-Framework/results/mvs_thesis/data/thesis-report/Policy"
out_folder = "{}/Final/".format(data_folder)

instances = [1, 5, 10]

SYSTEM = True
CASES = True
DOCKERS = True

SELECTED_DOCKERS = ['tfplugin', 'servicelifecyclemanagement', 'mvplugin', 'mv-policy-plugin']

def average_cpu (csv_filepath):
    # print(ntpath.basename(csv_filepath))
    df=pd.read_csv(csv_filepath)

    df['totalcpu'] = df['user'] + df['system'] 

    _max = df['totalcpu'].max()
    _min = df['totalcpu'].min()
    _mean = df['totalcpu'].mean()
    _std = df['totalcpu'].std()

    print("CPU Mean: {} \t Min: {} \t Max: {} \t Std: {} \n".format( _mean, _min, _max, _std))
    return {"mean": float(_mean), "min": float(_min), "max": float(_max), "std": float(_std)} 

def average_mem(csv_filepath):
    # print(ntpath.basename(csv_filepath))
    df=pd.read_csv(csv_filepath)

    _max = df['ram'].max()
    _min = df['ram'].min()
    _mean = df['ram'].mean()

    print("MEM Mean: {} \t Min: {} \t Max: {} \n".format( _mean, _min, _max))
    return {"mean": float(_mean), "min": float(_min), "max": float(_max)} 

def average_sys_ram(csv_filepath):
    # print(ntpath.basename(csv_filepath))
    df=pd.read_csv(csv_filepath)

    _min = df['used'].min()
    _max = df['used'].max()
    _mean = df['used'].mean()

    print("MEM Mean: {} \t Min: {} \t Max: {} \n".format( _mean, _min, _max))
    return {"mean": float(_mean), "min": float(_min), "max": float(_max)} 

def average_sys_cpu(csv_filepath):
    # print(ntpath.basename(csv_filepath))
    df=pd.read_csv(csv_filepath)

    df['totalsyscpu'] = df['user'] + df['system'] 

    _max = df['totalsyscpu'].max()
    _min = df['totalsyscpu'].min()
    _mean = df['totalsyscpu'].mean()

    print("System CPU Mean: {} \t Min: {} \t Max: {} \n".format( _mean, _min, _max))
    return {"mean": float(_mean), "min": float(_min), "max": float(_max)} 

def average_sys_load(csv_filepath):
    # print(ntpath.basename(csv_filepath))
    df=pd.read_csv(csv_filepath)

    load1_max = df['load1'].max()
    load1_min = df['load1'].min()
    load1_mean = df['load1'].mean()

    load5_max = df['load5'].max()
    load5_min = df['load5'].min()
    load5_mean = df['load5'].mean()

    load15_max = df['load15'].max()
    load15_min = df['load15'].min()
    load15_mean = df['load15'].mean()

    print("Load1 Mean: {} \t Min: {} \t Max: {} \n".format( load1_mean, load1_min, load1_max))
    return {"mean1": float(load1_mean), "min1": float(load1_min), "max1": float(load1_max),
            "mean5": float(load5_mean), "min5": float(load5_min), "max5": float(load5_max),
            "mean15": float(load15_mean), "min15": float(load15_min), "max15": float(load15_max)} 


result_sys_cpu_dict = {}
result_sys_load_dict = {}
result_sys_ram_dict = {}
result_cpu_dict = {}
result_mem_dict = {}

result_docker_cpu_dict = {}
result_docker_mem_dict = {}


for _i in instances:
    _PATH = "{}/{}".format(data_folder, _i)
    _OUT_PATH = "{}/Final/{}".format(data_folder, _i)

    try:
        if not os.path.exists(_OUT_PATH):
            os.makedirs(_OUT_PATH)
    except OSError:
        print ('Error: Creating directory. ' + _OUT_PATH)
      
    start_time = time.time()

    cpu_files = [y for x in os.walk(_PATH) for y in glob(os.path.join(x[0], '*-cpu.csv'))]
    mem_files = [y for x in os.walk(_PATH) for y in glob(os.path.join(x[0], '*-mem_usage.csv'))]
    sys_files = [y for x in os.walk(_PATH) for y in glob(os.path.join(x[0], 'system-*.csv'))]


    for _sys_file in sys_files:
        print(Path(_sys_file).parent.name)
        print(Path(_sys_file).name)

        _run = Path(_sys_file).parent.name.split("run_")[1]

        _type = Path(_sys_file).name
        _type = _type.split(".")[0]

        if ntpath.basename(_sys_file) == "system-cpu.csv":
            if not _i in result_sys_cpu_dict:
                result_sys_cpu_dict[_i] = {}

            # average_cpu(_cpu_file)
            result_sys_cpu_dict[_i][_run] = average_sys_cpu(_sys_file)

        if ntpath.basename(_sys_file) == "system-load.csv":
            if not _i in result_sys_load_dict:
                result_sys_load_dict[_i] = {}

            # average_cpu(_cpu_file)
            result_sys_load_dict[_i][_run] = average_sys_load(_sys_file)

        if ntpath.basename(_sys_file) == "system-ram.csv":
            if not _i in result_sys_ram_dict:
                result_sys_ram_dict[_i] = {}

            # average_cpu(_cpu_file)
            result_sys_ram_dict[_i][_run] = average_sys_ram(_sys_file)


    for _cpu_file in cpu_files:
        print(Path(_cpu_file).parent.name)
        print(Path(_cpu_file).name)

        if ntpath.basename(_cpu_file) == "system-cpu.csv":
            continue

        _run = Path(_cpu_file).parent.name.split("run_")[1]

        _docker = Path(_cpu_file).name
        _docker = _docker.split(".")[0]

        if not _i in result_cpu_dict:
            result_cpu_dict[_i] = {}

        if not _docker in result_cpu_dict[_i]:
            result_cpu_dict[_i][_docker] = {}

        if not _docker in result_docker_cpu_dict:
            result_docker_cpu_dict[_docker] = {}

        if not _i in result_docker_cpu_dict[_docker]:
            result_docker_cpu_dict[_docker][_i] = {}

        _avg_cpu = average_cpu(_cpu_file)
        result_cpu_dict[_i][_docker][_run] = _avg_cpu
        result_docker_cpu_dict[_docker][_i][_run] = _avg_cpu

    for _mem_file in mem_files:
        print(Path(_mem_file).parent.name)
        print(Path(_mem_file).name)

        _run = Path(_mem_file).parent.name.split("run_")[1]

        _docker = Path(_mem_file).name
        _docker = _docker.split(".")[0]

        if not _i in result_mem_dict:
            result_mem_dict[_i] = {}

        if not _docker in result_mem_dict[_i]:
            result_mem_dict[_i][_docker] = {}

        if not _docker in result_docker_mem_dict:
            result_docker_mem_dict[_docker] = {}

        if not _i in result_docker_mem_dict[_docker]:
            result_docker_mem_dict[_docker][_i] = {}

        _avg_mem = average_mem(_mem_file)
        result_mem_dict[_i][_docker][_run] = _avg_mem
        result_docker_mem_dict[_docker][_i][_run] = _avg_mem

    if CASES:
        for _case, _caseValue in result_cpu_dict.items():
            print(_case)
            with open('{outpath}/{case}-CPU-Final-Results.csv'.format(outpath=_OUT_PATH, case=_case), mode='w') as cpu_resultsfile:
                fieldnames = ['Docker Container', 'CPU Mean', 'CPU SD', 'CPU Max', 'CPU Max SD', 'CPU Min', 'CPU Min SD']
                writer = csv.writer(cpu_resultsfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(fieldnames)

                for _docker, _dockerValue in _caseValue.items():
                    _dockerName = _docker
                    _meanofMeans = statistics.mean([_dockerValue[v]['mean'] for v in _dockerValue])
                    _stddevofMeans = statistics.pstdev([_dockerValue[v]['mean'] for v in _dockerValue])

                    _meanofMax = statistics.mean([_dockerValue[v]['max'] for v in _dockerValue])
                    _stddevofMax = statistics.pstdev([_dockerValue[v]['max'] for v in _dockerValue])
                    
                    _meanofMin = statistics.mean([_dockerValue[v]['min'] for v in _dockerValue])
                    _stddevofMin = statistics.pstdev([_dockerValue[v]['min'] for v in _dockerValue])

                    # print(_dockerName)
                    # print(_dockerValue["1"]["mean"], _dockerValue["2"]["mean"], _dockerValue["3"]["mean"])
                    # print(_meanofMeans)
                    # print(_stddevofMeans)
                    # print(_meanofMax)
                    # print(_meanofMin)

                    writer.writerow([_dockerName, _meanofMeans, _stddevofMeans, _meanofMax,  _stddevofMax, _meanofMin, _stddevofMin])

        for _case, _caseValue in result_mem_dict.items():
            print(_case)
            with open('{outpath}/{case}-MEM-Final-Results.csv'.format(outpath=_OUT_PATH, case=_case), mode='w') as mem_resultsfile:
                fieldnames = ['Docker Container', 'MEM Mean', 'MEM SD', 'MEM Max', 'MEM Max SD', 'MEM Min', 'MEM Min SD']
                writer = csv.writer(mem_resultsfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(fieldnames)

                for _docker, _dockerValue in _caseValue.items():

                    _dockerName = _docker
                    _meanofMeans = statistics.mean([_dockerValue[v]['mean'] for v in _dockerValue])
                    _stddevofMeans = statistics.pstdev([_dockerValue[v]['mean'] for v in _dockerValue])

                    _meanofMax = statistics.mean([_dockerValue[v]['max'] for v in _dockerValue])
                    _stddevofMax = statistics.pstdev([_dockerValue[v]['max'] for v in _dockerValue])

                    _meanofMin = statistics.mean([_dockerValue[v]['min'] for v in _dockerValue])
                    _stddevofMin = statistics.pstdev([_dockerValue[v]['min'] for v in _dockerValue])

                    # print(_dockerName)
                    # print(_dockerValue["1"]["mean"], _dockerValue["2"]["mean"], _dockerValue["3"]["mean"])
                    # print(_meanofMeans)
                    # print(_stddevofMeans)
                    # print(_meanofMax)
                    # print(_meanofMin)

                    writer.writerow([_dockerName, _meanofMeans, _stddevofMeans, _meanofMax, _stddevofMax, _meanofMin, _stddevofMin])



if SYSTEM:

    with open('{outpath}/System-CPU-Final-Results.csv'.format(outpath=out_folder), mode='w') as system_cpu_resultsfile:
        fieldnames = ['Instances', 'CPU Mean', 'CPU SD', 'CPU Max', 'CPU Max SD', 'CPU Min', 'CPU Min SD' ]
        writer = csv.writer(system_cpu_resultsfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(fieldnames)
        for _instances, _runV in  result_sys_cpu_dict.items():

            _meanofMeans = statistics.mean([_runV[v]['mean'] for v in _runV])
            _stddevofMeans = statistics.pstdev([_runV[v]['mean'] for v in _runV])

            _meanofMax = statistics.mean([_runV[v]['max'] for v in _runV])
            _stddevofMax = statistics.pstdev([_runV[v]['max'] for v in _runV])

            _meanofMin = statistics.mean([_runV[v]['min'] for v in _runV])
            _stddevofMin = statistics.pstdev([_runV[v]['min'] for v in _runV])

            writer.writerow([_instances, _meanofMeans, _stddevofMeans, _meanofMax, _stddevofMax, _meanofMin, _stddevofMin])

    with open('{outpath}/System-RAM-Final-Results.csv'.format(outpath=out_folder), mode='w') as system_ram_resultsfile:
        fieldnames = ['Instances', 'MEM Mean', 'MEM SD', 'MEM Max', 'MEM Max SD', 'MEM Min', 'MEM Min SD']
        writer = csv.writer(system_ram_resultsfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(fieldnames)
        for _instances, _runV in  result_sys_ram_dict.items():

            _meanofMeans = statistics.mean([_runV[v]['mean'] for v in _runV])
            _stddevofMeans = statistics.pstdev([_runV[v]['mean'] for v in _runV])

            _meanofMax = statistics.mean([_runV[v]['max'] for v in _runV])
            _stddevofMax = statistics.pstdev([_runV[v]['max'] for v in _runV])

            _meanofMin = statistics.mean([_runV[v]['min'] for v in _runV])
            _stddevofMin = statistics.pstdev([_runV[v]['min'] for v in _runV])

            writer.writerow([_instances, _meanofMeans, _stddevofMeans, _meanofMax, _stddevofMax, _meanofMin, _stddevofMin])


if DOCKERS:
    for _docker, _dockerValue in result_docker_cpu_dict.items():
        _docker = _docker.split('_')[1]
        if not _docker in SELECTED_DOCKERS:
            continue
        print(_docker)
        with open('{outpath}/{docker}-CPU-Docker-Final-Results.csv'.format(outpath=out_folder, docker=_docker), mode='w') as cpu_resultsfile:
            fieldnames = ['Instances', 'CPU Mean', 'CPU SD', 'CPU Max', 'CPU Max SD', 'CPU Min', 'CPU Min SD' ]

            writer = csv.writer(cpu_resultsfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(fieldnames)

            for _case, _caseValue in _dockerValue.items():
                _caseName = _case
                _meanofMeans = statistics.mean([_caseValue[v]['mean'] for v in _caseValue])
                _stddevofMeans = statistics.pstdev([_caseValue[v]['mean'] for v in _caseValue])

                _meanofMax = statistics.mean([_caseValue[v]['max'] for v in _caseValue])
                _stddevofMax = statistics.pstdev([_caseValue[v]['max'] for v in _caseValue])

                _meanofMin = statistics.mean([_caseValue[v]['min'] for v in _caseValue])
                _stddevofMin = statistics.pstdev([_caseValue[v]['min'] for v in _caseValue])

                writer.writerow([_caseName, _meanofMeans, _stddevofMeans, _meanofMax, _stddevofMax, _meanofMin, _stddevofMin])


    for _docker, _dockerValue in result_docker_mem_dict.items():
        _docker = _docker.split('_')[1]
        if not _docker in SELECTED_DOCKERS:
            continue
        print(_docker)

        with open('{outpath}/{docker}-MEM-Docker-Final-Results.csv'.format(outpath=out_folder, docker=_docker), mode='w') as mem_resultsfile:
            fieldnames = ['Instances', 'MEM Mean', 'MEM SD', 'MEM Max', 'MEM Max SD', 'MEM Min', 'MEM Min SD']
            writer = csv.writer(mem_resultsfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(fieldnames)

            for _case, _caseValue in _dockerValue.items():
                _caseName = _case
                _meanofMeans = statistics.mean([_caseValue[v]['mean'] for v in _caseValue])
                _stddevofMeans = statistics.pstdev([_caseValue[v]['mean'] for v in _caseValue])

                _meanofMax = statistics.mean([_caseValue[v]['max'] for v in _caseValue])
                _stddevofMax = statistics.pstdev([_caseValue[v]['max'] for v in _caseValue])

                _meanofMin = statistics.mean([_caseValue[v]['min'] for v in _caseValue])
                _stddevofMin = statistics.pstdev([_caseValue[v]['min'] for v in _caseValue])

                writer.writerow([_caseName, _meanofMeans, _stddevofMeans, _meanofMax, _stddevofMax, _meanofMin, _stddevofMin])


print("Total time: {}".format(time.time() - start_time))

