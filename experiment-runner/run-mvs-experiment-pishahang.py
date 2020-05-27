"""
A python script that can be used to instantiate a service in Pishahang remotely.
Requirements:
- Python3.6
- python-mano-wrappers
- Pishahang's credential
- Pishahang's IP address
- The service descriptor UUID
"""

import wrappers
import json
import threading
import time
import os

from kubernetes import client

from keystoneauth1.identity import v3
from keystoneauth1 import session
from novaclient import client as nvclient

from heatclient import client as hclient
from dateutil import parser

import requests

TERMINATE_NS = False
CLEAR_VIM = True
CLEAR_DESCRIPTORS = True

AUTH_URL = "http://131.234.250.116/identity/v3"
# AUTH_URL = "http://131.234.250.117/identity/v3"

K8_URL = "https://131.234.250.178"
HOST_URL = "thesismano1.cs.upb.de"
APP_SERVER_PORT = 5055


ATOKEN = "eyJhbGciOiJSUzI1NiIsImtpZCI6IiJ9.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJkZWZhdWx0Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZWNyZXQubmFtZSI6ImRlZmF1bHQtdG9rZW4tZmo5N2QiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC5uYW1lIjoiZGVmYXVsdCIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50LnVpZCI6ImI3ZmIyNGM4LWY3NDItNDg1NS1hMzQ2LWI2MWU2OTIyOWFkNyIsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmRlZmF1bHQifQ.KWSove4kYGyCgdAVUxH_tUTvk3ZGeEIX_ZnSIfuDXRCLtsTX_P6wrqigXWhOc5EDhVfdyVw6J5l_d5ierjAykif-bahvScs1ioJ2PlrYTetT8e5KrThsz-4ull8201McaDDCQ22jvu6AhtW2HJM3Zi0HUHRreTdc1Rzi8-DbmB6nGx1VzlrjdlbB73JNxYgIq8QvpbYZufJm5DRVg0CsQ8fzkiLoOi_1rhT0-z-C_xHhRqmf5-xx7C58ld2zZGSm7hdHm33rtP-idpCAfeeVcgl1Q8mxlYBpzPpB26aLJ1rACNJX0ZjM2pZ19EPyD4mFpAbCETkNpoFmvqb4cijPPA"
OS_USERNAME = "admin"
OS_PASSWORD = "1234"
OS_PROJECT = "demo"

USERNAME = "pishahang"
PASSWORD = "1234"

EXPERIMENT_REFERENCE = "MVS-TF_300-SF_600-Time_3600-runs_3-1"

IMAGES = ["transcoder_mv"]
# INSTANCES = list(range(10, 400, 10))
INSTANCES = [1]
RUNS = 3


EXPERIMENT_TIME = 3600
SWITCH_FREQUENCY = 600

DESCRIPTORS_PATH = "/app/Pishahang/descriptors/multiversion"

DOCKER_EXCLUDE = []
INIT_VERSION = "virtual_deployment_units_con"
#################

aConfiguration = client.Configuration()
aConfiguration.host = K8_URL

aConfiguration.verify_ssl = False
aConfiguration.api_key = {"authorization": "Bearer " + ATOKEN}

aApiClient = client.ApiClient(aConfiguration)


# #####################################################

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' + directory)


def delete_replication_controller():

    v1 = client.CoreV1Api(aApiClient)
    ret = v1.list_namespaced_replication_controller(namespace='default', watch=False)
    for i in ret.items:
    #   print("%s\t%s" %
    #         (i.metadata.name, i.metadata.creation_timestamp))

      api_instance = client.CoreV1Api(aApiClient)
      body = client.V1DeleteOptions()
      api_response = api_instance.delete_namespaced_replication_controller(i.metadata.name, i.metadata.namespace, body=body)

def delete_pod():

    v1 = client.CoreV1Api(aApiClient)
    ret = v1.list_namespaced_pod(namespace='default', watch=False)
    for i in ret.items:
    #   print("%s\t%s" %
    #         (i.metadata.name, i.metadata.creation_timestamp))

      api_instance = client.CoreV1Api(aApiClient)
      body = client.V1DeleteOptions()
      api_response = api_instance.delete_namespaced_pod(i.metadata.name, i.metadata.namespace, body=body)

def delete_services():

    v1 = client.CoreV1Api(aApiClient)
    ret = v1.list_namespaced_service(namespace='default', watch=False)
    for i in ret.items:
    #   print("%s\t%s" %
    #         (i.metadata.name, i.metadata.creation_timestamp))

      api_instance = client.CoreV1Api(aApiClient)
      body = client.V1DeleteOptions()
      api_response = api_instance.delete_namespaced_service(i.metadata.name, i.metadata.namespace, body=body)

def delete_stacks():
    auth = v3.Password(auth_url=AUTH_URL,
                    username=OS_USERNAME,
                    password=OS_PASSWORD,
                    project_name='demo',
                    user_domain_id='default',
                    project_domain_id='default')
    sess = session.Session(auth=auth)
    heat = hclient.Client('1', session=sess)

    try:
        for s in heat.stacks.list():
            s.delete()
    except Exception as e:
        print(e)

def restart_pishahang(host=HOST_URL, port=APP_SERVER_PORT) :
    _base_path = 'http://{0}:{1}/restart_pishahang'.format(host, port)

    try:
        r = requests.get(_base_path, verify=False)
        print(r.text)
    except Exception as e:
        print("Restart Pishahang")

def get_pishahang_docker_list(host=HOST_URL, port=APP_SERVER_PORT):
    _base_path = 'http://{0}:{1}/get_docker_names'.format(host, port)

    try:
        r = requests.get(_base_path, verify=False)
        print(r.text)
        return json.loads(r.text)
    except Exception as e:
        print("get_docker_names")

def set_remote_version(version, host=HOST_URL, port=8898) :
    if "virtual_deployment_units_vm" in version:
        switch_type="VM"
    if "virtual_deployment_units_gpu" in version:
        switch_type="GPU"
    if "virtual_deployment_units_con" in version:
        switch_type="CON"

    _base_path = 'http://{0}:{1}/switch_version?version={2}'.format(host, port, switch_type)

    try:
        r = requests.get(_base_path, verify=False)
        # print("Switch Version")
        print("Switch Version: ", r.text)
    except Exception as e:
        print(e)
        print("Switch version could'nt be set")
# #####################################################

pishahang = wrappers.SONATAClient.Auth(HOST_URL)
pishahang_nsd = wrappers.SONATAClient.Nsd(HOST_URL)
pishahang_nslcm = wrappers.SONATAClient.Nslcm(HOST_URL)
pishahang_vnfpkgm = wrappers.SONATAClient.VnfPkgm(HOST_URL)
pishahang_pish = wrappers.SONATAClient.Pishahang(HOST_URL)

# #####################################################

if CLEAR_DESCRIPTORS:
    _token = json.loads(pishahang.auth(
                            username=USERNAME, 
                            password=PASSWORD))

    _token = json.loads(_token["data"])

    # Delete NSDs
    nsd_list = json.loads(pishahang_nsd.get_ns_descriptors(
                        token=_token["token"]["access_token"]))
    nsd_list = json.loads(nsd_list["data"])

    print(nsd_list)

    for _nsd in nsd_list:
        print(_nsd["uuid"])    
        pishahang_nsd.delete_ns_descriptors_nsdinfoid(token=_token["token"]["access_token"], nsdinfoid=_nsd["uuid"]) 

    nsd_list = json.loads(pishahang_nsd.get_ns_descriptors(
                        token=_token["token"]["access_token"]))
    nsd_list = json.loads(nsd_list["data"])

    print(nsd_list)

    # Delete VNFDs

    vnf_list = json.loads(pishahang_vnfpkgm.get_vnf_packages(
                        token=_token["token"]["access_token"]))
    vnf_list = json.loads(vnf_list["data"])

    print(vnf_list)

    for _vnfd in vnf_list:
        print(_vnfd["uuid"])    
        pishahang_vnfpkgm.delete_vnf_packages_vnfpkgid(token=_token["token"]["access_token"], vnfPkgId=_vnfd["uuid"]) 

    vnf_list = json.loads(pishahang_vnfpkgm.get_vnf_packages(
                        token=_token["token"]["access_token"]))
    vnf_list = json.loads(vnf_list["data"])

    print(vnf_list)

    # print(pishahang_pish.delete_pd_descriptors_pdpkgid("*"))
    time.sleep(5)

# #####################################################

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

for _image in IMAGES:
    for _instances in INSTANCES:
        for _run in range(1, RUNS+1):
            try:
                print(pishahang_pish.delete_pd_descriptors_pdpkgid(_image))
                restart_pishahang()
                delete_replication_controller()
                delete_pod()
                delete_services()
                time.sleep(60)

                experiment_timestamps = {}
                experiment_timestamps["start_time"] = int(time.time())

                nit = "./EXP_RESULTS/{0}/run_{1}".format(EXPERIMENT_REFERENCE, _run)

                createFolder("{nit}/".format(nit=nit))

                # extracting the token
                token = json.loads(pishahang.auth(username=USERNAME, password=PASSWORD))
                token = json.loads(token["data"])

                # Upload VNF
                VNFD_PATH = "{desc}/{name}_vnfd.yml".format(desc=DESCRIPTORS_PATH, name=_image)
                _res = pishahang_vnfpkgm.post_vnf_packages(token=token["token"]["access_token"],
                                                            package_path=VNFD_PATH)
                print(_res)
                time.sleep(0.5)

                # Upload NSD
                NSD_PATH = "{desc}/{name}_nsd.yml".format(desc=DESCRIPTORS_PATH, name=_image)
                _res = pishahang_nsd.post_ns_descriptors(token=token["token"]["access_token"],
                                                            package_path=NSD_PATH)
                print(_res)
                time.sleep(0.5)

                # Upload PD
                PD_PATH = "{desc}/{name}_policy.yml".format(desc=DESCRIPTORS_PATH, name=_image)
                _res = pishahang_pish.post_pd_descriptors(package_path=PD_PATH)
                print(_res)
                time.sleep(0.5)

                # Get NSD UUID and init
                _nsd_list = json.loads(pishahang_nsd.get_ns_descriptors(token=token["token"]["access_token"], limit=1000))
                _nsd_list = json.loads(_nsd_list["data"])

                _ns = None
                for _n in _nsd_list:
                    if _image == _n['nsd']['name']:            
                        _ns = _n['uuid']
                        print("UUID")
                        print(_ns)
                        continue

                if _ns:
                    # calling the service instantiation API 
                    instantiation = json.loads(pishahang_nslcm.post_ns_instances_nsinstanceid_instantiate(
                                            token=token["token"]["access_token"], nsInstanceId=_ns))
                    instantiation = json.loads(instantiation["data"])
                    print ("Service instantiation request has been sent!")


                    # extracting the request id
                    _rq_id = instantiation["id"]

                    # checking the service instantiation status
                    counter, timeout, sleep_interval = 0, 60, 2

                    while counter < timeout:

                        #calling the request API
                        request = json.loads(pishahang_nslcm.get_ns_instances_request_status(
                                            token=token["token"]["access_token"], nsInstanceId=_rq_id))
                        request = json.loads(request["data"])

                        # checking if the call was successful
                        try:
                            request_status = request["status"]
                        except:
                            print ("Error in request status chaeking!")
                            break

                        # checking if the instantiation was successful
                        if request["status"] == "ERROR":
                            print ("Error in service instantiation")
                            break
                        elif request["status"] == "READY":
                            print (request["status"] + " : Service has been successfully instantiated!")
                            break

                        # printing the current status and sleep
                        print (request["status"] + "...")
                        time.sleep(sleep_interval)
                        counter += sleep_interval

                    if counter > timeout:
                        print ("Error: service instantiation remained incomplete")
                else:
                    print("Could not upload and instantiate NS")


                # switch here
                _EXP_COUNTER = 0
                _curr_version = INIT_VERSION
                while(_EXP_COUNTER < EXPERIMENT_TIME):
                    time.sleep(SWITCH_FREQUENCY)

                    if "con" in _curr_version:
                        _curr_version = "virtual_deployment_units_gpu"
                    else:
                        _curr_version = "virtual_deployment_units_con"

                    print("Switching to: ", _curr_version, "at: ", _EXP_COUNTER)
                    set_remote_version(_curr_version)

                    _EXP_COUNTER += SWITCH_FREQUENCY


                experiment_timestamps["end_time"] = int(time.time())                                 


                print("Saving Metrics  ...")

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


                print("Metrics saved in folder {nit}".format(nit=nit))

                print("\n\n\n\n\n\n ENDED \n\n\n\n\n\n")

            except Exception as e:
                print("Main Exception")
                print(e)




