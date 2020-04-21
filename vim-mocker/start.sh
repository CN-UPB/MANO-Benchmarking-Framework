#!/bin/bash

finish() {
    # Fix ownership of output files
    user_id=$(stat -c '%u:%g' /data)
    chown -R ${user_id} /data
}

echo "Running Flask servers..."

pkill python3

# If heat
# python3 app/pishahang-os/auth/auth.py & \
# python3 app/pishahang-os/glance/glance.py & \
# python3 app/pishahang-os/heat/heat.py & \
# python3 app/pishahang-os/nova/nova.py & \

# DEBUG
# python3 app/pishahang-os/auth/app.py & \
# python3 app/pishahang-os/glance/app.py & \
# python3 app/pishahang-os/heat/app.py & \
# python3 app/pishahang-os/nova/app.py & \

# if OSM-Nova
python3 app/osm-os-obsolete/auth/auth.py & \
python3 app/osm-os-obsolete/glance/glance.py & \
python3 app/osm-os-obsolete/neutron/neutron.py & \
python3 app/osm-os-obsolete/nova/nova.py & \