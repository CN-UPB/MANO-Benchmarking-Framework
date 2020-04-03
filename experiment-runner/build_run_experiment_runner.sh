sudo docker stop experiment-runner
sudo docker rm experiment-runner
sudo docker build -t experiment-runner -f Dockerfile-dev .

sudo docker run -d --name experiment-runner -v $(pwd):/app  \
        -v /var/run/docker.sock:/container/path/docker.sock \
        experiment-runner

sudo docker exec -it experiment-runner bash