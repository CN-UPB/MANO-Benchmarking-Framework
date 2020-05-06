sudo docker stop experiment-runner
sudo docker rm experiment-runner
sudo docker build -t experiment-runner -f Dockerfile-dev .

# sudo docker run -d --name experiment-runner -v $(pwd):/app  \
#         -v /var/run/docker.sock:/container/path/docker.sock \
#         experiment-runner

# sudo docker exec -it experiment-runner bash

# nohup python -u ./run-emu-experiment-osm.py > emu-experiment.log &
# nohup python -u ./run-emu-experiment-sonata.py > emu-experiment.log &
# nohup python -u ./run-experiment-osm.py > experiment.log &
# nohup python -u ./run-experiment-sonata.py > experiment.log &
# nohup python -u ./run-experiment-sonata-k8-scaling.py > 10xpc-experiment.log &