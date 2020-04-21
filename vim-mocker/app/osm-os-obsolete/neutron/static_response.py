networks = {
  "networks": [
    {
      "shared": False,
      "name": "default",
      "subnets": [
        "b784c464-9425-4f0d-a2b7-f76d79ec6b89"
      ],
      "status": "ACTIVE",
      "tenant_id": "abcdefghijklmnopqrstuvwxyz123456",
      "id": "d2b30ddd-b397-4aef-ac50-3bf9ad83d3c7",
      "admin_state_up": True
    }
  ]
}

network = {
  "network": {
    "admin_state_up": True,
    "subnets": [
      "611b346b-54e8-461f-88fe-7d1aa14cec56"
    ],
    "tenant_id": "abcdefghijklmnopqrstuvwxyz123456",
    "id": "a6367ddd-9a3f-4fef-8ae7-22ee6c7e763d",
    "shared": False,
    "status": "ACTIVE",
    "name": "default"
  }
}

def ports_details(server_list):
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

floatingips = {
  "floatingips": [
    {
      "floating_ip_address": "10.10.193.37"
    }
  ]
}

def port(port_details):
  _port = {
    "port":
      {
        "admin_state_up": True,
        "device_id": "257614cc-e178-4c92-9c61-3b28d40eca44",
        "device_owner": "",
        "fixed_ips": [
          {
            "ip_address": "192.168.100.4",
            "subnet_id": "b784c464-9425-4f0d-a2b7-f76d79ec6b89"
          }
        ],
        "id": "0a20b7e1-fa3e-409f-9cea-f7f7c84aaf8c",
        "mac_address": None,
        "name": port_details["port"]["name"],
        "network_id": port_details["port"]["network_id"],
        "status": "ACTIVE",
        "tenant_id": "abcdefghijklmnopqrstuvwxyz123456"
      }
  }

  return _port

def ports():
  _ports = {
    "ports": [
      {
        "admin_state_up": True,
        "device_id": "257614cc-e178-4c92-9c61-3b28d40eca44",
        "device_owner": "",
        "fixed_ips": [
          {
            "ip_address": "192.168.100.4",
            "subnet_id": "b784c464-9425-4f0d-a2b7-f76d79ec6b89"
          }
        ],
        "id": "0a20b7e1-fa3e-409f-9cea-f7f7c84aaf8c",
        "mac_address": None,
        "name":"vdu-eth0",
        "network_id": "d2b30ddd-b397-4aef-ac50-3bf9ad83d3c7",
        "status": "ACTIVE",
        "tenant_id": "abcdefghijklmnopqrstuvwxyz123456"
      }
    ]
  }


  return _ports


def networks_status(_id):
  _networks_status = {
    "networks": [
      {
        "status": "ACTIVE",
        "subnets": [
          "b784c464-9425-4f0d-a2b7-f76d79ec6b89"
        ],
        "name": "default",
        "admin_state_up": True,
        "tenant_id": "abcdefghijklmnopqrstuvwxyz123456",
        "id": _id,
        "shared": False
      }
    ]
  }

  return _networks_status

def subnets(subnet_id):
  _subnets =  {
    "subnet": {
      "name": "default-sub",
      "network_id": "d2b30ddd-b397-4aef-ac50-3bf9ad83d3c7",
      "tenant_id": "abcdefghijklmnopqrstuvwxyz123456",
      "created_at": "2020-03-08T15:27:19Z",
      "dns_nameservers": [
        
      ],
      "allocation_pools": [
        {
          "start": "192.168.100.0",
          "end": "192.168.100.255"
        }
      ],
      "host_routers": [
        
      ],
      "gateway_ip": None,
      "ip_version": "4",
      "cidr": "192.168.100.0/24",
      "updated_at": None,
      "id": subnet_id,
      "enable_dhcp": False
    }
  }

  return _subnets