sudo docker stop vim-emu
sudo docker rm vim-emu

cd app/osm-os

sudo docker build -t vim-emu-img .

sudo docker run --name vim-emu -t -d --rm --privileged --pid='host' --network=netosm -v /var/run/docker.sock:/var/run/docker.sock vim-emu-img python3 examples/osm_default_daemon_topology_2_pop.py

# sudo docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' vim-emu

export VIMEMU_HOSTNAME=$(sudo docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' vim-emu)

# RUN the following command with VIM name
osm vim-delete vim-emu-mocker
osm vim-create --name vim-emu-mocker --user username --password password --auth_url http://$VIMEMU_HOSTNAME:6001/v2.0 --tenant tenantName --account_type openstack

sudo docker logs vim-emu -f