sudo docker stop vim-emu
sudo docker rm vim-emu

cd app/osm-os

sudo docker build -t vim-emu-img .

sudo docker run --name vim-emu -t -d --rm --privileged \
- p 4000:4000 \
- p 10243:10243 \
- p 9005:9005 \
- p 6001:6001 \
- p 9775:9775 \
- p 10697:10697 \
--pid='host' -v /var/run/docker.sock:/var/run/docker.sock vim-emu-img python3 examples/osm_default_daemon_topology_2_pop.py
