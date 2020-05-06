#!/bin/bash

finish() {
    # Fix ownership of output files
    user_id=$(stat -c '%u:%g' /data)
    chown -R ${user_id} /data
}

echo "Running Flask servers..."

pkill python3

case "$MANO" in
 osm) 
    python3 app/osm-os/auth/auth.py & \
    python3 app/osm-os/glance/glance.py & \
    python3 app/osm-os/neutron/neutron.py & \
    python3 app/osm-os/nova/nova.py & \
    echo "OSM" ;;
 pishahang) 
    python3 app/pishahang-os/auth/auth.py & \
    python3 app/pishahang-os/glance/glance.py & \
    python3 app/pishahang-os/heat/heat.py & \
    python3 app/pishahang-os/nova/nova.py & \
    echo "Pishahang" ;;
 *) 
    exit -1;
esac

# If heat

# DEBUG
# python3 app/pishahang-os/auth/app.py & \
# python3 app/pishahang-os/glance/app.py & \
# python3 app/pishahang-os/heat/app.py & \
# python3 app/pishahang-os/nova/app.py & \
