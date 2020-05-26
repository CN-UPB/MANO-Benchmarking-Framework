# import wrappers
# make method which does the following, take mano as parameter

# get start time
# sleep 5 min
# get NS instantiation time
# send instantiation request to osm/sonata

from wrappers import OSMClient
import time
import json
import requests
from urllib.request import urlopen
import csv
import os
import docker
from dateutil import parser
import threading
import uuid
import os
import statistics

from keystoneauth1.identity import v3
from keystoneauth1 import session
from novaclient import client as nvclient

client_docker = docker.DockerClient(base_url='unix://container/path/docker.sock')

DOCKER_EXCLUDE = ['']


IDLE_SLEEP = 1
NS_TERMINATION_SLEEP = 60 * 60 
INTER_EXPERIMENT_SLEEP = 45
NO_ACTIVITY_COUNT = 10
# NO_INSTANCES = 1

USERNAME = "admin"
PASSWORD = "admin"
HOST_URL = "thesismano3.cs.upb.de"
VIMACCOUNTID = "92d6eadc-9e3d-4439-994e-d8877d89864a"
APP_SERVER_PORT = 5055

# AUTH_URL = "http://131.234.250.117/identity/v3"
AUTH_URL = "http://10.0.1.2:6001/v2.0"
OS_USERNAME = "demo"
OS_PASSWORD = "1234"
OS_PROJECT = "demo"

EXPERIMENT_REFERENCE = "osm-containers-2"
IMAGES = ["cirros"]
# INSTANCES = list(range(10, 400, 10))
INSTANCES = [100, 200]
CASES = [1]
RUNS = 2
# REQUESTS_PER_MINUTE = list(range(30, 460, 30))
REQUESTS_PER_MINUTE = [100]

IS_EXPERIMENT_VNF_INSTANCES_BASED = True
SKIP_EXPERIMENT_IF_ERRORS = False


cases_vnfs = {
    1: 1,
    2: 3,
    3: 5
}

def run_async(func):
	from threading import Thread
	from functools import wraps

	@wraps(func)
	def async_func(*args, **kwargs):
		func_hl = Thread(target = func, args = args, kwargs = kwargs)
		func_hl.start()
		return func_hl

	return async_func


def restart_osm(host=HOST_URL, port=APP_SERVER_PORT) :
    _base_path = 'http://{0}:{1}/restart_osm'.format(host, port)

    try:
        r = requests.get(_base_path, verify=False)
        print(r.text)
        # return r.text
    except Exception as e:
        print("Restart OSM")

def osm_add_vim(host=HOST_URL, port=APP_SERVER_PORT) :
    _base_path = 'http://{0}:{1}/osm_add_vim'.format(host, port)

    try:
        r = requests.get(_base_path, verify=False)
        print(r.text)
        return r.text
    except Exception as e:
        print("Restart OSM")

def restart_mocker(host="thesismano2.cs.upb.de", port=APP_SERVER_PORT) :
    _base_path = 'http://{0}:{1}/restart_mocker'.format(host, port)

    try:
        r = requests.get(_base_path, verify=False)
        print(r.text)
    except Exception as e:
        print("Restart Pishahang")

def get_count(init_time, _ns_list):

    active_count = 0
    build_count = 0
    error_count = 0

    for _s in _ns_list:
        server_created = _s['create-time']
        if int(server_created) >= int(init_time) :
            if _s['nsState'] == "READY":
                active_count += 1
            elif _s['nsState'] == "BUILDING":
                build_count += 1
            elif _s['nsState'] == "BROKEN":
                error_count += 1
            else:
                print("Other Status")
                print(_s['nsState'])

    return active_count, build_count, error_count


def delete_instances():
    time.sleep(60)
    auth = v3.Password(auth_url=AUTH_URL,
                    username=OS_USERNAME,
                    password=OS_PASSWORD,
                    project_name=OS_PROJECT,
                    user_domain_id='default',
                    project_domain_id='default')

    sess = session.Session(auth=auth)

    nova = nvclient.Client('2', session=sess)

    _servers = nova.servers.list()

    for _s in _servers:
        try:
            _s.delete()
        except Exception as e:
            print(e)


def get_osm_init_times(ns_list):
    _ns = None
    init_times = []    
    for _n in ns_list:
        try:
            _ns = _n['_admin']['modified'] - _n['_admin']['created']
            init_times.append(_ns)

        except Exception as e:
            print("OSM Get Init")
            print(e)
            pass

    print(init_times)
    _result = "{mean},{std},{max},{min}".format(
        std=statistics.stdev(init_times),
        mean=statistics.mean(init_times),
        max=max(init_times),
        min=min(init_times)
    )

    return _result

def get_individual_times(individual_init_times, folder_path, init_time, _ns_list):
    auth = v3.Password(auth_url=AUTH_URL,
                    username=OS_USERNAME,
                    password=OS_PASSWORD,
                    project_name=OS_PROJECT,
                    user_domain_id='default',
                    project_domain_id='default')

    sess = session.Session(auth=auth)

    nova = nvclient.Client('2', session=sess)

    _servers = nova.servers.list()


    with open('{nit}/individual-build-times.csv'.format(nit=nit), 'w') as _file:
        _file.write("id,mano_time,ns_mano_time,vim_time\n")

        for _s in _servers:
            ns_init_time = next((item for item in _ns_list if item["short-name"] == "{}-{}".format(_s.name.split("-")[0], _s.name.split("-")[1])), False)
            if not ns_init_time:
                ns_init_time = 0
            else:
                ns_init_time = ns_init_time['create-time']

            server_created = parser.parse(_s.created)
            launch_time = parser.parse(_s.updated)
            if int(server_created.strftime("%s")) > int(init_time):
                # print(server_created.strftime("%s"), nsname, individual_init_times[int(_s.name.split("-")[1])])
                _mano_time = float(server_created.strftime("%s")) - float(individual_init_times[int(_s.name.split("-")[1])])
                ns_mano_time = float(server_created.strftime("%s")) - float(ns_init_time)
                _vim_time = float(launch_time.strftime("%s")) - float(server_created.strftime("%s"))

                print("{},{},{},{}\n".format(int(_s.name.split("-")[1]), _mano_time, ns_mano_time, _vim_time))
                _file.write("{},{},{},{}\n".format(int(_s.name.split("-")[1]), _mano_time, ns_mano_time, _vim_time))
    

    return

def get_osm_docker_list(host=HOST_URL, port=APP_SERVER_PORT):
    _base_path = 'http://{0}:{1}/get_docker_names'.format(host, port)

    try:
        r = requests.get(_base_path, verify=False)
        print(r.text)
        return json.loads(r.text)
    except Exception as e:
        print("get_docker_names")

osm_nsd = OSMClient.Nsd(HOST_URL)
osm_nslcm = OSMClient.Nslcm(HOST_URL) 
osm_auth = OSMClient.Auth(HOST_URL)

experiment_timestamps = {}

# http://patorjk.com/software/taag/#p=display&h=1&v=1&f=ANSI%20Shadow&t=OSM%20%0AExperiment
print("""


 ██████╗ ███████╗███╗   ███╗                                                     
██╔═══██╗██╔════╝████╗ ████║                                                     
██║   ██║███████╗██╔████╔██║                                                     
██║   ██║╚════██║██║╚██╔╝██║                                                     
╚██████╔╝███████║██║ ╚═╝ ██║                                                     
 ╚═════╝ ╚══════╝╚═╝     ╚═╝                                                     
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

for _image in IMAGES:
    for _case in CASES:
        for _instances in INSTANCES:
            # for _rpm in REQUESTS_PER_MINUTE:
            for _run in range(1, RUNS+1):
                _rpm = _instances
                try:
                    restart_mocker()
                    # restart_osm()
                    time.sleep(20)
                    # VIMACCOUNTID = osm_add_vim()
                    print("{image}_case{case}_{instances}_Run{run}".format(image=_image, case=_case, instances=_instances, run=_run))
                    # NO_INSTANCES = _instances
                    NSNAME = "{image}_case{case}".format(image=_image, case=_case)
                    nsdId = "{image}_case{case}-ns".format(image=_image, case=_case)
                    NSDESCRIPTION = "{image}_case{case}_{instances}_rpm{rpm}_Run{run}".format(image=_image, case=_case, instances=_instances, rpm=_rpm, run=_run)

                    print("PHASE 1 : Recording idle metrics...")
                    experiment_timestamps["start_time"] = int(time.time())

                    time.sleep(IDLE_SLEEP)

                    print("PHASE 2 : Starting Instantiation Sequence...")

                    experiment_timestamps["ns_inst_time"] = int(time.time())

                    _token = json.loads(osm_auth.auth(username=USERNAME, password=PASSWORD))
                    _token = json.loads(_token["data"])

                    _nsd_list = json.loads(osm_nsd.get_ns_descriptors(token=_token["id"]))
                    _nsd_list = json.loads(_nsd_list["data"])

                    _nsd = None
                    for _n in _nsd_list:
                        if nsdId == _n['id']:            
                            _nsd = _n['_id']
                    
                    # TODO: Calculate
                    if IS_EXPERIMENT_VNF_INSTANCES_BASED:
                        no_instantiate = int(_instances/cases_vnfs[_case])
                    else:
                        no_instantiate = _instances

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
                        # TIME_OUT = NS_TERMINATION_SLEEP
                        TIME_OUT = no_instantiate * 60
                        QUERY_FREQUENCY = 10
                        COUNTER = 0
                        print("Waiting Time: ", str(no_instantiate))

                        with open('{nit}/success-ratio.csv'.format(nit=nit), 'w') as _file:
                            _file.write("Time,Total,Active,Build,Error\n")
                            if IS_EXPERIMENT_VNF_INSTANCES_BASED:
                                TOTAL_INSTANCES = _instances
                            else:
                                TOTAL_INSTANCES = int(cases_vnfs[_case]*_instances)

                            _sr_old = "0,0,0"
                            _no_change_count = 0

                            while(COUNTER < TIME_OUT):
                                try:
                                    _ns_list_success = json.loads(osm_nslcm.get_ns_instances(token=_token["id"]))
                                    _ns_list_success = json.loads(_ns_list_success["data"])

                                    ACTIVE_INSTANCES, BUILD_INSTANCES, ERROR_INSTANCES = get_count(experiment_timestamps["ns_inst_time"], _ns_list_success)
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

                                    _sr_old = _sr_now

                                    _file.write(_successratio)

                                    if (ACTIVE_INSTANCES + ERROR_INSTANCES) == TOTAL_INSTANCES:
                                        if ACTIVE_INSTANCES == TOTAL_INSTANCES:
                                            experiment_complete = True
                                        experiment_timestamps["end_to_end_lifecycle_time"] = int(time.time())-int(experiment_timestamps["ns_inst_time"])
                                        print("{image}_case{case}_{instances}_Run{run}".format(image=_image, case=_case, instances=_instances, run=_run))
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
                    def init_task(token, uuid, i):
                        try:
                            print("{} - Took {}".format(i, time.time() - _start))
                            response = json.loads(osm_nslcm.post_ns_instances_nsinstanceid_instantiate(token=token,
                                        nsDescription=NSDESCRIPTION+uuid, 
                                        nsName="{}-{}-{}".format(NSNAME, i, uuid), 
                                        nsdId=_nsd, 
                                        vimAccountId=VIMACCOUNTID))

                            response = json.loads( response )
                            if response["error"]:
                                print(response)
                                print("ERROR - init request uuid")

                        except Exception as e:
                            print("Init Task")
                            print(e)
                            print(response)

                    _start = time.time()

                    print("Instantiating {0} NS instances".format(no_instantiate))
                    for i in range(0, no_instantiate):
                        _uuid = str(uuid.uuid4())
                        
                        init_task(_token["id"], _uuid, i)
                        individual_init_times[i] = time.time()
                        # Store init
                        time.sleep(60/_rpm)

                    # Helpers._delete_test_nsd("test_osm_cirros_2vnf_nsd")
                    experiment_timestamps["ns_inst_end_time"] = int(time.time())

                    print("PHASE 2 : Recording Metrics Post NS instantiation...")

                    successThread.join()

                    print("PHASE 3 : Starting Termination Sequence...")
                    experiment_timestamps["ns_term_start_time"] = int(time.time())

                    _token = json.loads(osm_auth.auth(username=USERNAME, password=PASSWORD))
                    _token = json.loads(_token["data"])

                    _ns_list = json.loads(osm_nslcm.get_ns_instances(token=_token["id"]))
                    _ns_list = json.loads(_ns_list["data"])

                    # get_individual_times(individual_init_times, nit, experiment_timestamps["ns_inst_time"], _ns_list)

                    _ns = None
                    print("Printing Status Of Instances...")
                    for _n in _ns_list:
                        try:
                            if nsdId == _n['nsd']['id']:            
                                _ns = _n['_id']
                                response = None

                                if "detailed-status" in _n:
                                    print(_n["detailed-status"])
                                else:
                                    print("detailed-status not available")

                                if _ns:
                                    response = json.loads(osm_nslcm.post_ns_instances_nsinstanceid_terminate(
                                                            token=_token["id"], 
                                                            nsInstanceId=_ns))
                                    # print(response)
                        except Exception as e:
                            pass

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

                    # docker_list = {}
                    # for _container in client_docker.containers.list():        
                    #     if not _container.attrs["Name"][1:] in DOCKER_EXCLUDE:
                    #             _charts["{0}-{1}".format(_container.attrs["Name"][1:], "cpu")] = { "url" : "http://{host}:19999/api/v1/data?chart=cgroup_{_name}.cpu&format=csv&after={after}&before={before}&format=csv&group=average&gtime=0&datasource&options=nonzeroseconds".format(host=HOST_URL, after=experiment_timestamps["start_time"], before=experiment_timestamps["end_time"], _name=_container.attrs["Name"][1:])}
                    #             _charts["{0}-{1}".format(_container.attrs["Name"][1:], "throttle_io")] = { "url" : "http://{host}:19999/api/v1/data?chart=cgroup_{_name}.throttle_io&format=csv&after={after}&before={before}&format=csv&group=average&gtime=0&datasource&options=nonzeroseconds".format(host=HOST_URL, after=experiment_timestamps["start_time"], before=experiment_timestamps["end_time"], _name=_container.attrs["Name"][1:])}
                    #             _charts["{0}-{1}".format(_container.attrs["Name"][1:], "mem_usage")] = { "url" : "http://{host}:19999/api/v1/data?chart=cgroup_{_name}.mem_usage&format=csv&after={after}&before={before}&format=csv&group=average&gtime=0&datasource&options=nonzeroseconds".format(host=HOST_URL, after=experiment_timestamps["start_time"], before=experiment_timestamps["end_time"], _name=_container.attrs["Name"][1:])}
                                
                    docker_list = get_osm_docker_list()

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
                        _file.write("Experiment Start Time {0}\n".format(experiment_timestamps["start_time"]))
                        _file.write("Instantiation Start Time {0}\n".format(experiment_timestamps["ns_inst_time"]))
                        _file.write("Instantiation End Time {0}\n".format(experiment_timestamps["ns_inst_end_time"]))
                        _file.write("Termination Start Time {0}\n".format(experiment_timestamps["ns_term_start_time"]))
                        _file.write("Termination End Time {0}\n".format(experiment_timestamps["ns_term_end_time"]))
                        _file.write("Experiment End Time {0}\n".format(experiment_timestamps["end_time"]))
                        _file.write("\nhttp://{host}:9000/interactive?host={host}&after={after}&before={before}&start_time={start_time}&ns_inst_time={ns_inst_time}&ns_inst_end_time={ns_inst_end_time}&ns_term_start_time={ns_term_start_time}&ns_term_end_time={ns_term_end_time}&end_time={end_time}&exp_description={exp_description}".format(host=HOST_URL, after=experiment_timestamps["start_time"], before=experiment_timestamps["end_time"],start_time=experiment_timestamps["start_time"],ns_inst_time=experiment_timestamps["ns_inst_time"],ns_inst_end_time=experiment_timestamps["ns_inst_end_time"],ns_term_start_time=experiment_timestamps["ns_term_start_time"],ns_term_end_time=experiment_timestamps["ns_term_end_time"],end_time=experiment_timestamps["end_time"],exp_description=NSDESCRIPTION))

                    _token = json.loads(osm_auth.auth(username=USERNAME, password=PASSWORD))
                    _token = json.loads(_token["data"])

                    _ns_list = json.loads(osm_nslcm.get_ns_instances(token=_token["id"]))
                    _ns_list = json.loads(_ns_list["data"])

                    with open('{nit}/end-to-end-time.csv'.format(nit=nit), 'w') as _file:
                        _file.write("end-to-end-time\n{0}".format(experiment_timestamps["end_to_end_lifecycle_time"]))

                    with open('{nit}/individual-times.csv'.format(nit=nit), 'w') as _file:
                        _file.write("mean,std,max,min\n{0}".format(get_osm_init_times(_ns_list)))

                    print("Metrics saved in folder {nit}".format(nit=nit))

                    print("\nhttp://{host}:9000/?host={host}&after={after}&before={before}&start_time={start_time}&ns_inst_time={ns_inst_time}&ns_inst_end_time={ns_inst_end_time}&ns_term_start_time={ns_term_start_time}&ns_term_end_time={ns_term_end_time}&end_time={end_time}&exp_description={exp_description}".format(host=HOST_URL, after=experiment_timestamps["start_time"], before=experiment_timestamps["end_time"],start_time=experiment_timestamps["start_time"],ns_inst_time=experiment_timestamps["ns_inst_time"],ns_inst_end_time=experiment_timestamps["ns_inst_end_time"],ns_term_start_time=experiment_timestamps["ns_term_start_time"],ns_term_end_time=experiment_timestamps["ns_term_end_time"],end_time=experiment_timestamps["end_time"],exp_description=NSDESCRIPTION))

                    print("\nhttp://{host}:9000/interactive?host={host}&after={after}&before={before}&start_time={start_time}&ns_inst_time={ns_inst_time}&ns_inst_end_time={ns_inst_end_time}&ns_term_start_time={ns_term_start_time}&ns_term_end_time={ns_term_end_time}&end_time={end_time}&exp_description={exp_description}".format(host=HOST_URL, after=experiment_timestamps["start_time"], before=experiment_timestamps["end_time"],start_time=experiment_timestamps["start_time"],ns_inst_time=experiment_timestamps["ns_inst_time"],ns_inst_end_time=experiment_timestamps["ns_inst_end_time"],ns_term_start_time=experiment_timestamps["ns_term_start_time"],ns_term_end_time=experiment_timestamps["ns_term_end_time"],end_time=experiment_timestamps["end_time"],exp_description=NSDESCRIPTION))

                    print("\n\n\n\n\n\n ENDED \n\n\n\n\n\n")
                    if experiment_complete:
                        os.rename(nit, "{nit}-Complete".format(nit=nit))
                    else:
                        os.rename(nit, "{nit}-{active}".format(nit=nit, active=experiment_missing))                        

                    # delete_instances()


                    # get_individual_times(individual_init_times, nit, experiment_timestamps["ns_inst_time"], _ns_list)

                    _ns = None
                    for _n in _ns_list:
                        try:
                            if nsdId == _n['nsd']['id']:            
                                _ns = _n['_id']
                                response = None

                                if _ns:
                                    response = json.loads(osm_nslcm.post_ns_instances_nsinstanceid_terminate(
                                                            token=_token["id"], 
                                                            nsInstanceId=_ns))
                                    # print(response)
                        except Exception as e:
                            pass

                    time.sleep(INTER_EXPERIMENT_SLEEP)

                    _token = json.loads(osm_auth.auth(username=USERNAME, password=PASSWORD))
                    _token = json.loads(_token["data"])

                    _ns_list = json.loads(osm_nslcm.get_ns_instances(token=_token["id"]))
                    _ns_list = json.loads(_ns_list["data"])


                    # get_individual_times(individual_init_times, nit, experiment_timestamps["ns_inst_time"], _ns_list)

                    _ns = None
                    for _n in _ns_list:
                        try:
                            if nsdId == _n['nsd']['id']:            
                                _ns = _n['_id']
                                response = None

                                if _ns:
                                    response = json.loads(osm_nslcm.post_ns_instances_nsinstanceid_terminate(
                                                            token=_token["id"], 
                                                            nsInstanceId=_ns,
                                                            force=True))
                                    # print(response)
                        except Exception as e:
                            pass

                    # restart_osm()
                    time.sleep(INTER_EXPERIMENT_SLEEP)
                    
                except Exception as e:
                    print(e)

                print("#####################\n\n EXPERIMENT DONE \n\n#####################")





