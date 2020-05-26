from concurrent.futures import ThreadPoolExecutor

from wrappers import SONATAClient
import time
import json
import requests
from urllib.request import urlopen
import csv
import os
import docker
from dateutil import parser
import threading

from keystoneauth1.identity import v3
from keystoneauth1 import session
from heatclient import client as hclient
from novaclient import client as nvclient

DOCKER_EXCLUDE = []

IDLE_SLEEP = 1

# Time between each run
INTER_EXPERIMENT_SLEEP = 10

# Consider experiment stopped after 5 * 10s of no update
NO_ACTIVITY_COUNT = 5

USERNAME = "pishahang"
PASSWORD = "1234"
HOST_URL = "131.234.28.240"
APP_SERVER_PORT = 5055

EXPERIMENT_REFERENCE = "EXPERIMENT_FIRST_TRIAL-2"
IMAGES = ["cirros"]

# INSTANCES = list(range(10, 400, 10))
INSTANCES = [100, 200]
CASES = [1]
RUNS = 2

# REQUESTS_PER_MINUTE = list(range(800, 1401, 200))
# REQUESTS_PER_MINUTE = [100]

# Restarting pishahang doesnt work with default installation!
RESTART_PISHAHANG = True
RESTART_MOCKER = False

IS_EXPERIMENT_VNF_INSTANCES_BASED = False
SKIP_EXPERIMENT_IF_ERRORS = True

cases_vnfs = {
    1: 1,
    2: 3,
    3: 5
}

# 131.234.28.240:5000/del_requests

def run_async(func):
	from threading import Thread
	from functools import wraps

	@wraps(func)
	def async_func(*args, **kwargs):
		func_hl = Thread(target = func, args = args, kwargs = kwargs)
		func_hl.start()
		return func_hl

	return async_func

def remove_requests(host=HOST_URL, port=APP_SERVER_PORT) :
    _base_path = 'http://{0}:{1}/del_requests'.format(host, port)

    try:
        r = requests.get(_base_path, verify=False)
        print(r.text)
    except Exception as e:
        print("Scale debug could'nt be set")

def restart_pishahang(host=HOST_URL, port=APP_SERVER_PORT) :
    _base_path = 'http://{0}:{1}/restart_pishahang'.format(host, port)

    try:
        r = requests.get(_base_path, verify=False)
        print(r.text)
    except Exception as e:
        print("Restart Pishahang")

def restart_mocker(host=HOST_URL, port=APP_SERVER_PORT) :
    _base_path = 'http://{0}:{1}/restart_mocker'.format(host, port)

    try:
        r = requests.get(_base_path, verify=False)
        print(r.text)
    except Exception as e:
        print("Restart Pishahang")

def get_pishahang_status(host=HOST_URL, port=APP_SERVER_PORT):
    _base_path = 'http://{0}:{1}/get_pishahang_status'.format(host, port)

    try:
        r = requests.get(_base_path, verify=False)
        print(r.text)
        return tuple(int(x) for x in r.text.split(","))
    except Exception as e:
        print("Get status Pishahang")

def get_pishahang_init_times(host=HOST_URL, port=APP_SERVER_PORT):
    _base_path = 'http://{0}:{1}/get_pishahang_init_times'.format(host, port)

    try:
        r = requests.get(_base_path, verify=False)
        print(r.text)
        return str(r.text)
    except Exception as e:
        print("Get status Pishahang")

def get_pishahang_docker_list(host=HOST_URL, port=APP_SERVER_PORT):
    _base_path = 'http://{0}:{1}/get_docker_names'.format(host, port)

    try:
        r = requests.get(_base_path, verify=False)
        print(r.text)
        return json.loads(r.text)
    except Exception as e:
        print("get_docker_names")

def sonata_cleanup():

    print("Sonata NSD/VNFD Cleanup")

    _token = json.loads(sonata_auth.auth(
                    username=USERNAME,
                    password=PASSWORD))
    _token = json.loads(_token["data"])

    nsd_list = json.loads(sonata_nsd.get_ns_descriptors(
                        token=_token["token"]["access_token"], limit=1000))
    nsd_list = json.loads(nsd_list["data"])

    print(len(nsd_list))
    for _nsd in nsd_list:
        sonata_nsd.delete_ns_descriptors_nsdinfoid(
                    token=_token["token"]["access_token"],
                    nsdinfoid=_nsd["uuid"]) 

    nsd_list = json.loads(sonata_nsd.get_ns_descriptors(
                        token=_token["token"]["access_token"]))
    nsd_list = json.loads(nsd_list["data"])

    # Delete VNFDs

    vnf_list = json.loads(sonata_vnfpkgm.get_vnf_packages(
                        token=_token["token"]["access_token"], limit=1000))
    vnf_list = json.loads(vnf_list["data"])

    for _vnfd in vnf_list:
        sonata_vnfpkgm.delete_vnf_packages_vnfpkgid(token=_token["token"]["access_token"], vnfPkgId=_vnfd["uuid"]) 

    vnf_list = json.loads(sonata_vnfpkgm.get_vnf_packages(
                        token=_token["token"]["access_token"]))
    vnf_list = json.loads(vnf_list["data"])

    time.sleep(5)

# http://patorjk.com/software/taag/#p=display&h=1&v=1&f=ANSI%20Shadow&t=OSM%20%0AExperiment
print("""


██████╗ ██╗███████╗██╗  ██╗ █████╗ ██╗  ██╗ █████╗ ███╗   ██╗ ██████╗            
██╔══██╗██║██╔════╝██║  ██║██╔══██╗██║  ██║██╔══██╗████╗  ██║██╔════╝            
██████╔╝██║███████╗███████║███████║███████║███████║██╔██╗ ██║██║  ███╗           
██╔═══╝ ██║╚════██║██╔══██║██╔══██║██╔══██║██╔══██║██║╚██╗██║██║   ██║           
██║     ██║███████║██║  ██║██║  ██║██║  ██║██║  ██║██║ ╚████║╚██████╔╝           
╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝            
███████╗██╗  ██╗██████╗ ███████╗██████╗ ██╗███╗   ███╗███████╗███╗   ██╗████████╗
██╔════╝╚██╗██╔╝██╔══██╗██╔════╝██╔══██╗██║████╗ ████║██╔════╝████╗  ██║╚══██╔══╝
█████╗   ╚███╔╝ ██████╔╝█████╗  ██████╔╝██║██╔████╔██║█████╗  ██╔██╗ ██║   ██║   
██╔══╝   ██╔██╗ ██╔═══╝ ██╔══╝  ██╔══██╗██║██║╚██╔╝██║██╔══╝  ██║╚██╗██║   ██║   
███████╗██╔╝ ██╗██║     ███████╗██║  ██║██║██║ ╚═╝ ██║███████╗██║ ╚████║   ██║   
╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   
██████╗ ██╗   ██╗███╗   ██╗███╗   ██╗███████╗██████╗                             
██╔══██╗██║   ██║████╗  ██║████╗  ██║██╔════╝██╔══██╗                            
██████╔╝██║   ██║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝                            
██╔══██╗██║   ██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗                            
██║  ██║╚██████╔╝██║ ╚████║██║ ╚████║███████╗██║  ██║                            
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝                            
                                                                                                                                                                  

                
""")

remove_requests()

TOTAL_EXPERIMENT_TIME = time.time()

for _image in IMAGES:
    for _case in CASES:
        for _instances in INSTANCES:
            # for _rpm in REQUESTS_PER_MINUTE:
            for _run in range(1, RUNS+1):
                try:
                    _rpm = _instances
                    remove_requests()
                    print("{image}_case{case}_{instances}_Run{run}".format(image=_image, case=_case, instances=_instances, run=_run))
                    # NO_INSTANCES = _instances
                    NSNAME = "{image}_case{case}-{_id}"
                    NSDESCRIPTION = "{image}_case{case}_{instances}_rpm{rpm}_Run{run}".format(image=_image, case=_case, instances=_instances, rpm=_rpm, run=_run)


                    NSD_PATH = "/app/SONATA/Descriptors/CASE{case}/{image}_case{case}_nsd_sonata.yml".format(image=_image, case=_case)
                    # VNFD_PATHS = ["/app/SONATA/Descriptors/CASE{case}/{image}_vnfd.1.yml".format(image=_image, case=_case), "/app/SONATA/Descriptors/CASE{case}/{image}_vnfd.2.yml".format(image=_image, case=_case), "/app/SONATA/Descriptors/CASE{case}/{image}_vnfd.3.yml".format(image=_image, case=_case), "/app/SONATA/Descriptors/CASE{case}/{image}_vnfd.4.yml".format(image=_image, case=_case), "/app/SONATA/Descriptors/CASE{case}/{image}_vnfd.5.yml".format(image=_image, case=_case)]
                    with open(NSD_PATH, 'r') as file:
                        nsd_data = file.read()

                    # with open(VNFD_PATH, 'r') as file:
                    #     vnfd_data = file.read()

                    sonata_nsd = SONATAClient.Nsd(HOST_URL)
                    sonata_nslcm = SONATAClient.Nslcm(HOST_URL) 
                    sonata_auth = SONATAClient.Auth(HOST_URL)
                    sonata_vnfpkgm = SONATAClient.VnfPkgm(HOST_URL)

                    experiment_timestamps = {}

                    sonata_cleanup()

                    _token = json.loads(sonata_auth.auth(
                                    username=USERNAME,
                                    password=PASSWORD))
                    _token = json.loads(_token["data"])


                    for _c in range(1, 6):
                        # for _vnfd in VNFD_PATHS:
                        VNFD_PATH = "/app/SONATA/Descriptors/CASE{case}/{image}_vnfd_{vnfid}.yml".format(image=_image, case=_case, vnfid=_c)
                        _res = sonata_vnfpkgm.post_vnf_packages(token=_token,
                            package_path=VNFD_PATH)
                        # print(_res)
                        time.sleep(0.5)

                    if IS_EXPERIMENT_VNF_INSTANCES_BASED:
                        no_instantiate = int(_instances/cases_vnfs[_case])
                    else:
                        no_instantiate = _instances

                    print("Instantiating {0} NS instances".format(no_instantiate))

                    # for i in range(0, no_instantiate):

                    with open("/tmp/" + NSNAME.format(_id=str(0), image=_image, case=_case) + "nsd.yml", "w") as _file:
                        _file.write(nsd_data.format(_id=0))

                    _res = sonata_nsd.post_ns_descriptors(token=_token,
                        package_path="/tmp/" + NSNAME.format(_id=str(0), image=_image, case=_case) + "nsd.yml")
                    # print(_res)
                    time.sleep(0.5)

                    print("PHASE 1 : Recording idle metrics...")
                    experiment_timestamps["start_time"] = int(time.time())

                    time.sleep(IDLE_SLEEP)

                    print("PHASE 2 : Starting Instantiation Sequence...")

                    experiment_timestamps["ns_inst_time"] = int(time.time())

                    _token = json.loads(sonata_auth.auth(username=USERNAME, password=PASSWORD))
                    _token = json.loads(_token["data"])

                    _nsd_list = json.loads(sonata_nsd.get_ns_descriptors(token=_token["token"]["access_token"], limit=1000))
                    _nsd_list = json.loads(_nsd_list["data"])

                    print(len(_nsd_list))

                    def createFolder(directory):
                        try:
                            if not os.path.exists(directory):
                                os.makedirs(directory)
                        except OSError:
                            print ('Error: Creating directory. ' + directory)

                    nit = "./EXP_RESULTS/{0}/{1}/{2}-{3}".format(EXPERIMENT_REFERENCE, no_instantiate, str(experiment_timestamps["ns_inst_time"]), NSDESCRIPTION)
                    createFolder("{nit}/".format(nit=nit))
                    experiment_complete = False
                    experiment_missing = 0

                    def successRatioThread():
                        global experiment_complete
                        global experiment_missing
                        # TIME_OUT = 60*NS_TERMINATION_SLEEP
                        TIME_OUT = no_instantiate * 60
                        QUERY_FREQUENCY = 10
                        COUNTER = 0

                        with open('{nit}/success-ratio.csv'.format(nit=nit), 'w') as _file:
                            _file.write("Time,Total,Active,Build,Error\n")
                            if IS_EXPERIMENT_VNF_INSTANCES_BASED:
                                TOTAL_INSTANCES = _instances
                            else:
                                TOTAL_INSTANCES = _instances

                            _sr_old = "0,0,0"
                            _no_change_count = -1

                            while(COUNTER < TIME_OUT):
                                try:
                                    # _requests = json.loads(sonata_nslcm.get_ns_instances_request_status(
                                    #                             token=_token["token"]["access_token"], limit=1000))
                                    # _requests = json.loads(_requests["data"])

                                    ACTIVE_INSTANCES, BUILD_INSTANCES, ERROR_INSTANCES = get_pishahang_status()
                                    experiment_missing = TOTAL_INSTANCES - ACTIVE_INSTANCES
                                    _successratio = "{time},{total},{active},{build},{error}\n".format(
                                                        time=(int(time.time())),
                                                        total=(max(0, TOTAL_INSTANCES)),
                                                        active=(max(0, ACTIVE_INSTANCES)),
                                                        build=(max(0, BUILD_INSTANCES)),
                                                        error=(max(0, ERROR_INSTANCES)))

                                    _sr_now = "{active},{build},{error}".format(
                                                        active=(max(0, ACTIVE_INSTANCES)),
                                                        build=(max(0, BUILD_INSTANCES)),
                                                        error=(max(0, ERROR_INSTANCES)))

                                    if _sr_old == _sr_now:
                                        _no_change_count += 1
                                        print("No activity increased: ", str(_no_change_count))
                                        if _no_change_count > NO_ACTIVITY_COUNT:
                                            print("ERROR: Stopping due to no activity")
                                            break
                                    else:
                                        _no_change_count = 0


                                    print(_successratio)
                                    print("###")
                                    
                                    _sr_old = _sr_now
                                    
                                    _file.write(_successratio)

                                    if (ACTIVE_INSTANCES + ERROR_INSTANCES) == TOTAL_INSTANCES:
                                        if ACTIVE_INSTANCES == TOTAL_INSTANCES:
                                            experiment_complete = True

                                        experiment_timestamps["end_to_end_lifecycle_time"] = int(time.time())-int(experiment_timestamps["ns_inst_time"])
                                        print("END-TO-END Time {enetime}".format( enetime=experiment_timestamps["end_to_end_lifecycle_time"]))
                                        break

                                    if SKIP_EXPERIMENT_IF_ERRORS:
                                        if ERROR_INSTANCES > 0:
                                            print("Skipping Experiment Due To Errors")
                                            break

                                    experiment_timestamps["end_to_end_lifecycle_time"] = int(time.time())-int(experiment_timestamps["ns_inst_time"])

                                except Exception as e:
                                    print(e)
                                    print("ERROR OpenStack")

                                time.sleep(QUERY_FREQUENCY)
                                COUNTER += QUERY_FREQUENCY

                    successThread = threading.Thread(target=successRatioThread)
                    successThread.start()

                    individual_init_times = {}

                    @run_async
                    def init_task(token, ns, i):
                        try:
                            print("{} - Took {}".format(i, time.time() - _start))
                            response = sonata_nslcm.post_ns_instances_nsinstanceid_instantiate(
                                            token=token, nsInstanceId=ns)

                            response = json.loads( response )

                            if response["error"]:
                                print(response)
                                print("ERROR - init request uuid")

                        except Exception as e:
                            print("Init Task")
                            print(e)
                            print(response)

                    _start = time.time()
                    for i in range(0, no_instantiate):
                        _ns = None
                        for _n in _nsd_list:
                            if NSNAME.format(_id=str(0), image=_image, case=_case) == _n['nsd']['name']:            
                                _ns = _n['uuid']
                                # print("UUID")
                                # print(_ns)
                                continue

                        if _ns:
                            init_task(_token["token"]["access_token"], _ns, i)

                            individual_init_times[i] = time.time()

                        else:
                            print("ERROR - no ns uuid")

                        #print(response)
                        # time.sleep(0.1) - 0.1 sleep not working with pishahang                    
                        time.sleep(60/_rpm)

                    # Helpers._delete_test_nsd("test_osm_cirros_2vnf_nsd")
                    experiment_timestamps["ns_inst_end_time"] = int(time.time())

                    print("PHASE 2 : Recording Metrics Post NS instantiation...")

                    successThread.join()

                    print("PHASE 3 : Starting Termination Sequence...")
                    experiment_timestamps["ns_term_start_time"] = int(time.time())

                    _token = json.loads(sonata_auth.auth(username=USERNAME, password=PASSWORD))
                    _token = json.loads(_token["data"])

                    _nsd_list = json.loads(sonata_nsd.get_ns_descriptors(
                                            token=_token["token"]["access_token"], limit=1000))
                    _nsd_list = json.loads(_nsd_list["data"])

                    _ns_list = json.loads(sonata_nslcm.get_ns_instances(
                                            token=_token["token"]["access_token"], limit=1000))
                    _ns_list = json.loads(_ns_list["data"])

                    # get_individual_times(individual_init_times, nit, experiment_timestamps["ns_inst_time"], _ns_list)

                    _ns = None
                    for _n in _nsd_list:
                        try:
                            if NSNAME.format(_id=str(i), image=_image, case=_case) == _n['nsd']['name']:
                                # TODO: Print status
                                for _n2 in _ns_list:
                                    if _n['uuid'] == _n2['descriptor_reference']:
                                        _ns = _n2['uuid']
                                        response = json.loads(
                                                    sonata_nslcm.post_ns_instances_nsinstanceid_terminate(
                                                        token=_token["token"]["access_token"], nsInstanceId=_ns))
                        except Exception as e:
                            print(e)


                    experiment_timestamps["ns_term_end_time"] = int(time.time())

                    print("PHASE 3 : Recording Metrics Post NS ...")

                    time.sleep(IDLE_SLEEP)

                    experiment_timestamps["end_time"] = int(time.time())                                 

                    print("\n ########### FINISHED ########### \n")

                    print("Experiment Start Time {0}".format(experiment_timestamps["start_time"]))
                    print("Instantiation Start Time {0}".format(experiment_timestamps["ns_inst_time"]))
                    print("Instantiation End Time {0}".format(experiment_timestamps["ns_inst_end_time"]))
                    print("Termination Start Time {0}".format(experiment_timestamps["ns_term_start_time"]))
                    print("Termination End Time {0}".format(experiment_timestamps["ns_term_end_time"]))
                    print("Experiment End Time {0}".format(experiment_timestamps["end_time"]))

                    # TODO: Save all the data generated into csv file
                    #       + Use before, after and fetch csv data from url as it is in the html file and write it to a file, named accordingly
                    #       + Create a folder with the "ns_inst_time" as name
                    #       'http://osmmano.cs.upb.de:19999/api/v1/data?chart=system.cpu&format=csv&options=nonzero'


                    print("PHASE 4 : Saving Metrics  ...")

                    _charts = {
                        "system-cpu" : { 
                            "url": "http://{host}:19999/api/v1/data?chart=system.cpu&after={after}&before={before}&format=csv&options=nonzero".format(host=HOST_URL,after=experiment_timestamps["start_time"],before=experiment_timestamps["end_time"])
                        },
                        "system-load" : { 
                            "url": "http://{host}:19999/api/v1/data?chart=system.load&after={after}&before={before}&format=csv&options=nonzero".format(host=HOST_URL, after=experiment_timestamps['start_time'], before=experiment_timestamps["end_time"])
                        },
                        "system-ram" : { 
                            "url": "http://{host}:19999/api/v1/data?chart=system.ram&format=datasource&after={after}&before={before}&format=csv&options=nonzero".format(host=HOST_URL, after=experiment_timestamps['start_time'], before=experiment_timestamps["end_time"])
                        },
                        "system-net" : { 
                            "url": "http://{host}:19999/api/v1/data?chart=system.net&format=datasource&after={after}&before={before}&format=csv&group=average&gtime=0&datasource&options=nonzeroseconds".format(host=HOST_URL, after=experiment_timestamps["start_time"], before=experiment_timestamps["end_time"])
                        },
                        "system-io" : { 
                            "url": "http://{host}:19999/api/v1/data?chart=system.io&format=datasource&after={after}&before={before}&format=csv&group=average&gtime=0&datasource&options=nonzeroseconds".format(host=HOST_URL, after=experiment_timestamps["start_time"], before=experiment_timestamps["end_time"])
                        }
                        }

                    docker_list = get_pishahang_docker_list()

                    for _container, v in docker_list.items():
                        if not _container in DOCKER_EXCLUDE:
                                _charts["{0}-{1}".format(_container, "cpu")] = { "url" : "http://{host}:19999/api/v1/data?chart=cgroup_{_name}.cpu&format=csv&after={after}&before={before}&format=csv&group=average&gtime=0&datasource&options=nonzeroseconds".format(host=HOST_URL, after=experiment_timestamps["start_time"], before=experiment_timestamps["end_time"], _name=_container)}
                                _charts["{0}-{1}".format(_container, "throttle_io")] = { "url" : "http://{host}:19999/api/v1/data?chart=cgroup_{_name}.throttle_io&format=csv&after={after}&before={before}&format=csv&group=average&gtime=0&datasource&options=nonzeroseconds".format(host=HOST_URL, after=experiment_timestamps["start_time"], before=experiment_timestamps["end_time"], _name=_container)}
                                _charts["{0}-{1}".format(_container, "mem_usage")] = { "url" : "http://{host}:19999/api/v1/data?chart=cgroup_{_name}.mem_usage&format=csv&after={after}&before={before}&format=csv&group=average&gtime=0&datasource&options=nonzeroseconds".format(host=HOST_URL, after=experiment_timestamps["start_time"], before=experiment_timestamps["end_time"], _name=_container)}
                            
                    for _sc, value  in _charts.items():
                        print(_sc)
                        try:
                            # TODO: make verify=false as a fallback
                            r = requests.get(value["url"], verify=False)

                            if r.status_code == requests.codes.ok:
                                print("success")

                                with open('{nit}/{sc}.csv'.format(nit=nit,sc=_sc), 'w') as csv_file:
                                    csv_file.write(r.text)
                            else:
                                print("Failed")

                        except Exception as e:
                            print(str(e))


                    with open('{nit}/experiment-meta.md'.format(nit=nit), 'w') as _file:
                        _file.write("Experiment Description {0}\n\n".format(NSDESCRIPTION))
                        _file.write("Experiment Start Time {0}\n".format(experiment_timestamps["start_time"]))
                        _file.write("Instantiation Start Time {0}\n".format(experiment_timestamps["ns_inst_time"]))
                        _file.write("Instantiation End Time {0}\n".format(experiment_timestamps["ns_inst_end_time"]))
                        _file.write("Termination Start Time {0}\n".format(experiment_timestamps["ns_term_start_time"]))
                        _file.write("Termination End Time {0}\n".format(experiment_timestamps["ns_term_end_time"]))
                        _file.write("Experiment End Time {0}\n".format(experiment_timestamps["end_time"]))
                        _file.write("\nhttp://{host}:9000/interactive?host={host}&after={after}&before={before}&start_time={start_time}&ns_inst_time={ns_inst_time}&ns_inst_end_time={ns_inst_end_time}&ns_term_start_time={ns_term_start_time}&ns_term_end_time={ns_term_end_time}&end_time={end_time}&exp_description={exp_description}".format(host=HOST_URL, after=experiment_timestamps["start_time"], before=experiment_timestamps["end_time"],start_time=experiment_timestamps["start_time"],ns_inst_time=experiment_timestamps["ns_inst_time"],ns_inst_end_time=experiment_timestamps["ns_inst_end_time"],ns_term_start_time=experiment_timestamps["ns_term_start_time"],ns_term_end_time=experiment_timestamps["ns_term_end_time"],end_time=experiment_timestamps["end_time"],exp_description=NSDESCRIPTION))

                    with open('{nit}/end-to-end-time.csv'.format(nit=nit), 'w') as _file:
                        _file.write("end-to-end-time\n{0}".format(experiment_timestamps["end_to_end_lifecycle_time"]))
                    
                    with open('{nit}/individual-times.csv'.format(nit=nit), 'w') as _file:
                        _file.write("mean,std,max,min\n{0}".format(get_pishahang_init_times()))

                    print("Metrics saved in folder {nit}".format(nit=nit))

                    print("\nhttp://{host}:9000/?host={host}&after={after}&before={before}&start_time={start_time}&ns_inst_time={ns_inst_time}&ns_inst_end_time={ns_inst_end_time}&ns_term_start_time={ns_term_start_time}&ns_term_end_time={ns_term_end_time}&end_time={end_time}&exp_description={exp_description}".format(host=HOST_URL, after=experiment_timestamps["start_time"], before=experiment_timestamps["end_time"],start_time=experiment_timestamps["start_time"],ns_inst_time=experiment_timestamps["ns_inst_time"],ns_inst_end_time=experiment_timestamps["ns_inst_end_time"],ns_term_start_time=experiment_timestamps["ns_term_start_time"],ns_term_end_time=experiment_timestamps["ns_term_end_time"],end_time=experiment_timestamps["end_time"],exp_description=NSDESCRIPTION))

                    print("\nhttp://{host}:9000/interactive?host={host}&after={after}&before={before}&start_time={start_time}&ns_inst_time={ns_inst_time}&ns_inst_end_time={ns_inst_end_time}&ns_term_start_time={ns_term_start_time}&ns_term_end_time={ns_term_end_time}&end_time={end_time}&exp_description={exp_description}".format(host=HOST_URL, after=experiment_timestamps["start_time"], before=experiment_timestamps["end_time"],start_time=experiment_timestamps["start_time"],ns_inst_time=experiment_timestamps["ns_inst_time"],ns_inst_end_time=experiment_timestamps["ns_inst_end_time"],ns_term_start_time=experiment_timestamps["ns_term_start_time"],ns_term_end_time=experiment_timestamps["ns_term_end_time"],end_time=experiment_timestamps["end_time"],exp_description=NSDESCRIPTION))

                    print("\n\n\n\n\n\n ENDED \n\n\n\n\n\n")
                    if experiment_complete:
                        os.rename(nit, "{nit}-Complete".format(nit=nit))
                    else:
                        os.rename(nit, "{nit}-{active}".format(nit=nit, active=experiment_missing))                        
                    # delete_stacks()

                except Exception as e:
                    print(e)
                    print("failed RUN")

                if RESTART_PISHAHANG:
                    restart_pishahang()

                if RESTART_MOCKER:
                    restart_mocker()
                    
                time.sleep(INTER_EXPERIMENT_SLEEP)

print("Total experiment time: {}".format(time.time() - TOTAL_EXPERIMENT_TIME))