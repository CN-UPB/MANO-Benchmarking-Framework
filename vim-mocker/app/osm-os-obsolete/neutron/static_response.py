networks = {
  "networks": [
    {
      "provider:physical_network": None,
      "ipv6_address_scope": None,
      "revision_number": 5,
      "port_security_enabled": True,
      "mtu": 1450,
      "id": "244b9ff4-5085-4db6-8e6e-e43565576988",
      "router:external": False,
      "availability_zone_hints": [
        
      ],
      "availability_zones": [
        "nova"
      ],
      "ipv4_address_scope": None,
      "shared": False,
      "project_id": "40d9de036960447dafd7d74d306cf189",
      "status": "ACTIVE",
      "subnets": [
        "5e8f553c-daee-4954-9e3f-e9aca59ddd49"
      ],
      "description": "",
      "tags": [
        
      ],
      "updated_at": "2020-02-25T10:03:47Z",
      "provider:segmentation_id": 54,
      "name": "large-priv",
      "admin_state_up": True,
      "tenant_id": "40d9de036960447dafd7d74d306cf189",
      "created_at": "2020-02-25T10:03:46Z",
      "provider:network_type": "vxlan"
    }
  ]
}

def ports(port_details):
  _ports = {
    "port": {
      "status": "DOWN",
      "binding:host_id": "",
      "description": "",
      "allowed_address_pairs": [
        
      ],
      "tags": [
        
      ],
      "extra_dhcp_opts": [
        
      ],
      "updated_at": "2020-03-08T15:27:17Z",
      "device_owner": "",
      "revision_number": 5,
      "binding:profile": {
        
      },
      "port_security_enabled": True,
      "fixed_ips": [
        {
          "subnet_id": "5e8f553c-daee-4954-9e3f-e9aca59ddd49",
          "ip_address": "10.0.100.16"
        }
      ],
      "id": "e9901e10-36d8-4c84-9db1-b852cdc63808",
      "security_groups": [
        "a2167217-dae9-4469-afe0-29d2c87a1110"
      ],
      "device_id": "",
      "name": "vdu-eth0",
      "admin_state_up": True,
      "network_id": port_details["port"]["network_id"],
      "tenant_id": "40d9de036960447dafd7d74d306cf189",
      "binding:vif_details": {
        
      },
      "binding:vnic_type": "normal",
      "binding:vif_type": "unbound",
      "mac_address": "fa:16:3e:db:cc:6a",
      "project_id": "40d9de036960447dafd7d74d306cf189",
      "created_at": "2020-03-08T15:27:17Z"
    }
  }

  return _ports


def networks_status(_id):
  _networks_status = {
    "networks": [
      {
        "provider:physical_network": None,
        "ipv6_address_scope": None,
        "revision_number": 5,
        "port_security_enabled": True,
        "mtu": 1450,
        "id": _id,
        "router:external": False,
        "availability_zone_hints": [
          
        ],
        "availability_zones": [
          "nova"
        ],
        "ipv4_address_scope": None,
        "shared": False,
        "project_id": "40d9de036960447dafd7d74d306cf189",
        "status": "ACTIVE",
        "subnets": [
          "5e8f553c-daee-4954-9e3f-e9aca59ddd49"
        ],
        "description": "",
        "tags": [
          
        ],
        "updated_at": "2020-02-25T10:03:47Z",
        "provider:segmentation_id": 54,
        "name": "large-priv",
        "admin_state_up": True,
        "tenant_id": "40d9de036960447dafd7d74d306cf189",
        "created_at": "2020-02-25T10:03:46Z",
        "provider:network_type": "vxlan"
      }
    ]
  }

  return _networks_status

def subnets(subnet_id):
  _subnets = {
    "subnet": {
      "service_types": [
        
      ],
      "description": "",
      "enable_dhcp": True,
      "tags": [
        
      ],
      "network_id": "244b9ff4-5085-4db6-8e6e-e43565576988",
      "tenant_id": "40d9de036960447dafd7d74d306cf189",
      "created_at": "2020-02-25T10:03:47Z",
      "dns_nameservers": [
        "8.8.8.8"
      ],
      "updated_at": "2020-02-25T10:03:47Z",
      "gateway_ip": "10.0.100.1",
      "ipv6_ra_mode": None,
      "allocation_pools": [
        {
          "start": "10.0.100.2",
          "end": "10.0.100.254"
        }
      ],
      "host_routes": [
        
      ],
      "revision_number": 2,
      "ip_version": 4,
      "ipv6_address_mode": None,
      "cidr": "10.0.100.0/24",
      "project_id": "40d9de036960447dafd7d74d306cf189",
      "id": subnet_id,
      "subnetpool_id": None,
      "name": "large-sub"
    }
  }
  
  return _subnets