def servers_details(server_list):
  _servers_details = {"servers": [] }
  for _s in server_list:
    _server = {
          "OS-EXT-STS:task_state": "spawning",
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
              "href": "http://vim-mocker:8774/v2.1/servers/{server_id}".format(server_id=_s),
              "rel": "self"
            },
            {
              "href": "http://vim-mocker:8774/servers/{server_id}".format(server_id=_s),
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
          "OS-EXT-STS:vm_state": "building",
          "OS-EXT-SRV-ATTR:instance_name": "instance-000001f1",
          "OS-SRV-USG:launched_at": None,
          "flavor": {
            "id": "40bab6b4-2891-4848-805c-1afa5763c072",
            "links": [
              {
                "href": "http://vim-mocker:8774/flavors/40bab6b4-2891-4848-805c-1afa5763c072",
                "rel": "bookmark"
              }
            ]
          },
          "id": _s,
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
          "OS-EXT-STS:power_state": 0,
          "OS-EXT-AZ:availability_zone": "nova",
          "metadata": {
            
          },
          "status": "BUILD",
          "updated": "2020-03-08T15:27:22Z",
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
    _servers_details["servers"].append(_server)    

  return _servers_details

flavors_detail = {
  "flavors": [
    {
      "links": [
        {
          "href": "http://vim-mocker:8774/v2.1/flavors/2",
          "rel": "self"
        },
        {
          "href": "http://vim-mocker:8774/flavors/2",
          "rel": "bookmark"
        }
      ],
      "ram": 2048,
      "OS-FLV-DISABLED:disabled": False,
      "os-flavor-access:is_public": True,
      "rxtx_factor": 1.0,
      "disk": 20,
      "id": "2",
      "name": "m1.small",
      "vcpus": 1,
      "swap": "",
      "OS-FLV-EXT-DATA:ephemeral": 0
    },
    {
      "links": [
        {
          "href": "http://vim-mocker:8774/v2.1/flavors/3",
          "rel": "self"
        },
        {
          "href": "http://vim-mocker:8774/flavors/3",
          "rel": "bookmark"
        }
      ],
      "ram": 4096,
      "OS-FLV-DISABLED:disabled": False,
      "os-flavor-access:is_public": True,
      "rxtx_factor": 1.0,
      "disk": 40,
      "id": "3",
      "name": "m1.medium",
      "vcpus": 2,
      "swap": "",
      "OS-FLV-EXT-DATA:ephemeral": 0
    },
    {
      "links": [
        {
          "href": "http://vim-mocker:8774/v2.1/flavors/4",
          "rel": "self"
        },
        {
          "href": "http://vim-mocker:8774/flavors/4",
          "rel": "bookmark"
        }
      ],
      "ram": 8192,
      "OS-FLV-DISABLED:disabled": False,
      "os-flavor-access:is_public": True,
      "rxtx_factor": 1.0,
      "disk": 80,
      "id": "4",
      "name": "m1.large",
      "vcpus": 4,
      "swap": "",
      "OS-FLV-EXT-DATA:ephemeral": 0
    },
    {
      "links": [
        {
          "href": "http://vim-mocker:8774/v2.1/flavors/42",
          "rel": "self"
        },
        {
          "href": "http://vim-mocker:8774/flavors/42",
          "rel": "bookmark"
        }
      ],
      "ram": 64,
      "OS-FLV-DISABLED:disabled": False,
      "os-flavor-access:is_public": True,
      "rxtx_factor": 1.0,
      "disk": 0,
      "id": "42",
      "name": "m1.nano",
      "vcpus": 1,
      "swap": "",
      "OS-FLV-EXT-DATA:ephemeral": 0
    },
    {
      "links": [
        {
          "href": "http://vim-mocker:8774/v2.1/flavors/451",
          "rel": "self"
        },
        {
          "href": "http://vim-mocker:8774/flavors/451",
          "rel": "bookmark"
        }
      ],
      "ram": 512,
      "OS-FLV-DISABLED:disabled": False,
      "os-flavor-access:is_public": True,
      "rxtx_factor": 1.0,
      "disk": 0,
      "id": "451",
      "name": "m1.heat",
      "vcpus": 1,
      "swap": "",
      "OS-FLV-EXT-DATA:ephemeral": 0
    },
    {
      "links": [
        {
          "href": "http://vim-mocker:8774/v2.1/flavors/5",
          "rel": "self"
        },
        {
          "href": "http://vim-mocker:8774/flavors/5",
          "rel": "bookmark"
        }
      ],
      "ram": 16384,
      "OS-FLV-DISABLED:disabled": False,
      "os-flavor-access:is_public": True,
      "rxtx_factor": 1.0,
      "disk": 160,
      "id": "5",
      "name": "m1.xlarge",
      "vcpus": 8,
      "swap": "",
      "OS-FLV-EXT-DATA:ephemeral": 0
    },
    {
      "links": [
        {
          "href": "http://vim-mocker:8774/v2.1/flavors/84",
          "rel": "self"
        },
        {
          "href": "http://vim-mocker:8774/flavors/84",
          "rel": "bookmark"
        }
      ],
      "ram": 128,
      "OS-FLV-DISABLED:disabled": False,
      "os-flavor-access:is_public": True,
      "rxtx_factor": 1.0,
      "disk": 0,
      "id": "84",
      "name": "m1.micro",
      "vcpus": 1,
      "swap": "",
      "OS-FLV-EXT-DATA:ephemeral": 0
    },
    {
      "links": [
        {
          "href": "http://vim-mocker:8774/v2.1/flavors/c1",
          "rel": "self"
        },
        {
          "href": "http://vim-mocker:8774/flavors/c1",
          "rel": "bookmark"
        }
      ],
      "ram": 256,
      "OS-FLV-DISABLED:disabled": False,
      "os-flavor-access:is_public": True,
      "rxtx_factor": 1.0,
      "disk": 0,
      "id": "c1",
      "name": "cirros256",
      "vcpus": 1,
      "swap": "",
      "OS-FLV-EXT-DATA:ephemeral": 0
    },
    {
      "links": [
        {
          "href": "http://vim-mocker:8774/v2.1/flavors/d1",
          "rel": "self"
        },
        {
          "href": "http://vim-mocker:8774/flavors/d1",
          "rel": "bookmark"
        }
      ],
      "ram": 512,
      "OS-FLV-DISABLED:disabled": False,
      "os-flavor-access:is_public": True,
      "rxtx_factor": 1.0,
      "disk": 5,
      "id": "d1",
      "name": "ds512M",
      "vcpus": 1,
      "swap": "",
      "OS-FLV-EXT-DATA:ephemeral": 0
    },
    {
      "links": [
        {
          "href": "http://vim-mocker:8774/v2.1/flavors/d2",
          "rel": "self"
        },
        {
          "href": "http://vim-mocker:8774/flavors/d2",
          "rel": "bookmark"
        }
      ],
      "ram": 1024,
      "OS-FLV-DISABLED:disabled": False,
      "os-flavor-access:is_public": True,
      "rxtx_factor": 1.0,
      "disk": 10,
      "id": "d2",
      "name": "ds1G",
      "vcpus": 1,
      "swap": "",
      "OS-FLV-EXT-DATA:ephemeral": 0
    },
    {
      "links": [
        {
          "href": "http://vim-mocker:8774/v2.1/flavors/d3",
          "rel": "self"
        },
        {
          "href": "http://vim-mocker:8774/flavors/d3",
          "rel": "bookmark"
        }
      ],
      "ram": 2048,
      "OS-FLV-DISABLED:disabled": False,
      "os-flavor-access:is_public": True,
      "rxtx_factor": 1.0,
      "disk": 10,
      "id": "d3",
      "name": "ds2G",
      "vcpus": 2,
      "swap": "",
      "OS-FLV-EXT-DATA:ephemeral": 0
    },
    {
      "links": [
        {
          "href": "http://vim-mocker:8774/v2.1/flavors/d4",
          "rel": "self"
        },
        {
          "href": "http://vim-mocker:8774/flavors/d4",
          "rel": "bookmark"
        }
      ],
      "ram": 4096,
      "OS-FLV-DISABLED:disabled": False,
      "os-flavor-access:is_public": True,
      "rxtx_factor": 1.0,
      "disk": 20,
      "id": "d4",
      "name": "ds4G",
      "vcpus": 4,
      "swap": "",
      "OS-FLV-EXT-DATA:ephemeral": 0
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
      "security_groups": [
        {
          "name": "default"
        }
      ],
      "OS-DCF:diskConfig": "MANUAL",
      "id": server_uuid,
      "links": [
        {
          "href": "http://vim-mocker:8774/v2.1/servers/{server_uuid}".format(server_uuid=server_uuid),
          "rel": "self"
        },
        {
          "href": "http://vim-mocker:8774/servers/{server_uuid}".format(server_uuid=server_uuid),
          "rel": "bookmark"
        }
      ],
      "adminPass": "DoCS8ETLokyt"
    }
  }

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