import wrappers
import json
import time
from dateutil import parser

USERNAME = "pishahang"
PASSWORD = "1234"

DEL_NSD = False
DEL_VNFD = False
DEL_INSTANCES = False

HOST_URL = "thesismano4.cs.upb.de"

sonata_nsd = wrappers.SONATAClient.Nsd(HOST_URL)
sonata_auth = wrappers.SONATAClient.Auth(HOST_URL)
sonata_vnfpkgm = wrappers.SONATAClient.VnfPkgm(HOST_URL)
sonata_nslcm = wrappers.SONATAClient.Nslcm(HOST_URL) 

_token = json.loads(sonata_auth.auth(
                        username=USERNAME, 
                        password=PASSWORD))

_token = json.loads(_token["data"])

if DEL_NSD:
    # Delete NSDs
    nsd_list = json.loads(sonata_nsd.get_ns_descriptors(
                        token=_token["token"]["access_token"]))
    nsd_list = json.loads(nsd_list["data"])

    print(nsd_list)

    for _nsd in nsd_list:
        print(_nsd["uuid"])    
        sonata_nsd.delete_ns_descriptors_nsdinfoid(token=_token["token"]["access_token"], nsdinfoid=_nsd["uuid"]) 

    nsd_list = json.loads(sonata_nsd.get_ns_descriptors(
                        token=_token["token"]["access_token"]))
    nsd_list = json.loads(nsd_list["data"])

    print(nsd_list)

if DEL_VNFD:
    # Delete VNFDs
    vnf_list = json.loads(sonata_vnfpkgm.get_vnf_packages(
                        token=_token["token"]["access_token"]))
    vnf_list = json.loads(vnf_list["data"])

    print(vnf_list)

    for _vnfd in vnf_list:
        print(_vnfd["uuid"])    
        sonata_vnfpkgm.delete_vnf_packages_vnfpkgid(token=_token["token"]["access_token"], vnfPkgId=_vnfd["uuid"]) 

    vnf_list = json.loads(sonata_vnfpkgm.get_vnf_packages(
                        token=_token["token"]["access_token"]))
    vnf_list = json.loads(vnf_list["data"])

    print(vnf_list)


TEST = True
if TEST:
    while True:

        _ns_list = json.loads(sonata_nslcm.get_ns_instances(
                                token=_token["token"]["access_token"], limit=1000))
        _ns_list = json.loads(_ns_list["data"])

        _requests = json.loads(sonata_nslcm.get_ns_instances_request_status(
                                    token=_token["token"]["access_token"], limit=1000))
        _requests = json.loads(_requests["data"])

        _ns = None
        for _r in _requests:
            try:
                server_created = parser.parse(_r['began_at'])
                if int(server_created.strftime("%s")) >= int(1):
                    print(_r['status'])
                    # ERROR
                    # INSTANTIATING
                    # READY
                    
                # _ns = _n['_id']
                # if _ns:
                #     response = json.loads(osm_nslcm.post_ns_instances_nsinstanceid_terminate(
                #                             token=_token["id"], 
                #                             nsInstanceId=_ns))
                #     print(response)
                time.sleep(1)
            except Exception as e:
                print(e)
                pass

        print("\n")