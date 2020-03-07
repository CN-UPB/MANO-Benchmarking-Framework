# Replace
# stack_created["id"]
# stack_created["links"]["href"]
stack_created = {
  "stack": {
    "id": "{stack_id}",
    "links": [
      {
        "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/{stack_name}/{stack_id}",
        "rel": "self"
      }
    ]
  }
}

found = "The resource was found at http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/{stack_name}/{stack_id}; you should be redirected automatically.  "

def create_started_0(stack_id, stack_name):
  create_started_0 = {
    "stack": {
      "parent": None,
      "disable_rollback": True,
      "description": "No description",
      "parameters": {
        "OS::project_id": "40d9de036960447dafd7d74d306cf189",
        "OS::stack_id": stack_id,
        "OS::stack_name": stack_name
      },
      "deletion_time": None,
      "stack_name": stack_name,
      "stack_user_project_id": "19a10c8e62c04fb7987d87aeda2474b8",
      "stack_status_reason": "Stack CREATE started",
      "creation_time": "2020-03-02T14:05:54Z",
      "links": [
        {
          "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/{stack_name}/{stack_id}".format(stack_name=stack_name, stack_id=stack_id),
          "rel": "self"
        }
      ],
      "capabilities": [
        
      ],
      "notification_topics": [
        
      ],
      "tags": None,
      "timeout_mins": None,
      "stack_status": "CREATE_IN_PROGRESS",
      "stack_owner": None,
      "updated_time": None,
      "id": stack_id,
      "outputs": [
        
      ],
      "template_description": "No description"
    }
  }

  return create_started_0

def create_complete_1(stack_id, stack_name):
  create_complete_1 = {
    "stack": {
      "parent": None,
      "disable_rollback": True,
      "description": "No description",
      "parameters": {
        "OS::project_id": "40d9de036960447dafd7d74d306cf189",
        "OS::stack_id": stack_id,
        "OS::stack_name": stack_name
      },
      "deletion_time": None,
      "stack_name": stack_name,
      "stack_user_project_id": "19a10c8e62c04fb7987d87aeda2474b8",
      "stack_status_reason": "Stack CREATE completed successfully",
      "creation_time": "2020-03-02T14:05:54Z",
      "links": [
        {
          "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/{stack_name}/{stack_id}".format(stack_name=stack_name, stack_id=stack_id),
          "rel": "self"
        }
      ],
      "capabilities": [
        
      ],
      "notification_topics": [
        
      ],
      "tags": None,
      "timeout_mins": None,
      "stack_status": "CREATE_COMPLETE",
      "stack_owner": None,
      "updated_time": None,
      "id": stack_id,
      "outputs": [
        
      ],
      "template_description": "No description"
    }
  }

  return create_complete_1

def stack_update_started_2(stack_id, stack_name):
  stack_update_started_2 = {
    "stack": {
      "parent": None,
      "disable_rollback": True,
      "description": "No description",
      "parameters": {
        "OS::project_id": "40d9de036960447dafd7d74d306cf189",
        "OS::stack_id": stack_id,
        "OS::stack_name": stack_name
      },
      "deletion_time": None,
      "stack_name": stack_name,
      "stack_user_project_id": "19a10c8e62c04fb7987d87aeda2474b8",
      "stack_status_reason": "Stack UPDATE started",
      "creation_time": "2020-03-02T14:05:54Z",
      "links": [
        {
          "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/{stack_name}/{stack_id}".format(stack_name=stack_name, stack_id=stack_id),
          "rel": "self"
        }
      ],
      "capabilities": [
        
      ],
      "notification_topics": [
        
      ],
      "tags": None,
      "timeout_mins": None,
      "stack_status": "UPDATE_IN_PROGRESS",
      "stack_owner": None,
      "updated_time": "2020-03-02T14:06:11Z",
      "id": stack_id,
      "outputs": [
        
      ],
      "template_description": "No description"
    }
  }
  return stack_update_started_2

def stack_update_completed_3(stack_id, stack_name):
  stack_update_completed_3 = {
    "stack": {
      "parent": None,
      "disable_rollback": True,
      "description": "No description",
      "parameters": {
        "OS::project_id": "40d9de036960447dafd7d74d306cf189",
        "OS::stack_id": stack_id,
        "OS::stack_name": stack_name
      },
      "deletion_time": None,
      "stack_name": stack_name,
      "stack_user_project_id": "19a10c8e62c04fb7987d87aeda2474b8",
      "stack_status_reason": "Stack UPDATE completed successfully",
      "creation_time": "2020-03-02T14:05:54Z",
      "links": [
        {
          "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/{stack_name}/{stack_id}".format(stack_name=stack_name, stack_id=stack_id),
          "rel": "self"
        }
      ],
      "capabilities": [
        
      ],
      "notification_topics": [
        
      ],
      "tags": None,
      "timeout_mins": None,
      "stack_status": "UPDATE_COMPLETE",
      "stack_owner": None,
      "updated_time": "2020-03-02T14:06:11Z",
      "id": stack_id,
      "outputs": [
        
      ],
      "template_description": "No description"
    }
  }

  return stack_update_completed_3


template = {
  "heat_template_version": "2015-04-30",
  "resources": {
    "SonataService.input.internal.6b4c2ba0-02f2-4e77-8185-e770c4757f3b": {
      "type": "OS::Neutron::RouterInterface",
      "properties": {
        "subnet": {
          "get_resource": "SonataService.input.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b"
        },
        "router": "95a8c9dc-de39-4823-a19a-ff86a54f7bb1"
      }
    },
    "SonataService.input.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b": {
      "type": "OS::Neutron::Subnet",
      "properties": {
        "cidr": "10.0.1.160/27",
        "gateway_ip": "10.0.1.161",
        "name": "SonataService.input.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "network": {
          "get_resource": "SonataService.input.net.6b4c2ba0-02f2-4e77-8185-e770c4757f3b"
        }
      }
    },
    "SonataService.mgmt.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b": {
      "type": "OS::Neutron::Subnet",
      "properties": {
        "gateway_ip": "10.0.1.65",
        "cidr": "10.0.1.64/27",
        "dns_nameservers": [
          "8.8.8.8"
        ],
        "name": "SonataService.mgmt.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "network": {
          "get_resource": "SonataService.mgmt.net.6b4c2ba0-02f2-4e77-8185-e770c4757f3b"
        }
      }
    },
    "SonataService.output.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b": {
      "type": "OS::Neutron::Subnet",
      "properties": {
        "cidr": "10.0.1.192/27",
        "gateway_ip": "10.0.1.193",
        "name": "SonataService.output.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "network": {
          "get_resource": "SonataService.output.net.6b4c2ba0-02f2-4e77-8185-e770c4757f3b"
        }
      }
    },
    "SonataService.input.net.6b4c2ba0-02f2-4e77-8185-e770c4757f3b": {
      "type": "OS::Neutron::Net",
      "properties": {
        "name": "SonatService.input.net.6b4c2ba0-02f2-4e77-8185-e770c4757f3b"
      }
    },
    "SonataService.mgmt.net.6b4c2ba0-02f2-4e77-8185-e770c4757f3b": {
      "type": "OS::Neutron::Net",
      "properties": {
        "name": "SonatService.mgmt.net.6b4c2ba0-02f2-4e77-8185-e770c4757f3b"
      }
    },
    "SonataService.output.net.6b4c2ba0-02f2-4e77-8185-e770c4757f3b": {
      "type": "OS::Neutron::Net",
      "properties": {
        "name": "SonatService.output.net.6b4c2ba0-02f2-4e77-8185-e770c4757f3b"
      }
    },
    "SonataService.output.internal.6b4c2ba0-02f2-4e77-8185-e770c4757f3b": {
      "type": "OS::Neutron::RouterInterface",
      "properties": {
        "subnet": {
          "get_resource": "SonataService.output.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b"
        },
        "router": "95a8c9dc-de39-4823-a19a-ff86a54f7bb1"
      }
    },
    "SonataService.external.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b": {
      "type": "OS::Neutron::Subnet",
      "properties": {
        "gateway_ip": "10.0.1.97",
        "cidr": "10.0.1.96/27",
        "dns_nameservers": [
          "8.8.8.8"
        ],
        "name": "SonataService.external.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "network": {
          "get_resource": "SonataService.external.net.6b4c2ba0-02f2-4e77-8185-e770c4757f3b"
        }
      }
    },
    "SonataService.internal.net.6b4c2ba0-02f2-4e77-8185-e770c4757f3b": {
      "type": "OS::Neutron::Net",
      "properties": {
        "name": "SonatService.internal.net.6b4c2ba0-02f2-4e77-8185-e770c4757f3b"
      }
    },
    "SonataService.internal.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b": {
      "type": "OS::Neutron::Subnet",
      "properties": {
        "cidr": "10.0.1.128/27",
        "gateway_ip": "10.0.1.129",
        "name": "SonataService.internal.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "network": {
          "get_resource": "SonataService.internal.net.6b4c2ba0-02f2-4e77-8185-e770c4757f3b"
        }
      }
    },
    "SonataService.ext.internal.6b4c2ba0-02f2-4e77-8185-e770c4757f3b": {
      "type": "OS::Neutron::RouterInterface",
      "properties": {
        "subnet": {
          "get_resource": "SonataService.external.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b"
        },
        "router": "95a8c9dc-de39-4823-a19a-ff86a54f7bb1"
      }
    },
    "SonataService.external.net.6b4c2ba0-02f2-4e77-8185-e770c4757f3b": {
      "type": "OS::Neutron::Net",
      "properties": {
        "name": "SonatService.external.net.6b4c2ba0-02f2-4e77-8185-e770c4757f3b"
      }
    },
    "SonataService.mgmt.internal.6b4c2ba0-02f2-4e77-8185-e770c4757f3b": {
      "type": "OS::Neutron::RouterInterface",
      "properties": {
        "subnet": {
          "get_resource": "SonataService.mgmt.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b"
        },
        "router": "95a8c9dc-de39-4823-a19a-ff86a54f7bb1"
      }
    }
  }
}

patch = "The request is accepted for processing."

def resources(stack_id, stack_name):
  resources = {
    "resources": [
      {
        "resource_name": "cirros-image-1_6b4c2ba0-02f2-4e77-8185-e770c4757f3b_spAddressCloudConfig",
        "links": [
          {
            "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/{stack_name}/{stack_id}/resources/cirros-image-1_6b4c2ba0-02f2-4e77-8185-e770c4757f3b_spAddressCloudConfig".format(stack_name=stack_name, stack_id=stack_id),
            "rel": "self"
          },
          {
            "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/{stack_name}/{stack_id}".format(stack_name=stack_name, stack_id=stack_id),
            "rel": "stack"
          }
        ],
        "logical_resource_id": "cirros-image-1_6b4c2ba0-02f2-4e77-8185-e770c4757f3b_spAddressCloudConfig",
        "creation_time": "2020-03-02T14:06:13Z",
        "resource_status": "CREATE_COMPLETE",
        "updated_time": "2020-03-02T14:06:11Z",
        "required_by": [
          "cirros-image-1.cirros-image-1.6b4c2ba0-02f2-4e77-8185-e770c4757f3b"
        ],
        "resource_status_reason": "state changed",
        "physical_resource_id": "45f24dea-7a6f-4aa4-9395-3025a59b2797",
        "resource_type": "OS::Heat::CloudConfig"
      },
      {
        "resource_name": "SonataService.output.internal.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "links": [
          {
            "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/{stack_name}/{stack_id}/resources/SonataService.output.internal.6b4c2ba0-02f2-4e77-8185-e770c4757f3b".format(stack_name=stack_name, stack_id=stack_id),
            "rel": "self"
          },
          {
            "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/{stack_name}/{stack_id}".format(stack_name=stack_name, stack_id=stack_id),
            "rel": "stack"
          }
        ],
        "logical_resource_id": "SonataService.output.internal.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "creation_time": "2020-03-02T14:05:54Z",
        "resource_status": "CREATE_COMPLETE",
        "updated_time": "2020-03-02T14:05:54Z",
        "required_by": [
          
        ],
        "resource_status_reason": "state changed",
        "physical_resource_id": "95a8c9dc-de39-4823-a19a-ff86a54f7bb1:subnet_id=bb7e71a2-932e-4fe1-9dfa-8e5ade668da4",
        "resource_type": "OS::Neutron::RouterInterface"
      },
      {
        "resource_name": "SonataService.input.internal.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "links": [
          {
            "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/{stack_name}/{stack_id}/resources/SonataService.input.internal.6b4c2ba0-02f2-4e77-8185-e770c4757f3b".format(stack_name=stack_name, stack_id=stack_id),
            "rel": "self"
          },
          {
            "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/{stack_name}/{stack_id}".format(stack_name=stack_name, stack_id=stack_id),
            "rel": "stack"
          }
        ],
        "logical_resource_id": "SonataService.input.internal.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "creation_time": "2020-03-02T14:05:55Z",
        "resource_status": "CREATE_COMPLETE",
        "updated_time": "2020-03-02T14:05:55Z",
        "required_by": [
          
        ],
        "resource_status_reason": "state changed",
        "physical_resource_id": "95a8c9dc-de39-4823-a19a-ff86a54f7bb1:subnet_id=913dce42-6790-4732-b944-7b9c4887ac10",
        "resource_type": "OS::Neutron::RouterInterface"
      },
      {
        "resource_name": "SonataService.input.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "links": [
          {
            "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/{stack_name}/{stack_id}/resources/SonataService.input.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b".format(stack_name=stack_name, stack_id=stack_id),
            "rel": "self"
          },
          {
            "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/{stack_name}/{stack_id}".format(stack_name=stack_name, stack_id=stack_id),
            "rel": "stack"
          }
        ],
        "logical_resource_id": "SonataService.input.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "creation_time": "2020-03-02T14:05:55Z",
        "resource_status": "CREATE_COMPLETE",
        "updated_time": "2020-03-02T14:05:55Z",
        "required_by": [
          "SonataService.input.internal.6b4c2ba0-02f2-4e77-8185-e770c4757f3b"
        ],
        "resource_status_reason": "state changed",
        "physical_resource_id": "913dce42-6790-4732-b944-7b9c4887ac10",
        "resource_type": "OS::Neutron::Subnet"
      },
      {
        "resource_name": "SonataService.mgmt.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "links": [
          {
            "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/{stack_name}/{stack_id}/resources/SonataService.mgmt.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b".format(stack_name=stack_name, stack_id=stack_id),
            "rel": "self"
          },
          {
            "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/{stack_name}/{stack_id}".format(stack_name=stack_name, stack_id=stack_id),
            "rel": "stack"
          }
        ],
        "logical_resource_id": "SonataService.mgmt.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "creation_time": "2020-03-02T14:05:54Z",
        "resource_status": "CREATE_COMPLETE",
        "updated_time": "2020-03-02T14:05:54Z",
        "required_by": [
          "SonataService.mgmt.internal.6b4c2ba0-02f2-4e77-8185-e770c4757f3b"
        ],
        "resource_status_reason": "state changed",
        "physical_resource_id": "68fe0d27-3e79-432a-994d-77fedf6022ba",
        "resource_type": "OS::Neutron::Subnet"
      },
      {
        "resource_name": "SonataService.output.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "links": [
          {
            "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/{stack_name}/{stack_id}/resources/SonataService.output.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b".format(stack_name=stack_name, stack_id=stack_id),
            "rel": "self"
          },
          {
            "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/{stack_name}/{stack_id}".format(stack_name=stack_name, stack_id=stack_id),
            "rel": "stack"
          }
        ],
        "logical_resource_id": "SonataService.output.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "creation_time": "2020-03-02T14:05:54Z",
        "resource_status": "CREATE_COMPLETE",
        "updated_time": "2020-03-02T14:05:54Z",
        "required_by": [
          "SonataService.output.internal.6b4c2ba0-02f2-4e77-8185-e770c4757f3b"
        ],
        "resource_status_reason": "state changed",
        "physical_resource_id": "bb7e71a2-932e-4fe1-9dfa-8e5ade668da4",
        "resource_type": "OS::Neutron::Subnet"
      },
      {
        "resource_name": "SonataService.input.net.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "links": [
          {
            "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/{stack_name}/{stack_id}/resources/SonataService.input.net.6b4c2ba0-02f2-4e77-8185-e770c4757f3b".format(stack_name=stack_name, stack_id=stack_id),
            "rel": "self"
          },
          {
            "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/{stack_name}/{stack_id}".format(stack_name=stack_name, stack_id=stack_id),
            "rel": "stack"
          }
        ],
        "logical_resource_id": "SonataService.input.net.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "creation_time": "2020-03-02T14:05:55Z",
        "resource_status": "CREATE_COMPLETE",
        "updated_time": "2020-03-02T14:05:55Z",
        "required_by": [
          "SonataService.input.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b"
        ],
        "resource_status_reason": "state changed",
        "physical_resource_id": "331d5c5d-bba9-4b0b-adf5-da83f4861fc0",
        "resource_type": "OS::Neutron::Net"
      },
      {
        "resource_name": "SonataService.mgmt.net.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "links": [
          {
            "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/{stack_name}/{stack_id}/resources/SonataService.mgmt.net.6b4c2ba0-02f2-4e77-8185-e770c4757f3b".format(stack_name=stack_name, stack_id=stack_id),
            "rel": "self"
          },
          {
            "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/{stack_name}/{stack_id}".format(stack_name=stack_name, stack_id=stack_id),
            "rel": "stack"
          }
        ],
        "logical_resource_id": "SonataService.mgmt.net.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "creation_time": "2020-03-02T14:05:55Z",
        "resource_status": "CREATE_COMPLETE",
        "updated_time": "2020-03-02T14:05:55Z",
        "required_by": [
          "SonataService.mgmt.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b"
        ],
        "resource_status_reason": "state changed",
        "physical_resource_id": "0661b73a-5008-4cb6-a01c-0ffa58d8a0b9",
        "resource_type": "OS::Neutron::Net"
      },
      {
        "resource_name": "SonataService.output.net.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "links": [
          {
            "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/{stack_name}/{stack_id}/resources/SonataService.output.net.6b4c2ba0-02f2-4e77-8185-e770c4757f3b".format(stack_name=stack_name, stack_id=stack_id),
            "rel": "self"
          },
          {
            "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/{stack_name}/{stack_id}".format(stack_name=stack_name, stack_id=stack_id),
            "rel": "stack"
          }
        ],
        "logical_resource_id": "SonataService.output.net.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "creation_time": "2020-03-02T14:05:55Z",
        "resource_status": "CREATE_COMPLETE",
        "updated_time": "2020-03-02T14:05:55Z",
        "required_by": [
          "SonataService.output.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b"
        ],
        "resource_status_reason": "state changed",
        "physical_resource_id": "c61f2f91-94b6-49b4-b920-d0c3689e8342",
        "resource_type": "OS::Neutron::Net"
      },
      {
        "resource_name": "cirros-image-1.cirros-image-1.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "links": [
          {
            "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/{stack_name}/{stack_id}/resources/cirros-image-1.cirros-image-1.6b4c2ba0-02f2-4e77-8185-e770c4757f3b".format(stack_name=stack_name, stack_id=stack_id),
            "rel": "self"
          },
          {
            "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/{stack_name}/{stack_id}".format(stack_name=stack_name, stack_id=stack_id),
            "rel": "stack"
          },
          {
            "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/{stack_name}-cirros-image-1.cirros-image-1.6b4c2ba0-02f2-4e77-8185-e770c4757f3b-tzgmdqfr6ur2/a45679f4-643a-4ba4-845a-c3c9ade12b6b".format(stack_name=stack_name),
            "rel": "nested"
          }
        ],
        "logical_resource_id": "cirros-image-1.cirros-image-1.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "creation_time": "2020-03-02T14:06:12Z",
        "resource_status_reason": "state changed",
        "updated_time": "2020-03-02T14:06:11Z",
        "required_by": [
          
        ],
        "resource_status": "CREATE_COMPLETE",
        "physical_resource_id": "a45679f4-643a-4ba4-845a-c3c9ade12b6b",
        "resource_type": "OS::Heat::ResourceGroup"
      },
      {
        "resource_name": "SonataService.internal.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "links": [
          {
            "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/{stack_name}/{stack_id}/resources/SonataService.internal.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b".format(stack_name=stack_name, stack_id=stack_id),
            "rel": "self"
          },
          {
            "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/{stack_name}/{stack_id}".format(stack_name=stack_name, stack_id=stack_id),
            "rel": "stack"
          }
        ],
        "logical_resource_id": "SonataService.internal.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "creation_time": "2020-03-02T14:05:54Z",
        "resource_status": "CREATE_COMPLETE",
        "updated_time": "2020-03-02T14:05:54Z",
        "required_by": [
          "cirros-image-1.cirros-image-1.eth0.6b4c2ba0-02f2-4e77-8185-e770c4757f3b"
        ],
        "resource_status_reason": "state changed",
        "physical_resource_id": "8ebb0e88-c5b3-42bf-8a8f-f6105ba222a7",
        "resource_type": "OS::Neutron::Subnet"
      },
      {
        "resource_name": "SonataService.external.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "links": [
          {
            "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/{stack_name}/{stack_id}/resources/SonataService.external.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b".format(stack_name=stack_name, stack_id=stack_id),
            "rel": "self"
          },
          {
            "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/{stack_name}/{stack_id}".format(stack_name=stack_name, stack_id=stack_id),
            "rel": "stack"
          }
        ],
        "logical_resource_id": "SonataService.external.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "creation_time": "2020-03-02T14:05:55Z",
        "resource_status": "CREATE_COMPLETE",
        "updated_time": "2020-03-02T14:05:55Z",
        "required_by": [
          "SonataService.ext.internal.6b4c2ba0-02f2-4e77-8185-e770c4757f3b"
        ],
        "resource_status_reason": "state changed",
        "physical_resource_id": "67485f03-bdd5-480b-aabe-61c08feebf29",
        "resource_type": "OS::Neutron::Subnet"
      },
      {
        "resource_name": "SonataService.internal.net.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "links": [
          {
            "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/{stack_name}/{stack_id}/resources/SonataService.internal.net.6b4c2ba0-02f2-4e77-8185-e770c4757f3b".format(stack_name=stack_name, stack_id=stack_id),
            "rel": "self"
          },
          {
            "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/{stack_name}/{stack_id}".format(stack_name=stack_name, stack_id=stack_id),
            "rel": "stack"
          }
        ],
        "logical_resource_id": "SonataService.internal.net.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "creation_time": "2020-03-02T14:05:55Z",
        "resource_status": "CREATE_COMPLETE",
        "updated_time": "2020-03-02T14:05:55Z",
        "required_by": [
          "SonataService.internal.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
          "cirros-image-1.cirros-image-1.eth0.6b4c2ba0-02f2-4e77-8185-e770c4757f3b"
        ],
        "resource_status_reason": "state changed",
        "physical_resource_id": "457e1c8c-fe4e-4ca0-a9cb-6419ae621584",
        "resource_type": "OS::Neutron::Net"
      },
      {
        "resource_name": "cirros-image-1.cirros-image-1.eth0.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "links": [
          {
            "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/{stack_name}/{stack_id}/resources/cirros-image-1.cirros-image-1.eth0.6b4c2ba0-02f2-4e77-8185-e770c4757f3b".format(stack_name=stack_name, stack_id=stack_id),
            "rel": "self"
          },
          {
            "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/{stack_name}/{stack_id}".format(stack_name=stack_name, stack_id=stack_id),
            "rel": "stack"
          }
        ],
        "logical_resource_id": "cirros-image-1.cirros-image-1.eth0.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "creation_time": "2020-03-02T14:06:12Z",
        "resource_status": "CREATE_COMPLETE",
        "updated_time": "2020-03-02T14:06:11Z",
        "required_by": [
          "cirros-image-1.cirros-image-1.6b4c2ba0-02f2-4e77-8185-e770c4757f3b"
        ],
        "resource_status_reason": "state changed",
        "physical_resource_id": "b3809c9e-15ef-4201-8974-35bf41a960d1",
        "resource_type": "OS::Neutron::Port"
      },
      {
        "resource_name": "SonataService.ext.internal.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "links": [
          {
            "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/{stack_name}/{stack_id}/resources/SonataService.ext.internal.6b4c2ba0-02f2-4e77-8185-e770c4757f3b".format(stack_name=stack_name, stack_id=stack_id),
            "rel": "self"
          },
          {
            "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/{stack_name}/{stack_id}".format(stack_name=stack_name, stack_id=stack_id),
            "rel": "stack"
          }
        ],
        "logical_resource_id": "SonataService.ext.internal.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "creation_time": "2020-03-02T14:05:54Z",
        "resource_status": "CREATE_COMPLETE",
        "updated_time": "2020-03-02T14:05:54Z",
        "required_by": [
          
        ],
        "resource_status_reason": "state changed",
        "physical_resource_id": "95a8c9dc-de39-4823-a19a-ff86a54f7bb1:subnet_id=67485f03-bdd5-480b-aabe-61c08feebf29",
        "resource_type": "OS::Neutron::RouterInterface"
      },
      {
        "resource_name": "SonataService.external.net.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "links": [
          {
            "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/{stack_name}/{stack_id}/resources/SonataService.external.net.6b4c2ba0-02f2-4e77-8185-e770c4757f3b".format(stack_name=stack_name, stack_id=stack_id),
            "rel": "self"
          },
          {
            "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/{stack_name}/{stack_id}".format(stack_name=stack_name, stack_id=stack_id),
            "rel": "stack"
          }
        ],
        "logical_resource_id": "SonataService.external.net.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "creation_time": "2020-03-02T14:05:55Z",
        "resource_status": "CREATE_COMPLETE",
        "updated_time": "2020-03-02T14:05:55Z",
        "required_by": [
          "SonataService.external.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b"
        ],
        "resource_status_reason": "state changed",
        "physical_resource_id": "41b267eb-30d7-4704-8bae-0ff94320cea4",
        "resource_type": "OS::Neutron::Net"
      },
      {
        "resource_name": "SonataService.mgmt.internal.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "links": [
          {
            "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/{stack_name}/{stack_id}/resources/SonataService.mgmt.internal.6b4c2ba0-02f2-4e77-8185-e770c4757f3b".format(stack_name=stack_name, stack_id=stack_id),
            "rel": "self"
          },
          {
            "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/{stack_name}/{stack_id}".format(stack_name=stack_name, stack_id=stack_id),
            "rel": "stack"
          }
        ],
        "logical_resource_id": "SonataService.mgmt.internal.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "creation_time": "2020-03-02T14:05:54Z",
        "resource_status": "CREATE_COMPLETE",
        "updated_time": "2020-03-02T14:05:54Z",
        "required_by": [
          
        ],
        "resource_status_reason": "state changed",
        "physical_resource_id": "95a8c9dc-de39-4823-a19a-ff86a54f7bb1:subnet_id=68fe0d27-3e79-432a-994d-77fedf6022ba",
        "resource_type": "OS::Neutron::RouterInterface"
      }
    ]
  }

def resources_status(stack_id, stack_name, resource_name):
  resources_status = {
    "resource": {
      "resource_name": resource_name,
      "description": "",
      "links": [
        {
          "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/{stack_name}/{stack_id}/resources/{resource_name}".format(stack_name=stack_name, stack_id=stack_id, resource_name=resource_name),
          "rel": "self"
        },
        {
          "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/{stack_name}/{stack_id}".format(stack_name=stack_name, stack_id=stack_id),
          "rel": "stack"
        }
      ],
      "logical_resource_id": resource_name,
      "creation_time": "2020-03-02T14:05:54Z",
      "resource_status": "CREATE_COMPLETE",
      "updated_time": "2020-03-02T14:05:54Z",
      "required_by": [
        
      ],
      "resource_status_reason": "state changed",
      "physical_resource_id": "95a8c9dc-de39-4823-a19a-ff86a54f7bb1:subnet_id=bb7e71a2-932e-4fe1-9dfa-8e5ade668da4",
      "attributes": {
        
      },
      "resource_type": "OS::Neutron::RouterInterface"
    }
  }
  return resources_status