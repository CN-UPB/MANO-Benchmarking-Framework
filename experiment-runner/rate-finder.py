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
from concurrent.futures import ThreadPoolExecutor

# the following 4 variables need to be populated with the right values
USERNAME = "pishahang"
PASSWORD = "1234"
HOST_URL = "thesismano4.cs.upb.de"

VNFDNAME = "cirros1"
NSDNAME = "cirros1" #  Keep this same as this key _n['nsd']['name']
DESCRIPTORS_PATH = "/app/SONATA/Descriptors/descriptors"

TERMINATE_NS = False
no_instantiate = 100
_rpm = 100

pishahang = wrappers.SONATAClient.Auth(HOST_URL)
pishahang_nsd = wrappers.SONATAClient.Nsd(HOST_URL)
pishahang_nslcm = wrappers.SONATAClient.Nslcm(HOST_URL)
pishahang_vnfpkgm = wrappers.SONATAClient.VnfPkgm(HOST_URL)

# extracting the token
token = json.loads(pishahang.auth(username=USERNAME, password=PASSWORD))
token = json.loads(token["data"])

# Upload VNF
VNFD_PATH = "{desc}/{name}_vnfd.yml".format(desc=DESCRIPTORS_PATH, name=VNFDNAME)
_res = pishahang_vnfpkgm.post_vnf_packages(token=token["token"]["access_token"],
                                            package_path=VNFD_PATH)
print(_res)
time.sleep(0.5)

# Upload NSD
NSD_PATH = "{desc}/{name}_nsd.yml".format(desc=DESCRIPTORS_PATH, name=NSDNAME)
_res = pishahang_nsd.post_ns_descriptors(token=token["token"]["access_token"],
                                            package_path=NSD_PATH)
print(_res)
time.sleep(0.5)

# Get NSD UUID and init
_nsd_list = json.loads(pishahang_nsd.get_ns_descriptors(token=token["token"]["access_token"], limit=1000))
_nsd_list = json.loads(_nsd_list["data"])

_ns = None
for _n in _nsd_list:
    if NSDNAME == _n['nsd']['name']:            
        _ns = _n['uuid']
        print("UUID")
        print(_ns)
        continue


def run_async(func):
	from threading import Thread
	from functools import wraps

	@wraps(func)
	def async_func(*args, **kwargs):
		func_hl = Thread(target = func, args = args, kwargs = kwargs)
		func_hl.start()
		return func_hl

	return async_func

#####################################################

# def init_task(token, ns, i):
#     print("{} - Took {}".format(i, time.time() - _start))
#     # _start = time.time()
#     response = json.loads(
#                 pishahang_nslcm.post_ns_instances_nsinstanceid_instantiate(
#                     token=token, nsInstanceId=ns))
#     print(response)

#     if response["error"]:
#         print(response)
#         print("ERROR - init request uuid")

# _start = time.time()
# with ThreadPoolExecutor(max_workers=50) as executor:
#     for i in range(0, no_instantiate):
#         if _ns:
#             future = executor.submit(init_task, token["token"]["access_token"], _ns, i)
#         else:
#             print("ERROR - no ns uuid")
#         time.sleep(60/_rpm)

# 342
#####################################################

@run_async
def init_task(token, ns, i):
    print("{} - Took {}".format(i, time.time() - _start))
    # _start = time.time()
    response = json.loads(
                pishahang_nslcm.post_ns_instances_nsinstanceid_instantiate(
                    token=token, nsInstanceId=ns))
    print(response)

    if response["error"]:
        print(response)
        print("ERROR - init request uuid")

_start = time.time()
for i in range(0, no_instantiate):
    if _ns:
        init_task(token["token"]["access_token"], _ns, i)
    else:
        print("ERROR - no ns uuid")
    time.sleep(60/_rpm)



print(time.time() - _start)
print ("Service instantiation request has been sent!")


