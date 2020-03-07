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

found = "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/{stack_name}/{stack_id}"


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
  return resources

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

resources_status_individual = {
  "cirros-image-1_6b4c2ba0-02f2-4e77-8185-e770c4757f3b_spAddressCloudConfig": {
  "resource": {
    "resource_name": "cirros-image-1_6b4c2ba0-02f2-4e77-8185-e770c4757f3b_spAddressCloudConfig",
    "description": "",
    "links": [
      {
        "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/SonataService-6b4c2ba0-02f2-4e77-8185-e770c4757f3b/1a2d5e94-c803-486d-b49d-67f712a37b84/resources/cirros-image-1_6b4c2ba0-02f2-4e77-8185-e770c4757f3b_spAddressCloudConfig",
        "rel": "self"
      },
      {
        "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/SonataService-6b4c2ba0-02f2-4e77-8185-e770c4757f3b/1a2d5e94-c803-486d-b49d-67f712a37b84",
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
    "attributes": {
      "config": "#cloud-config\nwrite_files:\n- {content: 'SP_ADDRESS=131.234.28.240\n\n', path: /etc/sonata_sp_address.conf}\n"
    },
    "resource_type": "OS::Heat::CloudConfig"
  }
},
  "SonataService.output.internal.6b4c2ba0-02f2-4e77-8185-e770c4757f3b": {
  "resource": {
    "resource_name": "SonataService.output.internal.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
    "description": "",
    "links": [
      {
        "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/SonataService-6b4c2ba0-02f2-4e77-8185-e770c4757f3b/1a2d5e94-c803-486d-b49d-67f712a37b84/resources/SonataService.output.internal.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "rel": "self"
      },
      {
        "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/SonataService-6b4c2ba0-02f2-4e77-8185-e770c4757f3b/1a2d5e94-c803-486d-b49d-67f712a37b84",
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
    "attributes": {
      
    },
    "resource_type": "OS::Neutron::RouterInterface"
  }
},
  "SonataService.input.internal.6b4c2ba0-02f2-4e77-8185-e770c4757f3b": {
  "resource": {
    "resource_name": "SonataService.input.internal.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
    "description": "",
    "links": [
      {
        "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/SonataService-6b4c2ba0-02f2-4e77-8185-e770c4757f3b/1a2d5e94-c803-486d-b49d-67f712a37b84/resources/SonataService.input.internal.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "rel": "self"
      },
      {
        "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/SonataService-6b4c2ba0-02f2-4e77-8185-e770c4757f3b/1a2d5e94-c803-486d-b49d-67f712a37b84",
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
    "attributes": {
      
    },
    "resource_type": "OS::Neutron::RouterInterface"
  }
},
  "SonataService.input.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b": {
  "resource": {
    "resource_name": "SonataService.input.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
    "description": "",
    "links": [
      {
        "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/SonataService-6b4c2ba0-02f2-4e77-8185-e770c4757f3b/1a2d5e94-c803-486d-b49d-67f712a37b84/resources/SonataService.input.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "rel": "self"
      },
      {
        "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/SonataService-6b4c2ba0-02f2-4e77-8185-e770c4757f3b/1a2d5e94-c803-486d-b49d-67f712a37b84",
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
    "attributes": {
      "service_types": [
        
      ],
      "description": "",
      "enable_dhcp": True,
      "tags": [
        
      ],
      "network_id": "331d5c5d-bba9-4b0b-adf5-da83f4861fc0",
      "tenant_id": "40d9de036960447dafd7d74d306cf189",
      "created_at": "2020-03-02T14:05:58Z",
      "dns_nameservers": [
        
      ],
      "updated_at": "2020-03-02T14:05:58Z",
      "ipv6_ra_mode": None,
      "allocation_pools": [
        {
          "start": "10.0.1.162",
          "end": "10.0.1.190"
        }
      ],
      "host_routes": [
        
      ],
      "revision_number": 2,
      "ipv6_address_mode": None,
      "ip_version": 4,
      "gateway_ip": "10.0.1.161",
      "cidr": "10.0.1.160/27",
      "project_id": "40d9de036960447dafd7d74d306cf189",
      "id": "913dce42-6790-4732-b944-7b9c4887ac10",
      "subnetpool_id": None,
      "name": "SonataService.input.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b"
    },
    "resource_type": "OS::Neutron::Subnet"
  }
},
  "SonataService.mgmt.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b": {
  "resource": {
    "resource_name": "SonataService.mgmt.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
    "description": "",
    "links": [
      {
        "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/SonataService-6b4c2ba0-02f2-4e77-8185-e770c4757f3b/1a2d5e94-c803-486d-b49d-67f712a37b84/resources/SonataService.mgmt.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "rel": "self"
      },
      {
        "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/SonataService-6b4c2ba0-02f2-4e77-8185-e770c4757f3b/1a2d5e94-c803-486d-b49d-67f712a37b84",
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
    "attributes": {
      "service_types": [
        
      ],
      "description": "",
      "enable_dhcp": True,
      "tags": [
        
      ],
      "network_id": "0661b73a-5008-4cb6-a01c-0ffa58d8a0b9",
      "tenant_id": "40d9de036960447dafd7d74d306cf189",
      "created_at": "2020-03-02T14:06:01Z",
      "dns_nameservers": [
        "8.8.8.8"
      ],
      "updated_at": "2020-03-02T14:06:01Z",
      "ipv6_ra_mode": None,
      "allocation_pools": [
        {
          "start": "10.0.1.66",
          "end": "10.0.1.94"
        }
      ],
      "host_routes": [
        
      ],
      "revision_number": 2,
      "ipv6_address_mode": None,
      "ip_version": 4,
      "gateway_ip": "10.0.1.65",
      "cidr": "10.0.1.64/27",
      "project_id": "40d9de036960447dafd7d74d306cf189",
      "id": "68fe0d27-3e79-432a-994d-77fedf6022ba",
      "subnetpool_id": None,
      "name": "SonataService.mgmt.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b"
    },
    "resource_type": "OS::Neutron::Subnet"
  }
},
  "SonataService.output.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b": {
  "resource": {
    "resource_name": "SonataService.output.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
    "description": "",
    "links": [
      {
        "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/SonataService-6b4c2ba0-02f2-4e77-8185-e770c4757f3b/1a2d5e94-c803-486d-b49d-67f712a37b84/resources/SonataService.output.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "rel": "self"
      },
      {
        "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/SonataService-6b4c2ba0-02f2-4e77-8185-e770c4757f3b/1a2d5e94-c803-486d-b49d-67f712a37b84",
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
    "attributes": {
      "service_types": [
        
      ],
      "description": "",
      "enable_dhcp": True,
      "tags": [
        
      ],
      "network_id": "c61f2f91-94b6-49b4-b920-d0c3689e8342",
      "tenant_id": "40d9de036960447dafd7d74d306cf189",
      "created_at": "2020-03-02T14:06:02Z",
      "dns_nameservers": [
        
      ],
      "updated_at": "2020-03-02T14:06:02Z",
      "ipv6_ra_mode": None,
      "allocation_pools": [
        {
          "start": "10.0.1.194",
          "end": "10.0.1.222"
        }
      ],
      "host_routes": [
        
      ],
      "revision_number": 2,
      "ipv6_address_mode": None,
      "ip_version": 4,
      "gateway_ip": "10.0.1.193",
      "cidr": "10.0.1.192/27",
      "project_id": "40d9de036960447dafd7d74d306cf189",
      "id": "bb7e71a2-932e-4fe1-9dfa-8e5ade668da4",
      "subnetpool_id": None,
      "name": "SonataService.output.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b"
    },
    "resource_type": "OS::Neutron::Subnet"
  }
},
  "SonataService.input.net.6b4c2ba0-02f2-4e77-8185-e770c4757f3b": {
  "resource": {
    "resource_name": "SonataService.input.net.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
    "description": "",
    "links": [
      {
        "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/SonataService-6b4c2ba0-02f2-4e77-8185-e770c4757f3b/1a2d5e94-c803-486d-b49d-67f712a37b84/resources/SonataService.input.net.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "rel": "self"
      },
      {
        "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/SonataService-6b4c2ba0-02f2-4e77-8185-e770c4757f3b/1a2d5e94-c803-486d-b49d-67f712a37b84",
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
    "attributes": {
      "provider:physical_network": None,
      "ipv6_address_scope": None,
      "revision_number": 5,
      "port_security_enabled": True,
      "provider:network_type": "vxlan",
      "id": "331d5c5d-bba9-4b0b-adf5-da83f4861fc0",
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
        "913dce42-6790-4732-b944-7b9c4887ac10"
      ],
      "description": "",
      "tags": [
        
      ],
      "updated_at": "2020-03-02T14:05:58Z",
      "provider:segmentation_id": 84,
      "name": "SonatService.input.net.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
      "admin_state_up": True,
      "tenant_id": "40d9de036960447dafd7d74d306cf189",
      "created_at": "2020-03-02T14:05:56Z",
      "mtu": 1450
    },
    "resource_type": "OS::Neutron::Net"
  }
},
  "SonataService.mgmt.net.6b4c2ba0-02f2-4e77-8185-e770c4757f3b": {
  "resource": {
    "resource_name": "SonataService.mgmt.net.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
    "description": "",
    "links": [
      {
        "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/SonataService-6b4c2ba0-02f2-4e77-8185-e770c4757f3b/1a2d5e94-c803-486d-b49d-67f712a37b84/resources/SonataService.mgmt.net.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "rel": "self"
      },
      {
        "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/SonataService-6b4c2ba0-02f2-4e77-8185-e770c4757f3b/1a2d5e94-c803-486d-b49d-67f712a37b84",
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
    "attributes": {
      "provider:physical_network": None,
      "ipv6_address_scope": None,
      "revision_number": 5,
      "port_security_enabled": True,
      "provider:network_type": "vxlan",
      "id": "0661b73a-5008-4cb6-a01c-0ffa58d8a0b9",
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
        "68fe0d27-3e79-432a-994d-77fedf6022ba"
      ],
      "description": "",
      "tags": [
        
      ],
      "updated_at": "2020-03-02T14:06:01Z",
      "provider:segmentation_id": 101,
      "name": "SonatService.mgmt.net.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
      "admin_state_up": True,
      "tenant_id": "40d9de036960447dafd7d74d306cf189",
      "created_at": "2020-03-02T14:05:58Z",
      "mtu": 1450
    },
    "resource_type": "OS::Neutron::Net"
  }
},
  "SonataService.output.net.6b4c2ba0-02f2-4e77-8185-e770c4757f3b": {
  "resource": {
    "resource_name": "SonataService.output.net.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
    "description": "",
    "links": [
      {
        "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/SonataService-6b4c2ba0-02f2-4e77-8185-e770c4757f3b/1a2d5e94-c803-486d-b49d-67f712a37b84/resources/SonataService.output.net.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "rel": "self"
      },
      {
        "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/SonataService-6b4c2ba0-02f2-4e77-8185-e770c4757f3b/1a2d5e94-c803-486d-b49d-67f712a37b84",
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
    "attributes": {
      "provider:physical_network": None,
      "ipv6_address_scope": None,
      "revision_number": 5,
      "port_security_enabled": True,
      "provider:network_type": "vxlan",
      "id": "c61f2f91-94b6-49b4-b920-d0c3689e8342",
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
        "bb7e71a2-932e-4fe1-9dfa-8e5ade668da4"
      ],
      "description": "",
      "tags": [
        
      ],
      "updated_at": "2020-03-02T14:06:02Z",
      "provider:segmentation_id": 31,
      "name": "SonatService.output.net.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
      "admin_state_up": True,
      "tenant_id": "40d9de036960447dafd7d74d306cf189",
      "created_at": "2020-03-02T14:05:59Z",
      "mtu": 1450
    },
    "resource_type": "OS::Neutron::Net"
  }
},
  "cirros-image-1.cirros-image-1.6b4c2ba0-02f2-4e77-8185-e770c4757f3b": {
  "resource": {
    "resource_name": "cirros-image-1.cirros-image-1.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
    "description": "",
    "links": [
      {
        "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/SonataService-6b4c2ba0-02f2-4e77-8185-e770c4757f3b/1a2d5e94-c803-486d-b49d-67f712a37b84/resources/cirros-image-1.cirros-image-1.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "rel": "self"
      },
      {
        "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/SonataService-6b4c2ba0-02f2-4e77-8185-e770c4757f3b/1a2d5e94-c803-486d-b49d-67f712a37b84",
        "rel": "stack"
      },
      {
        "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/SonataService-6b4c2ba0-02f2-4e77-8185-e770c4757f3b-cirros-image-1.cirros-image-1.6b4c2ba0-02f2-4e77-8185-e770c4757f3b-tzgmdqfr6ur2/a45679f4-643a-4ba4-845a-c3c9ade12b6b",
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
    "attributes": {
      "attributes": None,
      "refs": None,
      "refs_map": None,
      "removed_rsrc_list": [
        
      ]
    },
    "resource_type": "OS::Heat::ResourceGroup"
  }
},
  "SonataService.internal.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b": {
  "resource": {
    "resource_name": "SonataService.internal.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
    "description": "",
    "links": [
      {
        "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/SonataService-6b4c2ba0-02f2-4e77-8185-e770c4757f3b/1a2d5e94-c803-486d-b49d-67f712a37b84/resources/SonataService.internal.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "rel": "self"
      },
      {
        "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/SonataService-6b4c2ba0-02f2-4e77-8185-e770c4757f3b/1a2d5e94-c803-486d-b49d-67f712a37b84",
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
    "attributes": {
      "service_types": [
        
      ],
      "description": "",
      "enable_dhcp": True,
      "tags": [
        
      ],
      "network_id": "457e1c8c-fe4e-4ca0-a9cb-6419ae621584",
      "tenant_id": "40d9de036960447dafd7d74d306cf189",
      "created_at": "2020-03-02T14:06:04Z",
      "dns_nameservers": [
        
      ],
      "updated_at": "2020-03-02T14:06:04Z",
      "ipv6_ra_mode": None,
      "allocation_pools": [
        {
          "start": "10.0.1.130",
          "end": "10.0.1.158"
        }
      ],
      "host_routes": [
        
      ],
      "revision_number": 2,
      "ipv6_address_mode": None,
      "ip_version": 4,
      "gateway_ip": "10.0.1.129",
      "cidr": "10.0.1.128/27",
      "project_id": "40d9de036960447dafd7d74d306cf189",
      "id": "8ebb0e88-c5b3-42bf-8a8f-f6105ba222a7",
      "subnetpool_id": None,
      "name": "SonataService.internal.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b"
    },
    "resource_type": "OS::Neutron::Subnet"
  }
},
  "SonataService.external.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b": {
  "resource": {
    "resource_name": "SonataService.external.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
    "description": "",
    "links": [
      {
        "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/SonataService-6b4c2ba0-02f2-4e77-8185-e770c4757f3b/1a2d5e94-c803-486d-b49d-67f712a37b84/resources/SonataService.external.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "rel": "self"
      },
      {
        "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/SonataService-6b4c2ba0-02f2-4e77-8185-e770c4757f3b/1a2d5e94-c803-486d-b49d-67f712a37b84",
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
    "attributes": {
      "service_types": [
        
      ],
      "description": "",
      "enable_dhcp": True,
      "tags": [
        
      ],
      "network_id": "41b267eb-30d7-4704-8bae-0ff94320cea4",
      "tenant_id": "40d9de036960447dafd7d74d306cf189",
      "created_at": "2020-03-02T14:05:59Z",
      "dns_nameservers": [
        "8.8.8.8"
      ],
      "updated_at": "2020-03-02T14:05:59Z",
      "ipv6_ra_mode": None,
      "allocation_pools": [
        {
          "start": "10.0.1.98",
          "end": "10.0.1.126"
        }
      ],
      "host_routes": [
        
      ],
      "revision_number": 2,
      "ipv6_address_mode": None,
      "ip_version": 4,
      "gateway_ip": "10.0.1.97",
      "cidr": "10.0.1.96/27",
      "project_id": "40d9de036960447dafd7d74d306cf189",
      "id": "67485f03-bdd5-480b-aabe-61c08feebf29",
      "subnetpool_id": None,
      "name": "SonataService.external.subnet.6b4c2ba0-02f2-4e77-8185-e770c4757f3b"
    },
    "resource_type": "OS::Neutron::Subnet"
  }
},
  "SonataService.internal.net.6b4c2ba0-02f2-4e77-8185-e770c4757f3b": {
  "resource": {
    "resource_name": "SonataService.internal.net.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
    "description": "",
    "links": [
      {
        "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/SonataService-6b4c2ba0-02f2-4e77-8185-e770c4757f3b/1a2d5e94-c803-486d-b49d-67f712a37b84/resources/SonataService.internal.net.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "rel": "self"
      },
      {
        "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/SonataService-6b4c2ba0-02f2-4e77-8185-e770c4757f3b/1a2d5e94-c803-486d-b49d-67f712a37b84",
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
    "attributes": {
      "provider:physical_network": None,
      "ipv6_address_scope": None,
      "revision_number": 5,
      "port_security_enabled": True,
      "provider:network_type": "vxlan",
      "id": "457e1c8c-fe4e-4ca0-a9cb-6419ae621584",
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
        "8ebb0e88-c5b3-42bf-8a8f-f6105ba222a7"
      ],
      "description": "",
      "tags": [
        
      ],
      "updated_at": "2020-03-02T14:06:04Z",
      "provider:segmentation_id": 107,
      "name": "SonatService.internal.net.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
      "admin_state_up": True,
      "tenant_id": "40d9de036960447dafd7d74d306cf189",
      "created_at": "2020-03-02T14:06:00Z",
      "mtu": 1450
    },
    "resource_type": "OS::Neutron::Net"
  }
},
  "cirros-image-1.cirros-image-1.eth0.6b4c2ba0-02f2-4e77-8185-e770c4757f3b": {
  "resource": {
    "resource_name": "cirros-image-1.cirros-image-1.eth0.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
    "description": "",
    "links": [
      {
        "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/SonataService-6b4c2ba0-02f2-4e77-8185-e770c4757f3b/1a2d5e94-c803-486d-b49d-67f712a37b84/resources/cirros-image-1.cirros-image-1.eth0.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "rel": "self"
      },
      {
        "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/SonataService-6b4c2ba0-02f2-4e77-8185-e770c4757f3b/1a2d5e94-c803-486d-b49d-67f712a37b84",
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
    "attributes": {
      "allowed_address_pairs": [
        
      ],
      "extra_dhcp_opts": [
        
      ],
      "updated_at": "2020-03-02T14:06:30Z",
      "device_owner": "compute:None",
      "revision_number": 9,
      "port_security_enabled": True,
      "binding:profile": {
        
      },
      "fixed_ips": [
        {
          "subnet_id": "8ebb0e88-c5b3-42bf-8a8f-f6105ba222a7",
          "ip_address": "10.0.1.133"
        }
      ],
      "id": "b3809c9e-15ef-4201-8974-35bf41a960d1",
      "security_groups": [
        "a2167217-dae9-4469-afe0-29d2c87a1110"
      ],
      "binding:vif_details": {
        "port_filter": True,
        "ovs_hybrid_plug": False
      },
      "binding:vif_type": "ovs",
      "mac_address": "fa:16:3e:17:33:b0",
      "project_id": "40d9de036960447dafd7d74d306cf189",
      "status": "ACTIVE",
      "binding:host_id": "pishahang-os",
      "description": "",
      "tags": [
        
      ],
      "device_id": "0052738d-f6b2-4ce0-8e30-5162eaaa0791",
      "name": "cirros-image-1.cirros-image-1.eth0.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
      "admin_state_up": True,
      "network_id": "457e1c8c-fe4e-4ca0-a9cb-6419ae621584",
      "tenant_id": "40d9de036960447dafd7d74d306cf189",
      "created_at": "2020-03-02T14:06:17Z",
      "binding:vnic_type": "normal"
    },
    "resource_type": "OS::Neutron::Port"
  }
},
  "SonataService.ext.internal.6b4c2ba0-02f2-4e77-8185-e770c4757f3b": {
  "resource": {
    "resource_name": "SonataService.ext.internal.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
    "description": "",
    "links": [
      {
        "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/SonataService-6b4c2ba0-02f2-4e77-8185-e770c4757f3b/1a2d5e94-c803-486d-b49d-67f712a37b84/resources/SonataService.ext.internal.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "rel": "self"
      },
      {
        "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/SonataService-6b4c2ba0-02f2-4e77-8185-e770c4757f3b/1a2d5e94-c803-486d-b49d-67f712a37b84",
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
    "attributes": {
      
    },
    "resource_type": "OS::Neutron::RouterInterface"
  }
},
  "SonataService.external.net.6b4c2ba0-02f2-4e77-8185-e770c4757f3b": {
  "resource": {
    "resource_name": "SonataService.external.net.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
    "description": "",
    "links": [
      {
        "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/SonataService-6b4c2ba0-02f2-4e77-8185-e770c4757f3b/1a2d5e94-c803-486d-b49d-67f712a37b84/resources/SonataService.external.net.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "rel": "self"
      },
      {
        "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/SonataService-6b4c2ba0-02f2-4e77-8185-e770c4757f3b/1a2d5e94-c803-486d-b49d-67f712a37b84",
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
    "attributes": {
      "provider:physical_network": None,
      "ipv6_address_scope": None,
      "revision_number": 5,
      "port_security_enabled": True,
      "provider:network_type": "vxlan",
      "id": "41b267eb-30d7-4704-8bae-0ff94320cea4",
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
        "67485f03-bdd5-480b-aabe-61c08feebf29"
      ],
      "description": "",
      "tags": [
        
      ],
      "updated_at": "2020-03-02T14:05:59Z",
      "provider:segmentation_id": 93,
      "name": "SonatService.external.net.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
      "admin_state_up": True,
      "tenant_id": "40d9de036960447dafd7d74d306cf189",
      "created_at": "2020-03-02T14:05:57Z",
      "mtu": 1450
    },
    "resource_type": "OS::Neutron::Net"
  }
},
  "SonataService.mgmt.internal.6b4c2ba0-02f2-4e77-8185-e770c4757f3b": {
  "resource": {
    "resource_name": "SonataService.mgmt.internal.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
    "description": "",
    "links": [
      {
        "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/SonataService-6b4c2ba0-02f2-4e77-8185-e770c4757f3b/1a2d5e94-c803-486d-b49d-67f712a37b84/resources/SonataService.mgmt.internal.6b4c2ba0-02f2-4e77-8185-e770c4757f3b",
        "rel": "self"
      },
      {
        "href": "http://vim-mocker:8004/v1/40d9de036960447dafd7d74d306cf189/stacks/SonataService-6b4c2ba0-02f2-4e77-8185-e770c4757f3b/1a2d5e94-c803-486d-b49d-67f712a37b84",
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
    "attributes": {
      
    },
    "resource_type": "OS::Neutron::RouterInterface"
  }
}
}