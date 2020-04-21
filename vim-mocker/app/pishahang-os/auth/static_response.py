auth_token = {
  "token": {
    "is_domain": False,
    "methods": [
      "password"
    ],
    "roles": [
      {
        "id": "ef90fce64b86482cbb5690083ed0de3b",
        "name": "admin"
      }
    ],
    "expires_at": "2050-03-02T15:05:52.000000Z",
    "project": {
      "domain": {
        "id": "default",
        "name": "Default"
      },
      "id": "40d9de036960447dafd7d74d306cf189",
      "name": "demo"
    },
    "catalog": [
      {
        "endpoints": [
          {
            "url": "http://thesismano2.cs.upb.de:8776/v3/40d9de036960447dafd7d74d306cf189",
            "interface": "internal",
            "region": "RegionOne",
            "region_id": "RegionOne",
            "id": "5e8c4ef810e9483080bd4bafda1d52af"
          },
          {
            "url": "http://thesismano2.cs.upb.de:8776/v3/40d9de036960447dafd7d74d306cf189",
            "interface": "admin",
            "region": "RegionOne",
            "region_id": "RegionOne",
            "id": "a77f6fd8bdf04f2d9aef662c243c1c7d"
          },
          {
            "url": "http://thesismano2.cs.upb.de:8776/v3/40d9de036960447dafd7d74d306cf189",
            "interface": "public",
            "region": "RegionOne",
            "region_id": "RegionOne",
            "id": "c42173e5f98e4276941cd145e70df3e7"
          }
        ],
        "type": "volumev3",
        "id": "04b329a57ddf40b4b5df16ba65902459",
        "name": "cinderv3"
      },
      {
        "endpoints": [
          {
            "url": "http://thesismano2.cs.upb.de:8004/v1/40d9de036960447dafd7d74d306cf189",
            "interface": "internal",
            "region": "RegionOne",
            "region_id": "RegionOne",
            "id": "807619b9f1914908939f64995152b700"
          },
          {
            "url": "http://thesismano2.cs.upb.de:8004/v1/40d9de036960447dafd7d74d306cf189",
            "interface": "admin",
            "region": "RegionOne",
            "region_id": "RegionOne",
            "id": "98f35de9a78440b2869d6fb14635f4d8"
          },
          {
            "url": "http://thesismano2.cs.upb.de:8004/v1/40d9de036960447dafd7d74d306cf189",
            "interface": "public",
            "region": "RegionOne",
            "region_id": "RegionOne",
            "id": "ba57dad4167247689785f68f093eeda8"
          }
        ],
        "type": "orchestration",
        "id": "4448054a127d498f83982fd123df5f4e",
        "name": "heat"
      },
      {
        "endpoints": [
          {
            "url": "http://thesismano2.cs.upb.de:8774/v2.1",
            "interface": "admin",
            "region": "RegionOne",
            "region_id": "RegionOne",
            "id": "20df919f79bb4b3c83145a0329016e62"
          },
          {
            "url": "http://thesismano2.cs.upb.de:8774/v2.1",
            "interface": "internal",
            "region": "RegionOne",
            "region_id": "RegionOne",
            "id": "83be8def65514b09b48ab5ec021caded"
          },
          {
            "url": "http://thesismano2.cs.upb.de:8774/v2.1",
            "interface": "public",
            "region": "RegionOne",
            "region_id": "RegionOne",
            "id": "f906360648c2456593cf250a5da8b016"
          }
        ],
        "type": "compute",
        "id": "52f04927c9d74e2d83d71b932f9fba1e",
        "name": "nova"
      },
      {
        "endpoints": [
          {
            "url": "http://thesismano2.cs.upb.de/placement",
            "interface": "public",
            "region": "RegionOne",
            "region_id": "RegionOne",
            "id": "59f86280fe8b43d288381d0304c1ef17"
          },
          {
            "url": "http://thesismano2.cs.upb.de/placement",
            "interface": "admin",
            "region": "RegionOne",
            "region_id": "RegionOne",
            "id": "6ae4f5c6c62e491d992a76997ebea3ce"
          },
          {
            "url": "http://thesismano2.cs.upb.de/placement",
            "interface": "internal",
            "region": "RegionOne",
            "region_id": "RegionOne",
            "id": "ca0cda3bf843490598e8bf81b8c62867"
          }
        ],
        "type": "placement",
        "id": "627bed172a2f4a27b072ca60f7bc2bfe",
        "name": "placement"
      },
      {
        "endpoints": [
          {
            "url": "http://thesismano2.cs.upb.de:8000/v1",
            "interface": "admin",
            "region": "RegionOne",
            "region_id": "RegionOne",
            "id": "27de018a33914b01a495895aa9f47174"
          },
          {
            "url": "http://thesismano2.cs.upb.de:8000/v1",
            "interface": "internal",
            "region": "RegionOne",
            "region_id": "RegionOne",
            "id": "4158b0a62d9d41deb730a5c79eaa6767"
          },
          {
            "url": "http://thesismano2.cs.upb.de:8000/v1",
            "interface": "public",
            "region": "RegionOne",
            "region_id": "RegionOne",
            "id": "b033cb64578d4d0d9b13a285a0abaf69"
          }
        ],
        "type": "cloudformation",
        "id": "66c1229f2aa34a5c8edc68c4e545dfd8",
        "name": "heat-cfn"
      },
      {
        "endpoints": [
          {
            "url": "http://thesismano2.cs.upb.de:8774/v2/40d9de036960447dafd7d74d306cf189",
            "interface": "public",
            "region": "RegionOne",
            "region_id": "RegionOne",
            "id": "276148bfdb0b47678ca76a6a17c91d9f"
          },
          {
            "url": "http://thesismano2.cs.upb.de:8774/v2/40d9de036960447dafd7d74d306cf189",
            "interface": "admin",
            "region": "RegionOne",
            "region_id": "RegionOne",
            "id": "60bf0a6f1c90412a82dbc0d7aa1a1603"
          },
          {
            "url": "http://thesismano2.cs.upb.de:8774/v2/40d9de036960447dafd7d74d306cf189",
            "interface": "internal",
            "region": "RegionOne",
            "region_id": "RegionOne",
            "id": "be0b5269fb2440c08b0f4eab82bd5139"
          }
        ],
        "type": "compute_legacy",
        "id": "7b8ce11547a74e46adc5896b1a2d1287",
        "name": "nova_legacy"
      },
      {
        "endpoints": [
          {
            "url": "http://thesismano2.cs.upb.de:9292",
            "interface": "internal",
            "region": "RegionOne",
            "region_id": "RegionOne",
            "id": "407c7e97ce5a4cf1b04485d99a025b1d"
          },
          {
            "url": "http://thesismano2.cs.upb.de:9292",
            "interface": "admin",
            "region": "RegionOne",
            "region_id": "RegionOne",
            "id": "8ee6107692e344d29ea2a962b70b1a28"
          },
          {
            "url": "http://thesismano2.cs.upb.de:9292",
            "interface": "public",
            "region": "RegionOne",
            "region_id": "RegionOne",
            "id": "baae1b2a91214de7bbc9ec05cc128ba5"
          }
        ],
        "type": "image",
        "id": "99e56ee7f46648578060fdbd20fe3b31",
        "name": "glance"
      },
      {
        "endpoints": [
          {
            "url": "http://thesismano2.cs.upb.de:9696/",
            "interface": "public",
            "region": "RegionOne",
            "region_id": "RegionOne",
            "id": "43110874c56a4dbab5184d843c79fab9"
          },
          {
            "url": "http://thesismano2.cs.upb.de:9696/",
            "interface": "admin",
            "region": "RegionOne",
            "region_id": "RegionOne",
            "id": "9c41e12bb35940c386217133292f7dda"
          },
          {
            "url": "http://thesismano2.cs.upb.de:9696/",
            "interface": "internal",
            "region": "RegionOne",
            "region_id": "RegionOne",
            "id": "c5597c06d7334a3186836d86c3c7fafa"
          }
        ],
        "type": "network",
        "id": "a16fc2ca77024eb6a516070fc2115144",
        "name": "neutron"
      },
      {
        "endpoints": [
          {
            "url": "http://thesismano2.cs.upb.de:8776/v1/40d9de036960447dafd7d74d306cf189",
            "interface": "admin",
            "region": "RegionOne",
            "region_id": "RegionOne",
            "id": "12e63481f7024133a81984477424f4e5"
          },
          {
            "url": "http://thesismano2.cs.upb.de:8776/v1/40d9de036960447dafd7d74d306cf189",
            "interface": "public",
            "region": "RegionOne",
            "region_id": "RegionOne",
            "id": "5234fa07dba44b0190ef396db7360560"
          },
          {
            "url": "http://thesismano2.cs.upb.de:8776/v1/40d9de036960447dafd7d74d306cf189",
            "interface": "internal",
            "region": "RegionOne",
            "region_id": "RegionOne",
            "id": "9888d791f0f740a9bed66d822888eb9c"
          }
        ],
        "type": "volume",
        "id": "a436eb386bab4875bf37cdeffbf58096",
        "name": "cinder"
      },
      {
        "endpoints": [
          {
            "url": "http://thesismano2.cs.upb.de:8776/v2/40d9de036960447dafd7d74d306cf189",
            "interface": "internal",
            "region": "RegionOne",
            "region_id": "RegionOne",
            "id": "9ab3ecb6ceb447a8904eabd08bb1cdef"
          },
          {
            "url": "http://thesismano2.cs.upb.de:8776/v2/40d9de036960447dafd7d74d306cf189",
            "interface": "admin",
            "region": "RegionOne",
            "region_id": "RegionOne",
            "id": "d0650f149a4a465f950fd2eda3fdc36c"
          },
          {
            "url": "http://thesismano2.cs.upb.de:8776/v2/40d9de036960447dafd7d74d306cf189",
            "interface": "public",
            "region": "RegionOne",
            "region_id": "RegionOne",
            "id": "d7de9975197e44d49688c4594c368493"
          }
        ],
        "type": "volumev2",
        "id": "b29ab2786c284c78a2a795abc9e2b619",
        "name": "cinderv2"
      },
      {
        "endpoints": [
          {
            "url": "http://thesismano2.cs.upb.de/identity_admin",
            "interface": "admin",
            "region": "RegionOne",
            "region_id": "RegionOne",
            "id": "3145d5e1d48343feb7e59c71bd0e41df"
          },
          {
            "url": "http://thesismano2.cs.upb.de/identity",
            "interface": "public",
            "region": "RegionOne",
            "region_id": "RegionOne",
            "id": "37ec5b9565b34f26b191792bd6b03c52"
          },
          {
            "url": "http://thesismano2.cs.upb.de/identity",
            "interface": "internal",
            "region": "RegionOne",
            "region_id": "RegionOne",
            "id": "418dacd648024244853bfa8791579a36"
          }
        ],
        "type": "identity",
        "id": "cd5ca34f5d3a4c55957f01285753040c",
        "name": "keystone"
      }
    ],
    "user": {
      "password_expires_at": None,
      "domain": {
        "id": "default",
        "name": "Default"
      },
      "id": "f84af8cfd99248fe82b11419a229135f",
      "name": "admin"
    },
    "audit_ids": [
      "lpe2iT-DQ1W53NxAXflFzQ"
    ],
    "issued_at": "2020-03-02T14:05:52.000000Z"
  }
}