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

_PATH = "/home/ashwin/Documents/WHB-Hadi/ScalabilityPaper/FINAL-150-3000rpm/150-final-1/150"
_OUT_PATH = "/home/ashwin/Documents/MSc/pg-scramble/MANO-Benchmarking-Framework/results/vim-mocker/Final"


RPM = True
DOCKERS = False
CASES = False

SKIP_COMPLETE = False

def average_cpu (csv_filepath):
    # print(ntpath.basename(csv_filepath))
    df=pd.read_csv(csv_filepath)

    df['totalcpu'] = df['user'] + df['system'] 

    _max = df['totalcpu'].max()
    _min = df['totalcpu'].min()
    _mean = df['totalcpu'].mean()

    print("CPU Mean: {} \t Min: {} \t Max: {} \n".format( _mean, _min, _max))
    return {"mean": float(_mean), "min": float(_min), "max": float(_max)} 

def average_mem(csv_filepath):
    # print(ntpath.basename(csv_filepath))
    df=pd.read_csv(csv_filepath)

    _max = df['ram'].max()
    _min = df['ram'].min()
    _mean = df['ram'].mean()

    print("MEM Mean: {} \t Min: {} \t Max: {} \n".format( _mean, _min, _max))
    return {"mean": float(_mean), "min": float(_min), "max": float(_max)} 

start_time = time.time()

cpu_files = [y for x in os.walk(_PATH) for y in glob(os.path.join(x[0], '*-cpu.csv'))]
mem_files = [y for x in os.walk(_PATH) for y in glob(os.path.join(x[0], '*-mem_usage.csv'))]

result_cpu_dict = {}
result_mem_dict = {}
result_docker_cpu_dict = {}
result_docker_mem_dict = {}
result_rpm_cpu_dict = {}
result_rpm_mem_dict = {}

for _cpu_file in cpu_files:
    print(Path(_cpu_file).parent.name)
    print(Path(_cpu_file).name)

    if ntpath.basename(_cpu_file) == "system-cpu.csv":
        continue

    _case, _run = Path(_cpu_file).parent.name.split("_Run")

    if SKIP_COMPLETE:
        if "Complete" not in _run:
            continue

    _run = _run.split("-")[0]
    _rpm = _case.split("-")[1].split("_rpm")[1]
    _case = _case.split("-")[1]

    _docker = Path(_cpu_file).name
    _docker = _docker.split(".")[0]

    if not _docker in result_docker_cpu_dict:
        result_docker_cpu_dict[_docker] = {}

    if not _case in result_docker_cpu_dict[_docker]:
        result_docker_cpu_dict[_docker][_case] = {}


    if not _docker in result_rpm_cpu_dict:
        result_rpm_cpu_dict[_docker] = {}

    if not _rpm in result_rpm_cpu_dict[_docker]:
        result_rpm_cpu_dict[_docker][_rpm] = {}


    if not _case in result_cpu_dict:
        result_cpu_dict[_case] = {}

    if not _docker in result_cpu_dict[_case]:
        result_cpu_dict[_case][_docker] = {}

    # average_cpu(_cpu_file)

    result_cpu_dict[_case][_docker][_run] = average_cpu(_cpu_file)
    result_docker_cpu_dict[_docker][_case][_run] = average_cpu(_cpu_file)
    result_rpm_cpu_dict[_docker][_rpm][_run] = average_cpu(_cpu_file)

for _mem_file in mem_files:
    print(Path(_mem_file).parent.name)
    print(Path(_mem_file).name)

    _case, _run = Path(_mem_file).parent.name.split("_Run")

    if SKIP_COMPLETE:
        if "Complete" not in _run:
            continue

    _run = _run.split("-")[0]
    _rpm = _case.split("-")[1].split("_rpm")[1]
    _case = _case.split("-")[1]

    _docker = Path(_mem_file).name
    _docker = _docker.split(".")[0]

    if not _docker in result_docker_mem_dict:
        result_docker_mem_dict[_docker] = {}

    if not _case in result_docker_mem_dict[_docker]:
        result_docker_mem_dict[_docker][_case] = {}

    if not _docker in result_rpm_mem_dict:
        result_rpm_mem_dict[_docker] = {}

    if not _rpm in result_rpm_mem_dict[_docker]:
        result_rpm_mem_dict[_docker][_rpm] = {}

    if not _case in result_mem_dict:
        result_mem_dict[_case] = {}

    if not _docker in result_mem_dict[_case]:
        result_mem_dict[_case][_docker] = {}

    result_mem_dict[_case][_docker][_run] = average_mem(_mem_file)
    result_docker_mem_dict[_docker][_case][_run] = average_mem(_mem_file)
    result_rpm_mem_dict[_docker][_rpm][_run] = average_mem(_mem_file)


print(json.dumps(result_cpu_dict, sort_keys=True, indent=4))
print(json.dumps(result_mem_dict, sort_keys=True, indent=4))

if DOCKERS:
    for _docker, _dockerValue in result_docker_cpu_dict.items():
        print(_docker)
        with open('{outpath}/{docker}-CPU-Docker-Final-Results.csv'.format(outpath=_OUT_PATH, docker=_docker), mode='w') as cpu_resultsfile:
            fieldnames = ['Case', 'CPU Mean', 'CPU SD', 'CPU Max', 'CPU Max SD', 'CPU Min', 'CPU Min SD' ]

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
        print(_docker)
        with open('{outpath}/{docker}-MEM-Docker-Final-Results.csv'.format(outpath=_OUT_PATH, docker=_docker), mode='w') as mem_resultsfile:
            fieldnames = ['Case', 'MEM Mean', 'MEM SD', 'MEM Max', 'MEM Max SD', 'MEM Min', 'MEM Min SD']
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

# RPM
if RPM:
    for _docker, _dockerValue in result_rpm_cpu_dict.items():
        print(_docker)
        with open('{outpath}/{docker}-CPU-RPM-Final-Results.csv'.format(outpath=_OUT_PATH, docker=_docker), mode='w') as cpu_resultsfile:
            fieldnames = ['RPM', 'CPU Mean', 'CPU SD', 'CPU Max', 'CPU Max SD', 'CPU Min', 'CPU Min SD' ]

            writer = csv.writer(cpu_resultsfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(fieldnames)

            for _rpm, _caseValue in _dockerValue.items():
                _caseName = _rpm
                _meanofMeans = statistics.mean([_caseValue[v]['mean'] for v in _caseValue])
                _stddevofMeans = statistics.pstdev([_caseValue[v]['mean'] for v in _caseValue])

                _meanofMax = statistics.mean([_caseValue[v]['max'] for v in _caseValue])
                _stddevofMax = statistics.pstdev([_caseValue[v]['max'] for v in _caseValue])

                _meanofMin = statistics.mean([_caseValue[v]['min'] for v in _caseValue])
                _stddevofMin = statistics.pstdev([_caseValue[v]['min'] for v in _caseValue])

                writer.writerow([_caseName, _meanofMeans, _stddevofMeans, _meanofMax, _stddevofMax, _meanofMin, _stddevofMin])


    for _docker, _dockerValue in result_rpm_mem_dict.items():
        print(_docker)
        with open('{outpath}/{docker}-MEM-RPM-Final-Results.csv'.format(outpath=_OUT_PATH, docker=_docker), mode='w') as mem_resultsfile:
            fieldnames = ['RPM', 'MEM Mean', 'MEM SD', 'MEM Max', 'MEM Max SD', 'MEM Min', 'MEM Min SD']
            writer = csv.writer(mem_resultsfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(fieldnames)

            for _rpm, _caseValue in _dockerValue.items():
                _caseName = _rpm
                _meanofMeans = statistics.mean([_caseValue[v]['mean'] for v in _caseValue])
                _stddevofMeans = statistics.pstdev([_caseValue[v]['mean'] for v in _caseValue])

                _meanofMax = statistics.mean([_caseValue[v]['max'] for v in _caseValue])
                _stddevofMax = statistics.pstdev([_caseValue[v]['max'] for v in _caseValue])

                _meanofMin = statistics.mean([_caseValue[v]['min'] for v in _caseValue])
                _stddevofMin = statistics.pstdev([_caseValue[v]['min'] for v in _caseValue])

                writer.writerow([_caseName, _meanofMeans, _stddevofMeans, _meanofMax, _stddevofMax, _meanofMin, _stddevofMin])


# RPM END
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



print("Total time: {}".format(time.time() - start_time))

