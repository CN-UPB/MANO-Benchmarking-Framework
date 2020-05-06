def servers_details(server_list):
  _servers_details = {"servers": [] }
  for _s in server_list:
    _server =  {
      "name": "dc1_as-1-stress-VM-1",
      "full_name": "dc1_as-1-stress-VM-1",
      "id": _s,
      "template_name": "as-1-stress-VM-1",
      "flavor": {
        "id": "72936ae1-56e0-44f0-a689-58080967dc6c",
        "links": [
          {
            "href": "http://thesismano2.cs.upb.de:9775/v2.1/fc394f2ab2df4114bde39905f800dc57/flavors/72936ae1-56e0-44f0-a689-58080967dc6c",
            "rel": "bookmark"
          }
        ]
      },
      "image": {
        "id": "95bd65e3-3048-428f-8a9c-4705a67a55e9",
        "links": [
          {
            "href": "http://thesismano2.cs.upb.de:9775/v2.1/fc394f2ab2df4114bde39905f800dc57/images/95bd65e3-3048-428f-8a9c-4705a67a55e9",
            "rel": "bookmark"
          }
        ]
      },
      "command": None,
      "status": "ACTIVE",
      "OS-EXT-STS:power_state": 1,
      "OS-EXT-STS:task_state": None,
      "links": [
        {
          "href": "http://thesismano2.cs.upb.de:9775/v2.1/fc394f2ab2df4114bde39905f800dc57/servers/{server_id}".format(server_id=_s)
        }
      ]
    }
    
    _servers_details["servers"].append(_server)    

  return _servers_details

flavors_detail = {
  "flavors": [
    {
      "id": "e2d11672-3a02-489a-a61e-7a9734ec9b4f",
      "name": "m1.tiny",
      "cpu": 1,
      "memory": 512,
      "memory_unit": "MB",
      "storage": 1,
      "storage_unit": "GB",
      "links": [
        {
          "href": "http://thesismano2.cs.upb.de:9775/v2.1/fc394f2ab2df4114bde39905f800dc57/flavors/e2d11672-3a02-489a-a61e-7a9734ec9b4f"
        }
      ],
      "OS-FLV-DISABLED:disabled": False,
      "OS-FLV-EXT-DATA:ephemeral": 0,
      "os-flavor-access:is_public": True,
      "ram": 512,
      "vcpus": 1,
      "swap": 0,
      "disk": 1,
      "rxtx_factor": 1.0
    },
    {
      "id": "f7dc15f9-9ff7-4867-9c82-7d51769681c9",
      "name": "m1.nano",
      "cpu": 1,
      "memory": 64,
      "memory_unit": "MB",
      "storage": 0,
      "storage_unit": "GB",
      "links": [
        {
          "href": "http://thesismano2.cs.upb.de:9775/v2.1/fc394f2ab2df4114bde39905f800dc57/flavors/f7dc15f9-9ff7-4867-9c82-7d51769681c9"
        }
      ],
      "OS-FLV-DISABLED:disabled": False,
      "OS-FLV-EXT-DATA:ephemeral": 0,
      "os-flavor-access:is_public": True,
      "ram": 64,
      "vcpus": 1,
      "swap": 0,
      "disk": 0,
      "rxtx_factor": 1.0
    },
    {
      "id": "cc637a5d-f1ba-45b0-a7eb-2951bd794d5b",
      "name": "m1.micro",
      "cpu": 1,
      "memory": 128,
      "memory_unit": "MB",
      "storage": 0,
      "storage_unit": "GB",
      "links": [
        {
          "href": "http://thesismano2.cs.upb.de:9775/v2.1/fc394f2ab2df4114bde39905f800dc57/flavors/cc637a5d-f1ba-45b0-a7eb-2951bd794d5b"
        }
      ],
      "OS-FLV-DISABLED:disabled": False,
      "OS-FLV-EXT-DATA:ephemeral": 0,
      "os-flavor-access:is_public": True,
      "ram": 128,
      "vcpus": 1,
      "swap": 0,
      "disk": 0,
      "rxtx_factor": 1.0
    },
    {
      "id": "5459ddaa-4095-49a4-8d85-af013afbb6d6",
      "name": "m1.small",
      "cpu": 1,
      "memory": 1024,
      "memory_unit": "MB",
      "storage": 2,
      "storage_unit": "GB",
      "links": [
        {
          "href": "http://thesismano2.cs.upb.de:9775/v2.1/fc394f2ab2df4114bde39905f800dc57/flavors/5459ddaa-4095-49a4-8d85-af013afbb6d6"
        }
      ],
      "OS-FLV-DISABLED:disabled": False,
      "OS-FLV-EXT-DATA:ephemeral": 0,
      "os-flavor-access:is_public": True,
      "ram": 1024,
      "vcpus": 1,
      "swap": 0,
      "disk": 2,
      "rxtx_factor": 1.0
    },
    {
      "id": "72936ae1-56e0-44f0-a689-58080967dc6c",
      "name": "stress-VM-flv",
      "cpu": 1,
      "memory": 512,
      "memory_unit": "MB",
      "storage": 1,
      "storage_unit": "GB",
      "links": [
        {
          "href": "http://thesismano2.cs.upb.de:9775/v2.1/fc394f2ab2df4114bde39905f800dc57/flavors/72936ae1-56e0-44f0-a689-58080967dc6c"
        }
      ],
      "OS-FLV-DISABLED:disabled": False,
      "OS-FLV-EXT-DATA:ephemeral": 0,
      "os-flavor-access:is_public": True,
      "ram": 512,
      "vcpus": 1,
      "swap": 0,
      "disk": 1,
      "rxtx_factor": 1.0
    }
  ]
}

flavor_extra = { "extra_specs": {} }

def flavor_create(flavor_details):
  flavor_create = {
    "flavor": {
      "links": [
        {
          "href": "http://vim-mocker:8774/v2.1/flavors/40bab6b4-2891-4848-805c-1afa5763c072",
          "rel": "self"
        },
        {
          "href": "http://vim-mocker:8774/flavors/40bab6b4-2891-4848-805c-1afa5763c072",
          "rel": "bookmark"
        }
      ],
      "ram": 512,
      "OS-FLV-DISABLED:disabled": False,
      "os-flavor-access:is_public": True,
      "rxtx_factor": 1.0,
      "disk": 1,
      "id": "40bab6b4-2891-4848-805c-1afa5763c072",
      "name": flavor_details["flavor"]["name"],
      "vcpus": 1,
      "swap": "",
      "OS-FLV-EXT-DATA:ephemeral": 0
    }
  }

  return flavor_create

def servers(server_uuid):
  _servers = {
    "server": {
      "name": "dc1_as-1-stress-VM-1",
      "full_name": "dc1_as-1-stress-VM-1",
      "id": server_uuid,
      "template_name": "as-1-stress-VM-1",
      "flavor": {
        "id": "72936ae1-56e0-44f0-a689-58080967dc6c",
        "links": [
          {
            "href": "http://thesismano2.cs.upb.de:9775/v2.1/fc394f2ab2df4114bde39905f800dc57/flavors/72936ae1-56e0-44f0-a689-58080967dc6c",
            "rel": "bookmark"
          }
        ]
      },
      "image": {
        "id": "95bd65e3-3048-428f-8a9c-4705a67a55e9",
        "links": [
          {
            "href": "http://thesismano2.cs.upb.de:9775/v2.1/fc394f2ab2df4114bde39905f800dc57/images/95bd65e3-3048-428f-8a9c-4705a67a55e9",
            "rel": "bookmark"
          }
        ]
      },
      "command": None,
      "links": [
        {
          "href": "http://thesismano2.cs.upb.de:9775/v2.1/fc394f2ab2df4114bde39905f800dc57/servers/{server_uuid}".format(server_uuid=server_uuid)
        }
      ]
    }
  }

  return _servers

def server_id(server_id):
  _server_id = {
    "server": {
      "OS-EXT-STS:task_state": None,
      "addresses": {
        "large-priv": [
          {
            "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:db:cc:6a",
            "version": 4,
            "addr": "10.0.100.16",
            "OS-EXT-IPS:type": "fixed"
          }
        ]
      },
      "links": [
        {
          "href": "http://vim-mocker:8774/v2.1/servers/{server_id}".format(server_id),
          "rel": "self"
        },
        {
          "href": "http://vim-mocker:8774/servers/{server_id}".format(server_id),
          "rel": "bookmark"
        }
      ],
      "image": {
        "id": "a96ad4ff-ae59-4a5c-876a-41e72e2220e9",
        "links": [
          {
            "href": "http://vim-mocker:8774/images/a96ad4ff-ae59-4a5c-876a-41e72e2220e9",
            "rel": "bookmark"
          }
        ]
      },
      "OS-EXT-STS:vm_state": "active",
      "OS-EXT-SRV-ATTR:instance_name": "instance-000001f1",
      "OS-SRV-USG:launched_at": "2020-03-08T15:27:26.000000",
      "flavor": {
        "id": "40bab6b4-2891-4848-805c-1afa5763c072",
        "links": [
          {
            "href": "http://vim-mocker:8774/flavors/40bab6b4-2891-4848-805c-1afa5763c072",
            "rel": "bookmark"
          }
        ]
      },
      "id": server_id,
      "security_groups": [
        {
          "name": "default"
        }
      ],
      "user_id": "b6231e05afc1441db1c91085c4251ef0",
      "OS-DCF:diskConfig": "MANUAL",
      "accessIPv4": "",
      "accessIPv6": "",
      "progress": 0,
      "OS-EXT-STS:power_state": 1,
      "OS-EXT-AZ:availability_zone": "nova",
      "metadata": {
        
      },
      "status": "ACTIVE",
      "updated": "2020-03-08T15:27:26Z",
      "hostId": "9e1e3f6536d0ae24c3c8888335750a82204ee4c63a0c5b22cafa54df",
      "OS-EXT-SRV-ATTR:host": "pishahang-os",
      "OS-SRV-USG:terminated_at": None,
      "key_name": None,
      "OS-EXT-SRV-ATTR:hypervisor_hostname": "pishahang-os",
      "name": "ns-1-stress-VM-1",
      "created": "2020-03-08T15:27:19Z",
      "tenant_id": "40d9de036960447dafd7d74d306cf189",
      "os-extended-volumes:volumes_attached": [
        
      ],
      "config_drive": ""
    }
  }